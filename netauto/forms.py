from django.forms import ModelForm
from .models import Contohmodel

class Formcontoh(ModelForm):
    
    class Meta:
        model = Contohmodel
        fields = '__all__'
