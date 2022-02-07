from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy, send_mail_func

def home(request):
       # sleepy.delay(10)    
       send_mail_func.delay()
       return HttpResponse('<h1> welcome back deepchand!!!!!! </h1> ')

                  