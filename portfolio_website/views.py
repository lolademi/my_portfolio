from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('hello world')
    return render(request, "portfolio_website/index.html")
