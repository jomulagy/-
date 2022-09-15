from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    text = forms.CharField(max_length = 1000)

    class Meta:
        model = Message
        fields = ("text",)