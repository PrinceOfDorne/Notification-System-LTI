from django.shortcuts import render
from .models import Query

def home(request):
    context = {
        'queries': Query.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
