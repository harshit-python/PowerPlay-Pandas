from django.shortcuts import render
from django.http import HttpResponse

def organisations_home(request):
    """
    Handles the homepage of Organisations.
    """
    return HttpResponse("this is the homepage for organisations app")
