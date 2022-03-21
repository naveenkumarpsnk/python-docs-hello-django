from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello My friends - Good Morning, We are alll learning Azure & We are Happy - this is Naveen")
