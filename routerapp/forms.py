from django.forms import ModelForm
from .models import Contohmodel, Routerm, Manualcommand
from django import forms


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
            'kecepatan_internet': forms.TextInput({'class': 'form-control', 'placeholder': 'dalam kilobyte'}),
        }


class Manualform(ModelForm):

    class Meta:
        model = Manualcommand
        fields = ['host', 'command']
        widgets = {
            'host': forms.Select({'class': 'form-control'}),
            'command': forms.TextInput({'class': 'form-control'})
        }

class auto2Form(forms.Form):
    kecepatan = forms.CharField(widget=forms.TextInput({'class':'form-control', 'placeholder': 'dalam kilobyte / boleh juga kosongkan'}),label="kecepatan minimum",max_length=50, required=False)
