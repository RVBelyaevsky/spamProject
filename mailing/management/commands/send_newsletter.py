from django.core.management.base import BaseCommand

from mailing.services import sending_mail


class Command(BaseCommand):
    help = 'Создаем рассылку'

    def handle(self, *args, **kwargs):
        sending_mail()
