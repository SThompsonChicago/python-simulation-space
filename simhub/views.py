from django.shortcuts import render
from django.http import JsonResponse
from . import calculations

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def solver1(request):
    last = {}
    current = {}
    next = {}
    
    for key in request.GET:
        current[key] = float(request.GET[key])
        last[key] = float(request.GET[key])
        next[key] = float(request.GET[key])

    return JsonResponse(calculations.solver1Function(last, current, next))