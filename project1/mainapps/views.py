from django.shortcuts import render
from django.http import HttpResponse

# Request handler
def homepage(request):
    return HttpResponse('Hello World')