import os
import django
import json
import requests
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform_API.settings')
django.setup()

# Send POST request
data = [
    {"rt": random.randint(180, 220), "email": f"user{i}@example.com", "acc": 1, "game": "cs" if i < 20 else "lol"} for i in range(40)
]
response = requests.post('http://127.0.0.1:8000/api/rt/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
print(response.json())
