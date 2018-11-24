from django.http import HttpResponse
from django.shortcuts import render


# Basic View, using a Http Response, Request: It's what the client has sent to your server


def hello_world(request):
    #  Without Template
    #    return HttpResponse('Hello World')
    #  With Template
    return render(request, 'home.html')
