from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def users(request):
    # return render(request, 'myapp/home.html')
    return HttpResponse('<h1> Hello Users Page <h1>')
