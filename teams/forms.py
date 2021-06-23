from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Equipo,Estadio,Extra,Comment

class CustomUserCreationForm(UserCreationForm):
    telefono = forms.IntegerField(label = "telefono")
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2","telefono",]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','value':'-'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }