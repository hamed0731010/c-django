from .views import speed
from django.urls import path
urlpatterns = [
    path('', speed, name='speed'),]