from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Virat(request):
    return HttpResponse("<h1>Virat is best batsman</h1>")

def Jaddu(request):
    return HttpResponse("<h1><i>Jaddu is best all rounder</i></h1>")