from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy

def home(request):
       sleepy(5)
       return HttpResponse('<h1> welcome home !!!!!!! </h1> ')

       