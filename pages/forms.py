from django import forms
from .models import Contact
from .models import OpenAccount


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'from_where',
            'subject',
            'message',
        ]

class OpenAccountForm(forms.ModelForm):
    class Meta:
        model = OpenAccount
        fields = [
            'full_name',
            'national_code',
            'phone',
            'investment',
            'familiarity',
        ]

