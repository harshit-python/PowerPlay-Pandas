from django.shortcuts import render
from django.http import HttpResponse

def league_sphere_home(request):
    """
    Handles the homepage of League Sphere Hub.
    """
    return HttpResponse("this is the homepage for league sphere app")
