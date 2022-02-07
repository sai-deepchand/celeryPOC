from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from celeryPOC import settings

@shared_task
def sleepy(x):
       sleep(x)
       return None


@shared_task
def send_mail_func():
       mail_subject = "testing celery"
       message = "sending mail using celery one more time "
       to_email = '2018129@iiitdmj.ac.in'
       send_mail(
              subject = mail_subject,
              message=message,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[to_email],
              fail_silently=True,
       )
       return "Done"