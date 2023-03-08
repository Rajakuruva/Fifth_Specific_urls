from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def MSD(request):
    return HttpResponse("<h1>Msd is best finisher in world</h1>")

def Raina(request):
    return HttpResponse("<i>Raina is MR IPL match</i>")