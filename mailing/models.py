from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    first_name = models.CharField(max_length=200, verbose_name='имя')
    last_name = models.CharField(max_length=200, verbose_name='фамилия')
    comment = models.TextField(verbose_name='комментарии', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f"{self.email} клиент ({self.first_name} {self.last_name})"


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='тема')
    body = models.TextField(verbose_name='сообщение')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    STATUS = (
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('finished', 'завершена'),
    )

    first_sending = models.DateTimeField(verbose_name='первая отправка')
    end_sending = models.DateTimeField(verbose_name='окончание отправки')
    status = models.CharField(max_length=15, choices=STATUS, verbose_name='статус')
    is_active = models.BooleanField(default=True, verbose_name='признак активности')

    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ('can_view_newsletter', 'может просмотреть рассылки'),
            ('can_delete_newsletter', 'может отключить рассылки'),
        ]

    def __str__(self):
        return f'Рассылка: {self.first_sending} - {self.end_sending}'


class Log(models.Model):
    last_try = models.DateTimeField(verbose_name='последняя попытка')
    status = models.BooleanField(verbose_name='статус')
    server_answer = models.TextField(verbose_name='ответ сервера', **NULLABLE)

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

    class Meta:
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'

    def __str__(self):
        return f"{self.last_try} {self.status}"
