from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    send_copy = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-control1', 'placeholder': 'Get message copy'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'title', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Message'}),
        }