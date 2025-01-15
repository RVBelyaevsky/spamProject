from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import ClientForm, MessageForm, NewsletterForm
from mailing.models import Client, Message, Newsletter, Log
from mailing.services import get_uniq_clients_count, count_mailing_items, count_active_mailing_items


def index_data(request):
    context = {'count_mailing_items': count_mailing_items(),
               'count_active_mailing_items': count_active_mailing_items(),
               'count_unic_clients': get_uniq_clients_count(),

               }

    return render(request, 'mailing/index.html', context)


# Клиенты
class ClientListView(ListView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['email', 'first_name', 'last_name']
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(DetailView):
    model = Client


class MessageListView(ListView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    forms = MessageForm
    fields = ['title', 'body', ]
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ['title', 'body']
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsletterForm

        raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')


class NewsletterDetailView(DetailView):
    model = Newsletter


class LogListView(ListView):
    model = Log

