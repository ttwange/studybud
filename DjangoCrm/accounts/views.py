from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")
def contact(request):
    return HttpResponse("Hello contact!")
