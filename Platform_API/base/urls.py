from django.urls import path
from .views import ReactionTimeAPIView, GameAPIView, MemoryAPIView, AmpAPIView, HandEyeAPIView, SimonTaskAPIView

urlpatterns = [
    path('rt/', ReactionTimeAPIView.as_view(), name='reaction-time-api'),
    path('game/', GameAPIView.as_view(), name='game-api'),
    path('memory/', MemoryAPIView.as_view(), name='memory-api'),
    path('apm/', AmpAPIView.as_view(), name='apm-api'),
    path('handeye/', HandEyeAPIView.as_view(), name='handeye-api'),
    path('simontask/', SimonTaskAPIView.as_view(), name='simontask-api'),

]
