from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homefun(request):
    return HttpResponse("hi this is my homepage")

def contactfun(request):
    return HttpResponse("hi contact me at 9347188888")

def lehangafun(request):
    return render(request, 'lehanga.html')


def hoodiesfun(request):
    return render(request, 'hoodies.html')

