import os
import django
import json
import requests
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform_API.settings')
django.setup()

data = [
    {"rt": random.randint(180, 220), "email": f"user{i}@example.com", "acc": 1, "game": "cs" if i < 20 else "lol"} for i in range(40)
]
#response = requests.post('http://127.0.0.1:8000/api/rt/', generators=json.dumps(generators), headers={'Content-Type': 'application/json'})
#print(response.json())

ranks = ["Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster", "Challenger"]
game_time_range = range(5, 51)

data = [
    {
        "game": "cs" if i < 20 else "lol",
        "email": f"user{i}@example.com",
        "rank": random.choice(ranks),
        "best_rank": random.choice(ranks),  # changed from "bestRank"
        "game_time": random.choice(game_time_range),  # changed from "gameTime"
        "age": random.randint(18, 40),
        "rt": random.randint(180, 220),   # add this
        "acc": 1   # and this
    }
    for i in range(40)
]

response = requests.post('http://127.0.0.1:8000/api/game/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
print(response.json())
