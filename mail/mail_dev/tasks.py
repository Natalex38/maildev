from mail.celery import app
from .service import send_mail

@app.task
def send_delayed_mail(data, ulr_mail):
    send_mail(data, ulr_mail)
