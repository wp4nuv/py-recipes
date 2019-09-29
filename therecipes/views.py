from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # main page is for searching; text or category
    return HttpResponse("Hello, world. This is the index.")