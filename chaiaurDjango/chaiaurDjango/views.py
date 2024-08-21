from django.http import HttpResponse

def func1(request):
    return HttpResponse("Hi this is func1")


def func2(request):
    return HttpResponse("Hi this is func2")
