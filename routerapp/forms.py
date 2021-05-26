from django.forms import ModelForm
from django.forms.widgets import Select, TextInput, Textarea
from .models import Contohmodel, Routerm, Configlog
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class Formcontoh(ModelForm):

    class Meta:
        model = Contohmodel
        fields = '__all__'


class RoutermForm(ModelForm):

    class Meta:
        model = Routerm
        fields = '__all__'
        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'masukan nama untuk router'}),
            'host': forms.TextInput({'class': 'form-control', 'placeholder': 'alamat host router | contoh: 192.168.1.1'}),
            'user': forms.TextInput({'class': 'form-control', 'placeholder': 'masukan username router'}),
            'password': forms.TextInput({'class': 'form-control', 'placeholder': 'masukan pasword router'}),
            'kecepatan_download': forms.TextInput({'class': 'form-control', 'placeholder': 'dalam kilobyte'}),
            'kecepatan_upload': forms.TextInput({'class': 'form-control', 'placeholder': 'dalam kilobyte'}),
        }


class Manualform(ModelForm):

    class Meta:
        model = Configlog
        fields = ['host', 'command', 'output']
        widgets = {
            'host': Select({'class': 'form-control'}),
            'command': TextInput({'class': 'form-control'}),
            'output' : Textarea(attrs={'id':'out','class': 'form-control bg-dark text-white', 'rows':"5", 'cols':"70" })
        }

class auto2Form(forms.Form):
    limitat = forms.CharField(widget=forms.TextInput({'class':'form-control', 'placeholder': 'kosong maka kecepatan maksimum router (dalam kb)'}),label="kecepatan minimum",max_length=50, required=False)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}))
    
