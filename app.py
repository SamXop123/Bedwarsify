from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "b1f3cb867a6477c36f7d0dfbbce70816" 

users_db = {
    "testuser": {"email": "testuser@example.com", "password": "password123"}
}


strategies = {
    "beginner": [
        {"id": "bed-defense-basics", "title": "Bed Defense Basics", "description": "Learn how to protect your bed...", "image": "bed-def.jpg", "difficulty": "Beginner", "icon": "shield"},
        {"id": "resource-management", "title": "Resource Management", "description": "Master the art of collecting...", "image": "emerald.jpg", "difficulty": "Beginner", "icon": "target"},
        {"id": "rush-tactics", "title": "Rush Tactics", "description": "Learn how to quickly eliminate...", "image": "bed-rush.jpg", "difficulty": "Beginner", "icon": "sword"},
    ],
    "intermediate": [
        {"id": "island-control", "title": "Island Control", "description": "Techniques to dominate...", "image": "islands.jpg", "difficulty": "Intermediate", "icon": "map-pin"},
        {"id": "team-coordination", "title": "Team Coordination", "description": "Learn effective communication...", "image": "bed-team.jpg", "difficulty": "Intermediate", "icon": "target"},
        {"id": "mid-game-transitions", "title": "Mid-Game Transitions", "description": "How to adapt your strategy...", "image": "bed-transition.jpg", "difficulty": "Intermediate", "icon": "sword"},
    ],
    "advanced": [
        {"id": "advanced-bridging", "title": "Advanced Bridging", "description": "Master speed bridging...", "image": "tellybridge.jpg", "difficulty": "Advanced", "icon": "map-pin"},
        {"id": "counter-strategies", "title": "Counter Strategies", "description": "How to counter common tactics...", "image": "counter.jpg", "difficulty": "Advanced", "icon": "shield"},
        {"id": "solo-carry-techniques", "title": "Solo Carry Techniques", "description": "Advanced strategies for carrying...", "image": "hq720_2.jpg", "difficulty": "Advanced", "icon": "sword"},
    ]
}

videos = [
    {"title": "Ultimate Bed Defense Tutorial", "duration": "8:24", "views": "68K", "image": "sddefault.jpg", "url": "https://youtu.be/aEHtUboGcgg?si=JcZsBaaWf4hkFzc2"},
    {"title": "Pro Bridging Techniques", "duration": "6:00", "views": "2.7K", "image": "hq720.jpg", "url": "https://youtu.be/P9j7MCkZjsg?si=kw1oTwSTskhtP3KO"},
    {"title": "How to Win 1v4 Situations", "duration": "25:28", "views": "55K", "image": "maxresdefault.jpg", "url": "https://youtu.be/VirKwKNyv30?si=jEeF9RMQAm08BFGx"},
]

default_metadata = {
    "title": "Bedwarsify - Minecraft Bedwars Strategy Guide",
    "description": "Discover pro strategies, watch video tutorials, and explore interactive maps to dominate in Minecraft Bedwars."
}

def find_strategy(strategy_id):
    for level, items in strategies.items():
        for strategy in items:
            if strategy['id'] == strategy_id:
                return strategy, level
    return None, None


