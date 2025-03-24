from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

strategies = {
    "beginner": [
        {"title": "Bed Defense Basics", "description": "Learn how to protect your bed...", "image": "bed-def.jpg", "difficulty": "Beginner", "icon": "shield"},
        {"title": "Resource Management", "description": "Master the art of collecting...", "image": "bed-gen.png", "difficulty": "Beginner", "icon": "target"},
        {"title": "Rush Tactics", "description": "Learn how to quickly eliminate...", "image": "bed-rush.jpg", "difficulty": "Beginner", "icon": "sword"},
    ],
    "intermediate": [
        {"title": "Island Control", "description": "Techniques to dominate...", "image": "bed-island.jpg", "difficulty": "Intermediate", "icon": "map-pin"},
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

@app.route('/')
def home():
    metadata = {
        "title": "Bedwarsify - Minecraft Bedwars Strategy Guide",
        "description": "Discover pro strategies, watch video tutorials, and explore interactive maps to dominate in Minecraft Bedwars."
    }
    return render_template('index.html', strategies=strategies, videos=videos, metadata=metadata, current_year=datetime.now().year)


if __name__ == '__main__':
    app.run(debug=True)