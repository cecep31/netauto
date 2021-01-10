from django.shortcuts import render
from .models import Contohmodel, Routerm
from .forms import Formcontoh
from . import sendcom
import json



# Create your views here.
def show_ip(request):

    data=sendcom.show_ip("192.168.31.1","admin","")
    return render(request, "home.html", { 'data': data })
    pass

def homepage(request):
    router=Routerm.objects.all()
    context = {
        'router': router
    }
    return render(request, "home.html", context)
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