@app.route('/')
def home():
    return render_template('index.html', strategies=strategies, videos=videos, metadata=default_metadata, current_year=datetime.now().year)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_db.get(username)

        if user and user['password'] == password:  
            session['username'] = username  
            flash("Logged in successfully!", "success")
            return redirect(url_for('home')) 
        else:
            flash("Invalid username or password", "danger")
            return render_template('login.html', error="Invalid username or password", metadata=default_metadata)

    return render_template('login.html', metadata=default_metadata)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username in users_db:
            flash("Username already exists", "danger")
            return render_template('signup.html', error="Username already exists", metadata=default_metadata)

        users_db[username] = {'email': email, 'password': password}  
        flash("Account created successfully! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html', metadata=default_metadata)


@app.route('/logout')
def logout():
    session.pop('username', None)  
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


@app.route('/about')
def about():
    about_metadata = {
        "title": "About Bedwarsify - Learn More About Us",
        "description": "Discover the story behind Bedwarsify, our mission to empower Minecraft Bedwars players, and meet the team behind the site."
    }
    return render_template('about.html', metadata=about_metadata)


@app.route('/guide/<strategy_id>')
def guide(strategy_id):
    strategy, level = find_strategy(strategy_id)
    if not strategy:
        flash("Strategy not found.", "danger")
        return redirect(url_for('home') + '#learn-strategy')

    guide_metadata = {
        "title": f"Bedwarsify - {strategy['title']} Guide",
        "description": f"Learn how to master {strategy['title']} in Minecraft Bedwars with this detailed guide."
    }

    guide_content = {
        "bed-defense-basics": {
            "title": "Bed Defense Basics",
            "content": """
                <h3>Introduction</h3>
                <p>Protecting your bed is the most important aspect of Bedwars. Without a bed, you cannot respawn, making it critical to defend it effectively.</p>
                
                <h3>Step 1: Gather Resources</h3>
                <p>Start by collecting iron and gold from your island's generators. Use these to purchase wool or wood from the shop.</p>
                
                <h3>Step 2: Build a Basic Defense</h3>
                <p>Surround your bed with layers of wool or wood. Wool is cheap and quick to place, making it ideal for early-game defense.</p>
                
                <h3>Step 3: Upgrade Your Defense</h3>
                <p>As you gather more resources, add stronger materials like end stone or obsidian. Use emeralds to buy obsidian for the ultimate protection.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Always leave a small entrance to your bed so you can escape if needed.</li>
                    <li>Place traps like mining fatigue or alarm traps to alert you of enemies.</li>
                    <li>Work with your team to defend the bed while others gather resources.</li>
                </ul>
            """
        },
        "resource-management": {
            "title": "Resource Management",
            "content": """
                <h3>Introduction</h3>
                <p>Efficient resource management can give you a significant advantage in Bedwars. Knowing what to collect and when to spend is key.</p>
                
                <h3>Step 1: Prioritize Iron and Gold</h3>
                <p>Focus on collecting iron and gold early in the game. These resources are essential for basic items like wool, tools, and armor.</p>
                
                <h3>Step 2: Collect Emeralds Strategically</h3>
                <p>Once your base is secure, head to the center islands to collect emeralds. Use them to buy powerful items like obsidian or diamond swords.</p>
                
                <h3>Step 3: Spend Wisely</h3>
                <p>Don’t waste resources on unnecessary items. For example, only buy a pickaxe if you need to break through enemy defenses.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Always keep a stack of wool for quick bridging.</li>
                    <li>Coordinate with your team to share resources efficiently.</li>
                    <li>Upgrade your generators to increase resource production.</li>
                </ul>
            """
        },
        "rush-tactics": {
            "title": "Rush Tactics",
            "content": """
                <h3>Introduction</h3>
                <p>Rushing is a high-risk, high-reward strategy that involves quickly attacking enemy teams to destroy their beds.</p>
                
                <h3>Step 1: Prepare Quickly</h3>
                <p>Grab a stack of wool and a sword as soon as the game starts. Speed is key in a rush strategy.</p>
                
                <h3>Step 2: Bridge to the Enemy</h3>
                <p>Use your wool to bridge to the nearest enemy island. Build at an angle to avoid being knocked off easily.</p>
                
                <h3>Step 3: Destroy the Bed</h3>
                <p>Break the enemy bed as quickly as possible. If they have a defense, use a pickaxe or TNT to break through.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Bring a fireball to knock enemies off their island.</li>
                    <li>Be prepared to fight—rushing often leads to early confrontations.</li>
                    <li>Communicate with your team to coordinate a multi-directional rush.</li>
                </ul>
            """
        },
        "island-control": {
            "title": "Island Control",
            "content": """
                <h3>Introduction</h3>
                <p>Controlling key islands can give you access to valuable resources and strategic positions.</p>
                
                <h3>Step 1: Secure Your Base</h3>
                <p>Before heading out, ensure your bed is defended with at least a basic layer of protection.</p>
                
                <h3>Step 2: Capture Diamond Islands</h3>
                <p>Bridge to the nearest diamond islands and control them. Diamonds allow you to upgrade your gear and defenses.</p>
                
                <h3>Step 3: Hold the Center</h3>
                <p>Once you have diamonds, move to the center to collect emeralds. Build defenses to hold the position.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Use invisibility potions to sneak into enemy-controlled islands.</li>
                    <li>Place blocks to block enemy bridges to your controlled islands.</li>
                    <li>Work with your team to maintain control of multiple islands.</li>
                </ul>
            """
        },
        "team-coordination": {
            "title": "Team Coordination",
            "content": """
                <h3>Introduction</h3>
                <p>Effective team coordination can make or break a Bedwars match. Communication is key.</p>
                
                <h3>Step 1: Assign Roles</h3>
                <p>At the start of the game, assign roles: one player defends, one collects resources, and others rush or support.</p>
                
                <h3>Step 2: Communicate Constantly</h3>
                <p>Use voice chat or in-game chat to keep your team updated on enemy movements and resource needs.</p>
                
                <h3>Step 3: Support Each Other</h3>
                <p>If a teammate is rushing, provide them with resources or backup. If someone is defending, help reinforce the bed.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Share resources like emeralds and diamonds with your team.</li>
                    <li>Call out enemy positions to help your team prepare.</li>
                    <li>Stay positive—good morale can improve team performance.</li>
                </ul>
            """
        },
        "mid-game-transitions": {
            "title": "Mid-Game Transitions",
            "content": """
                <h3>Introduction</h3>
                <p>The mid-game is a critical phase where you need to adapt your strategy based on the state of the match.</p>
                
                <h3>Step 1: Assess the Situation</h3>
                <p>Check which teams are still alive and whether your bed is still intact. Adjust your strategy accordingly.</p>
                
                <h3>Step 2: Upgrade Your Gear</h3>
                <p>Use diamonds and emeralds to buy better armor, weapons, and tools. A diamond sword and iron armor can make a big difference.</p>
                
                <h3>Step 3: Plan Your Next Move</h3>
                <p>If your bed is safe, focus on eliminating other teams. If your bed is gone, play more aggressively to take out enemies.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Keep an eye on the center—control it to gain more resources.</li>
                    <li>Buy potions like speed or invisibility to gain an edge.</li>
                    <li>Coordinate with your team to decide whether to defend or attack.</li>
                </ul>
            """
        },
        "advanced-bridging": {
            "title": "Advanced Bridging",
            "content": """
                <h3>Introduction</h3>
                <p>Advanced bridging techniques like speed bridging can help you move faster and surprise your enemies.</p>
                
                <h3>Step 1: Practice Speed Bridging</h3>
                <p>Learn to place blocks while moving backward or sideways. This allows you to bridge faster without falling.</p>
                
                <h3>Step 2: Master Ninja Bridging</h3>
                <p>Ninja bridging involves placing blocks at an angle to create a diagonal bridge, making it harder for enemies to knock you off.</p>
                
                <h3>Step 3: Use Scaffolding</h3>
                <p>In some versions of Minecraft, scaffolding can be used for quick vertical bridging. Practice using it to climb islands.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Practice in solo mode to improve your bridging speed.</li>
                    <li>Use a speed potion to bridge even faster.</li>
                    <li>Always have a backup stack of blocks in case you run out.</li>
                </ul>
            """
        },
        "counter-strategies": {
            "title": "Counter Strategies",
            "content": """
                <h3>Introduction</h3>
                <p>Knowing how to counter common Bedwars strategies can give you a significant advantage.</p>
                
                <h3>Countering Rushers</h3>
                <p>If an enemy is rushing, build a quick defense around your bed and prepare to fight. Use a knockback stick to push them off.</p>
                
                <h3>Countering Turtlers</h3>
                <p>Against teams that heavily defend their bed, use TNT or a pickaxe to break through. Invisibility potions can help you sneak in.</p>
                
                <h3>Countering Campers</h3>
                <p>If a team is camping the center, use a fireball or bow to knock them off from a distance before moving in.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Always have a variety of tools (e.g., TNT, pickaxe, fireball) to counter different strategies.</li>
                    <li>Scout enemy bases to understand their playstyle before attacking.</li>
                    <li>Work with your team to execute counters effectively.</li>
                </ul>
            """
        },
        "solo-carry-techniques": {
            "title": "Solo Carry Techniques",
            "content": """
                <h3>Introduction</h3>
                <p>Solo carrying in Bedwars requires a combination of skill, strategy, and game sense to win even with an uncooperative team.</p>
                
                <h3>Step 1: Focus on Your Bed</h3>
                <p>Defend your bed at all costs. Use obsidian and traps to make it nearly impossible for enemies to break.</p>
                
                <h3>Step 2: Gear Up Quickly</h3>
                <p>Rush to diamond islands and the center to collect resources. Buy a diamond sword, iron armor, and potions as soon as possible.</p>
                
                <h3>Step 3: Eliminate Enemies</h3>
                <p>Use your gear advantage to take out enemy teams one by one. Focus on destroying their beds first, then finishing them off.</p>
                
                <h3>Tips</h3>
                <ul>
                    <li>Use invisibility potions to sneak into enemy bases undetected.</li>
                    <li>Always carry a bow to deal with enemies from a distance.</li>
                    <li>Stay calm and focus on one enemy team at a time.</li>
                </ul>
            """
        }
    }

    guide_data = guide_content.get(strategy_id, {
        "title": "Guide Not Found",
        "content": "<p>Sorry, the guide for this strategy is not available yet.</p>"
    })

    return render_template('guide.html', strategy=strategy, level=level, guide_data=guide_data, strategies=strategies, metadata=guide_metadata)


if __name__ == '__main__':
    app.run(debug=True)