import requests

url = 'http://localhost:3000/api/rt/'
headers = {'Authorization': 'Bearer mytoken'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json().get('generators')
    print(data)
else:
    print(f"Failed to fetch generators. Status code: {response.status_code}")


'''import requests
from your_project_name.your_app_name.models import ReactionTime

import base.serializers
from base import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError

url = 'http://localhost:3000/api/rt/'
headers = {'Authorization': 'Bearer mytoken'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    generators = response.json().get('generators')

    # Here, assuming the serializer is from Django Rest Framework
    serializer = base.serializers.ReactionTimeSerializer(generators=generators, many=True)

    if serializer.is_valid():
        try:
            # Save the validated generators to the model
            serializer.save()
            print("Data has been saved successfully")
        except ValidationError as e:
            print(f"Error while saving generators: {e}")
    else:
        print(f"Error in serialization: {serializer.errors}")
else:
    print(f"Failed to fetch generators. Status code: {response.status_code}")'''
