from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
       return x + y


@shared_task
def sleepy(x):
       sleep(x)
       return None