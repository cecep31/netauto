from django.shortcuts import render
from .models import Contohmodel
from .forms import Formcontoh
from . import sendcom

# Create your views here.
def show(request):
    data=sendcom.show_ip("192.168.31.1","admin","")
    return render(request, "home.html", { 'data': data })
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