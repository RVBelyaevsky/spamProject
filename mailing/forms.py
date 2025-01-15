from django import forms
from django.forms import BooleanField, ModelForm

from mailing.models import Client, Message, Newsletter


class StyleFormMixin:
    """
     Форма для стализации
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'first_name', 'last_name')


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'body')


class NewsletterForm(StyleFormMixin, ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['message'].queryset = Message.objects.filter(owner=self.instance.owner)
    #     self.fields['client'].queryset = Client.objects.filter(owner=self.instance.owner)

    class Meta:
        model = Newsletter
        fields = ('first_sending', 'end_sending', 'status', 'clients', 'message')


# class NewsletterModeratorForm(StyleFormMixin, ModelForm):
#     class Meta:
#         model = Newsletter
#         fields = ('status',)'''
