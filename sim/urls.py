from django.urls import path
from .views import *

urlpatterns = [
    path('', photo_wall, name='photo_wall'),
]