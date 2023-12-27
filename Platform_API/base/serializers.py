from .models import Game, Memory, Amp, HandEye, SimonTask, Performance
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

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ['memorySpan', 'email']

    def create(self, validated_data):
        return Memory.objects.create(**validated_data)

class AmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amp
        fields = ['performance', 'email', 'time']

    def create(self, validated_data):
        return Amp.objects.create(**validated_data)

class HandEyeSerializer(serializers.ModelSerializer):
    performance = serializers.ListField(
        child=serializers.FloatField(),  # Specify the type of data in the list
        required=False  # Make it optional or ensure your API always provides it
    )
    def create(self, validated_data):
        handeye = HandEye.objects.create(**validated_data)
        return handeye

    class Meta:
        model = HandEye
        fields = ['performance', 'email']


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['correctPercent', 'avgCompatibleRT', 'avgIncompatibleRT', 'simonEffect']

class SimonTaskSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer()

    class Meta:
        model = SimonTask
        fields = ['performance', 'email', 'created_at']

    def create(self, validated_data):
        performance_data = validated_data.pop('performance')
        performance = Performance.objects.create(**performance_data)
        simon_task = SimonTask.objects.create(performance=performance, **validated_data)
        return simon_task
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game', 'email', 'rank', 'bestRank', 'gameTime', 'age']