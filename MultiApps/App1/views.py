from django.shortcuts import render
from django.http import HttpResponse

#Single-Project Multiples -Apps
def f1(request):
    s='''<center><h1>  Hello user ...!</h1><hr color=red width=85%><h2> Welcome First App1...</h2><hr color=red width=65%> />'''
    return HttpResponse(s)