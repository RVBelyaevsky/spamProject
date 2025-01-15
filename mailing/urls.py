from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import index_data, MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, \
    MessageDeleteView, NewsletterListView, NewsletterCreateView, NewsletterUpdateView, NewsletterDeleteView, \
    NewsletterDetailView, LogListView
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView


app_name = MailingConfig.name

urlpatterns = [
    path('', index_data, name='main'),

    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('newsletter_list/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter_create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter_update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter_delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),

    path('log_list/', LogListView.as_view(), name='log_list'),
]
