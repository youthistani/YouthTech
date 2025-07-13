from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password1')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].name = 'username'
        self.fields['password'].label = ''
        self.fields['password'].name = 'password'
        self.fields['username'].help_text = '<span class="form-text text-muted">Required. 100 character or fewer. latters, digits, @/./+/-/-/_ only</span>'

        self.fields['password'].help_text = '<span class="form-text text-muted">Required. 8 character or fewer. latters, digits, @/./+/-/-/_ only</span>'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'example@gmail.com'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].widget.attrs['label'] = ''
        self.fields['username'].help_text = '<span class="form-text">Required. 100 character or fewer. latters, digits, @/./+/-/-/_ only</span>'  

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].widget.attrs['label'] = ''
        self.fields['password1'].help_text = "<span class='form-text text-muted'>password can't be too similar to your personal information</br>password must contain 8 characters.</br>password can't be a commonly used password.</br>password can\'t be entirely numeric</span>"

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['label'] = ''
        self.fields['password2'].help_text = '<span class="form-text text-priamry">Enter the same password as before, for verification</span>'