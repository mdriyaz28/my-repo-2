from django.shortcuts import render
from django.http import HttpResponse

#Single-Project Multiples -Apps
def f1(request):
    s='''<center><h1>  Hello user ...!</h1><hr color=red width=85%><h2> Welcome Second App2...</h2><hr color=red width=65% /></center>'''
    return HttpResponse(s)

#Mutiple-Urls for Single View
import time
def Dtime(request):

    t=time.ctime()
    s="<center><h1>  Hello user ...!</h1><hr color=red width=85%><h2> The sever current time is..... </h2><hr color=red width=65%/>" , t,"</center>"

    return HttpResponse(s)

#Default View For Wrong Urls
def Home(request):
    s='''<center><h1>  Hello user ...!</h1><hr color=red width=85%><h2> Trying Url is Not- Found</h2><hr color=red width=65% /></center>'''
    return HttpResponse(s)