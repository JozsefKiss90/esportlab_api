from .models import Game
from rest_framework import serializers
from .models import ReactionTime

class ReactionTimeSerializer(serializers.ModelSerializer):
    rtArray = serializers.SerializerMethodField()
    class Meta:
        model = ReactionTime
        fields = ['rtArray', 'rt', 'email', 'acc', 'game']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game', 'email', 'rank', 'best_rank', 'game_time', 'age']

