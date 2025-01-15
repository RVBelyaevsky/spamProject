from django.contrib import admin

from mailing.models import Client, Message, Newsletter, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'owner')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_sending', 'status')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_try', 'status', 'server_answer')
