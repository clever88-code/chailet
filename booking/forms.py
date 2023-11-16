from django import forms
from django.core.exceptions import ValidationError
from requests import request
from core.models import *

class Application_forms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder': 'Опишите что вам может потребыватся на столе я хуй знает'})
        self.fields['date_booking'].widget.attrs.update({'placeholder': 'Выберите дату и время'})


    class Meta:
        model = booking
        fields = ['table_booking', 'date_booking', 'description']