from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_mail(mail,  html_body):
        msg = EmailMultiAlternatives(subject='Акция!', to=[mail, ], from_email='alexis3898nata@mail.ru')
        msg.attach_alternative(html_body, 'text/html')
        msg.send()