from django.http import HttpResponse
from django.shortcuts import render

def renderIndex(request):
    return render(request, 'index.html')

def func1(request):
    return HttpResponse("This is APP Hi this is func1")


def func2(request):
    return HttpResponse("This is APP Hi this is func2")

def rendNestHtml(request):
    return render(request, 'window/ind.html')