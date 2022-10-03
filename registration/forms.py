from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requis, 254 caractères maximum et doit être valide.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà enregistré, veuillez essayer un autre.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={ 'class':'form-control mt-3', 'rows':3, 'placeholder':'Biographie'}),
            'link': forms.URLInput(attrs={ 'class':'form-control mt-3', 'placeholder':'Lien'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requis, 254 caractères maximum et doit être valide.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Cet email est déjà enregistré, veuillez essayer un autre.")
        return email
