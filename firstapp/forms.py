from django import forms 
from firstapp.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

