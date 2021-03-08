from django import forms
from projects.models import UserCredentials, Projects


class CredentialsForm(forms.ModelForm):

    class Meta:
        model = UserCredentials
        fields = '__all__'
        widgets = {
            'authentication_type': forms.RadioSelect(),
            'end_point': forms.TextInput(attrs={"class": "form-control"}),
            'service': forms.Select(attrs={"class": "form-control"}),
            'token': forms.TextInput(attrs={"class": "form-control"}),
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'password': forms.TextInput(attrs={"class": "form-control", "type": "password"}),
        }
