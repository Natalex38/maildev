from django.http import HttpResponse
from .models import UserMail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .service import send_mail
from .tasks import send_delayed_mail

def index(request):
    user = UserMail.objects.all()
    data = {
        'users': user
    }
    body_site = render_to_string('../templates/items/user.html', data)
    return HttpResponse(body_site)

@csrf_exempt
def mail_send(request):
    if request.method == 'POST':
        user = UserMail.objects.all()
        data = {
            'users': user
        }
        url_mail = '../templates/mail.html'
        for i in data.get('users'):
            info = {
                'first_name': i.FIRST_NAME,
                'last_name': i.LAST_NAME,
                'birthday': i.BIRTHDAY,
                'mail': i.MAIL
            }
            mail = i.MAIL
            html_body = render_to_string(url_mail, info)
            send_mail(mail, html_body)
            # Функция создания таски на отправку письма
            # send_delayed_mail.delay(mail, html_body)
            i.STATUS = 'Отправлено'
            i.save()

        return redirect('/mail')
