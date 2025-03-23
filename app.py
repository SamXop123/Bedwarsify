from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

strategies = {
    "beginner": [
        {"title": "Bed Defense Basics", "description": "Learn how to protect your bed...", "image": "placeholder.svg", "difficulty": "Beginner", "icon": "shield"},
        {"title": "Resource Management", "description": "Master the art of collecting...", "image": "placeholder.svg", "difficulty": "Beginner", "icon": "target"},
        {"title": "Rush Tactics", "description": "Learn how to quickly eliminate...", "image": "placeholder.svg", "difficulty": "Beginner", "icon": "sword"},
    ],
    "intermediate": [
        {"title": "Island Control", "description": "Techniques to dominate...", "image": "placeholder.svg", "difficulty": "Intermediate", "icon": "map-pin"},
        {"title": "Team Coordination", "description": "Learn effective communication...", "image": "placeholder.svg", "difficulty": "Intermediate", "icon": "target"},
        {"title": "Mid-Game Transitions", "description": "How to adapt your strategy...", "image": "placeholder.svg", "difficulty": "Intermediate", "icon": "sword"},
    ],
    "advanced": [
        {"title": "Advanced Bridging", "description": "Master speed bridging...", "image": "placeholder.svg", "difficulty": "Advanced", "icon": "map-pin"},
        {"title": "Counter Strategies", "description": "How to counter common tactics...", "image": "placeholder.svg", "difficulty": "Advanced", "icon": "shield"},
        {"title": "Solo Carry Techniques", "description": "Advanced strategies for carrying...", "image": "placeholder.svg", "difficulty": "Advanced", "icon": "sword"},
    ]
}

videos = [
    {"title": "Ultimate Bed Defense Tutorial", "duration": "15:24", "views": "245K", "image": "placeholder.svg"},
    {"title": "Pro Bridging Techniques", "duration": "12:08", "views": "189K", "image": "placeholder.svg"},
    {"title": "How to Win 1v4 Situations", "duration": "18:32", "views": "320K", "image": "placeholder.svg"},
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