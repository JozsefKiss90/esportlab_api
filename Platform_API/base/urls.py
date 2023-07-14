from django.urls import path
from .views import ReactionTimeAPIView, MyView

urlpatterns = [
    path('rt/', ReactionTimeAPIView.as_view(), name='reaction-time-api'),
    path('mymodel/', MyView.as_view(), name='my-model'),
]
