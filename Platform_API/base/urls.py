from django.urls import path
from .views import ReactionTimeAPIView, GameAPIView

urlpatterns = [
    path('rt/', ReactionTimeAPIView.as_view(), name='reaction-time-api'),
    path('game/', GameAPIView.as_view(), name='game-api'),
]
