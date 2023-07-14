from rest_framework import serializers
from .models import ReactionTime, MyModel


class ReactionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactionTime
        fields = ['rt', 'email', 'acc', 'game']


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
