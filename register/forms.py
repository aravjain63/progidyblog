from django import forms
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        #print(User.objects.filter(email=email).count())
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']