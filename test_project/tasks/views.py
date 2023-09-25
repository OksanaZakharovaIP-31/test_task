from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'tasks/index.html')

def entry(request):
    return render(request, 'tasks/entry.html')

d
def registration(request):
    return render(request, 'tasks/registration.html')
