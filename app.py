from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "b1f3cb867a6477c36f7d0dfbbce70816"
users_db = {
    "testuser": {"email": "testuser@example.com", "password": "password123"}
}

strategies = {
    "beginner": [
        {"title": "Bed Defense Basics", "description": "Learn how to protect your bed...", "image": "bed-def.jpg", "difficulty": "Beginner", "icon": "shield"},
        {"title": "Resource Management", "description": "Master the art of collecting...", "image": "emerald.jpg", "difficulty": "Beginner", "icon": "target"},
        {"title": "Rush Tactics", "description": "Learn how to quickly eliminate...", "image": "bed-rush.jpg", "difficulty": "Beginner", "icon": "sword"},
    ],
    "intermediate": [
        {"title": "Island Control", "description": "Techniques to dominate...", "image": "islands.jpg", "difficulty": "Intermediate", "icon": "map-pin"},
        {"title": "Team Coordination", "description": "Learn effective communication...", "image": "bed-team.jpg", "difficulty": "Intermediate", "icon": "target"},
        {"title": "Mid-Game Transitions", "description": "How to adapt your strategy...", "image": "bed-transition.jpg", "difficulty": "Intermediate", "icon": "sword"},
    ],
    "advanced": [
        {"title": "Advanced Bridging", "description": "Master speed bridging...", "image": "tellybridge.jpg", "difficulty": "Advanced", "icon": "map-pin"},
        {"title": "Counter Strategies", "description": "How to counter common tactics...", "image": "counter.jpg", "difficulty": "Advanced", "icon": "shield"},
        {"title": "Solo Carry Techniques", "description": "Advanced strategies for carrying...", "image": "hq720_2.jpg", "difficulty": "Advanced", "icon": "sword"},
    ]
}

videos = [
    {"title": "Ultimate Bed Defense Tutorial", "duration": "15:24", "views": "245K", "image": "sddefault.jpg", "url": "https://youtu.be/aEHtUboGcgg?si=JcZsBaaWf4hkFzc2"},
    {"title": "Pro Bridging Techniques", "duration": "12:08", "views": "189K", "image": "hq720.jpg", "url": "https://youtu.be/P9j7MCkZjsg?si=kw1oTwSTskhtP3KO"},
    {"title": "How to Win 1v4 Situations", "duration": "18:32", "views": "320K", "image": "maxresdefault.jpg", "url": "https://youtu.be/VirKwKNyv30?si=jEeF9RMQAm08BFGx"},
]

default_metadata = {
    "title": "Bedwarsify - Minecraft Bedwars Strategy Guide",
    "description": "Discover pro strategies, watch video tutorials, and explore interactive maps to dominate in Minecraft Bedwars."
}

@app.route('/')
def home():
    return render_template('index.html', strategies=strategies, videos=videos, metadata=default_metadata, current_year=datetime.now().year)

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_db.get(username)

        if user and user['password'] == password:  # Plain text password comparison (not secure)
            session['username'] = username  # Store the username in session
            flash("Logged in successfully!", "success")
            return redirect(url_for('home'))  # Redirect to the home page
        else:
            flash("Invalid username or password", "danger")
            return render_template('login.html', error="Invalid username or password", metadata=default_metadata)

    return render_template('login.html', metadata=default_metadata)

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username in users_db:
            flash("Username already exists", "danger")
            return render_template('signup.html', error="Username already exists", metadata=default_metadata)

        users_db[username] = {'email': email, 'password': password}  # Store plain text password (not secure)
        flash("Account created successfully! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html', metadata=default_metadata)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from session
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        flash("Message sent successfully! We'll get back to you soon.", "success")
        return redirect(url_for('home'))

    return render_template('contact.html', metadata=default_metadata)

if __name__ == '__main__':
    app.run(debug=True)

