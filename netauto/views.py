from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Contohmodel, Routerm, Automation
from .forms import Formcontoh, RoutermForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import sendcom
import json
import routeros_api



# Create your views here.
@login_required(login_url=settings.LOGIN_URL) 
def show_ip(request):

    data=sendcom.show_ip("192.168.31.1","admin","")
    return render(request, "home.html", { 'data': data })
    pass

@login_required(login_url=settings.LOGIN_URL) 
def homepage(request):
    auto = Automation.objects.all()
    router=Routerm.objects.all()
    context = {
        'auto': auto,
        'router': router
    }
    return render(request, "home.html", context)
    pass

@login_required(login_url=settings.LOGIN_URL) 
def addcontoh(request):
    contoh = Contohmodel.objects.all()
    fromcontoh = Formcontoh
    context= {
        'formk' : fromcontoh,
        'k': contoh,
    }
    return render(request, 'addcontoh.html', context)
    pass

@login_required(login_url=settings.LOGIN_URL) 
def addrouter(request):
    router=Routerm.objects.all()
    form = RoutermForm
    context = {
        'formk' : form,
        'router': router
    }
    return render(request, "addrouter.html", context)
    pass

@login_required(login_url=settings.LOGIN_URL) 
def addr(request):
    if request.method == 'POST':
        form = RoutermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "berhasil bosku")
            return redirect(addrouter)

    pass

@login_required(login_url=settings.LOGIN_URL) 
def router(request, id):
    router=Routerm.objects.all()
    idk=id
    data=Routerm.objects.filter(pk=id)
    context = {
        'data' : data,
        'router': router,
        'idk':idk
    }
    return render(request,'detailrouter.html',context)
    pass

@login_required(login_url=settings.LOGIN_URL) 
def apiip(request):
    host = "192.168.31.1"

    conn = routeros_api.RouterOsApiPool(host, username="admin", password="", plaintext_login=True)
    api= conn.get_api()

    list_ip = api.get_resource('ip/address')
    show_ip = list_ip.get()

    data = json.dumps(show_ip, indent=3)
    conn.disconnect()
    d=json.loads(data)
    context={
        'data':d,
    }
    return render(request,'coba.html',context)