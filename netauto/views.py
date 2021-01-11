from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contohmodel, Routerm
from .forms import Formcontoh, RoutermForm
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

def addrouter(request):
    router=Routerm.objects.all()
    form = RoutermForm
    context = {
        'formk' : form,
        'router': router
    }
    return render(request, "addrouter.html", context)
    pass

def addr(request):
    if request.method == 'POST':
        form = RoutermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "berhasil bosku")
            return redirect(addrouter)

    pass

def router(request, id):
    router=Routerm.objects.all()
    data=Routerm.objects.filter(pk=id)
    context = {
        'data' : data,
        'router': router
    }
    return render(request,'detailrouter.html',context)
    pass