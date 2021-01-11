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
            'nama' : forms.TextInput({'class':'form-control'}),
            'host' : forms.TextInput({'class':'form-control'}),
            'user' : forms.TextInput({'class':'form-control'}),
            'password' : forms.TextInput({'class':'form-control'}),
        }
