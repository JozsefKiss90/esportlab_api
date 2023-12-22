from .models import Game
from rest_framework import serializers
from .models import ReactionTime


class ReactionTimeSerializer(serializers.ModelSerializer):
    rtArray = serializers.ListField(
        child=serializers.FloatField(),  # Specify the type of data in the list
        required=False  # Make it optional or ensure your API always provides it
    )

    def create(self, validated_data):
        # Handle creating a ReactionTime instance from validated data
        # Use your set_rtArray method here if necessary
        return ReactionTime.objects.create(**validated_data)

    class Meta:
        model = ReactionTime
        fields = ['rtArray', 'rt', 'email']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game', 'email', 'rank', 'best_rank', 'game_time', 'age']

