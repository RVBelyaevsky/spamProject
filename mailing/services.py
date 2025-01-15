import pytz

from datetime import datetime

from django.core.mail import send_mail

from config import settings
from config.settings import EMAIL_HOST_USER
from mailing.models import Client, Newsletter


def get_uniq_clients_count():
    all_clients = Client.objects.all()
    email_list = []
    for client in all_clients:
        email_list.append(client.email)

    return len(set(email_list))


def count_mailing_items():
    return Newsletter.objects.count()


def count_active_mailing_items():
    return Newsletter.objects.filter(status='launched').count()


def sending_mail():
    point_time = datetime.now(pytz.timezone(settings.TIME_ZONE))
    newsletters = Newsletter.objects.all().filter(is_active=True)

    for newsletter in newsletters:
        if point_time >= newsletter.first_sending:
            # send mail logic here
            send_mail(
                newsletter.message.title,
                newsletter.message.body,
                EMAIL_HOST_USER,
                list(newsletter.clients.values_list('email', flat=True)),
                fail_silently=False
            )
            print(f'Отправка завершена')
