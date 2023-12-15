from django.urls import path
from .views import AiController



urlpatterns = [
    path('main',AiController.main) 
]