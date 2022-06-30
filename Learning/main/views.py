from django.shortcuts import render, HttpResponse


def hello_world(request):
    response = '<h1> HELLO WORLD! </h1>'
    return HttpResponse(response)

def main_page(request):
    pass
