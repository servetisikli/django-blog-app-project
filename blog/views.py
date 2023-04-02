from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return render(request, 'myapp/home.html')
    return HttpResponse('<h1> Hello Blog Page <h1>')