from django.shortcuts import render
from django.http import HttpResponse

def common_home(request):
    """
    Handles the homepage of common Hub.
    """
    return HttpResponse("this is the homepage for common app")
