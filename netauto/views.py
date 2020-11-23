from django.shortcuts import render
from .models import Contohmodel
from .forms import Formcontoh

# Create your views here.
def show(request):
    return render(request, "home.html")
    pass

def addcontoh(request):
    contoh = Contohmodel.objects.all()
    fromcontoh = Formcontoh
    context= {
        'formk' : fromcontoh,
        'k': contoh,
    }
    return render(request, 'addcontoh.html', context)
    pass