from django.forms import ModelForm
from .models import Contohmodel, Routerm
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
            'nama' : forms.TextInput({'class':'form-control','placeholder':'masukan nama untuk router'}),
            'host' : forms.TextInput({'class':'form-control','placeholder':'alamat host router | contoh: 192.168.1.1'}),
            'user' : forms.TextInput({'class':'form-control','placeholder':'masukan username router'}),
            'password' : forms.TextInput({'class':'form-control','placeholder':'masukan pasword router'}),
            'kecepatan_internet' : forms.TextInput({'class':'form-control','placeholder':'dalam kilobyte'}),
        }
