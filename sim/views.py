from django.shortcuts import render
from .services import get_all_rows

# Create your views here.

def photo_wall(request):
    photos = get_all_rows("Django")
    context = {
        "photos": photos,
    }
    return render(request, "photo_wall.html", context)