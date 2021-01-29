from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account



class StartForm(forms.ModelForm):
    # email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address")
    class Meta:
        model = Account
        fields = ('email', 'phone')
        # 'first_name', 'last_name',

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        print('this is the email address')
        print(email)
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"{email} is taken.")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            account = Account.objects.get(phone=phone)
        except Exception as e:
            return phone
        raise forms.ValidationError(f"{phone} is already used.")


class NameForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name:
            return first_name
        raise forms.ValidationError(f"Enter a valid name")

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name:
            return last_name
        raise forms.ValidationError(f"Enter a valid name")
