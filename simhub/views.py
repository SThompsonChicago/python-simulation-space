from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def solver1(request):
    data = {
        'thing': 3,
        'location': 'thingland'
    }
    return JsonResponse(data)