from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contohmodel, Routerm, Automation
from .forms import Formcontoh, RoutermForm, auto2Form, LoginForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import sendcom
import json
import routeros_api
from django.urls import reverse
from django.contrib.auth import authenticate, login


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def show_ip(request):

    data = sendcom.show_ip("192.168.31.1", "admin", "")
    return render(request, "home.html", {'data': data})


@login_required(login_url=settings.LOGIN_URL)
def homepage(request):
    auto1 = Automation.objects.filter(autokey="auto1")
    auto2 = Automation.objects.filter(autokey="auto2")
    routerside = Routerm.objects.all()
    auto2form=auto2Form
    router = Routerm.objects.all()[:1]
    context = {
        'auto1': auto1,
        'auto2': auto2,
        'router':router,
        'routerside': routerside,
        'auto2form':auto2form
    }
    return render(request, "home.html", context)


@login_required(login_url=settings.LOGIN_URL)
def addcontoh(request):
    contoh = Contohmodel.objects.all()
    fromcontoh = Formcontoh
    context = {
        'formk': fromcontoh,
        'k': contoh,
    }
    return render(request, 'addcontoh.html', context)


@login_required(login_url=settings.LOGIN_URL)
def addrouter(request):
    if request.method == 'POST':
        form = RoutermForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, "berhasil menambahkan " + form['nama'].value())
            return redirect('addrouter')
            # return HttpResponseRedirect(reverse("addrouter"))
    else:
        routerside = Routerm.objects.all()
        form = RoutermForm
        context = {
            'form': form,
            'routerside': routerside
        }
        return render(request, "addrouter.html", context)

@login_required(login_url=settings.LOGIN_URL)
def updaterouter(request, idr):
    router = Routerm.objects.get(id=idr)
    if request.method == 'POST':
        form = RoutermForm(request.POST, instance=router)
        if form.is_valid():
            form.save()
            messages.success(request,"berhasil mengubah router")
            return redirect('router', idr)
    else:
        form = RoutermForm(instance=router)
        routerside = Routerm.objects.all()
        context = {
            'idk' : idr,
            'form' : form,
            'routerside': routerside
        }
        return render(request, 'uprouter.html', context)

@login_required(login_url=settings.LOGIN_URL)
def delrouter(request, idr):
    router = Routerm.objects.filter(id=idr)
    for ro in router:
        namar = ro.nama
        
    router.delete()

    messages.success(
                request, "Berhasil menghapus router" + namar)
    return HttpResponseRedirect(reverse("show"))


@login_required(login_url=settings.LOGIN_URL)
def detailrouter(request, id):
    auto1 = Automation.objects.filter(autokey="auto1")
    auto2 = Automation.objects.filter(autokey="auto2")
    routerside = Routerm.objects.all()
    idk = id
    router = Routerm.objects.filter(pk=id)
    auto2form=auto2Form
    context = {
        'auto1': auto1,
        'auto2': auto2,
        'router': router,
        'routerside': routerside,
        'idk': idk,
        'auto2form':auto2form
    }
    return render(request, 'detailrouter.html', context)


@login_required(login_url=settings.LOGIN_URL)
def apiip(request):
    host = "192.168.31.1"

    conn = routeros_api.RouterOsApiPool(
        host, username="admin", password="", plaintext_login=True)
    api = conn.get_api()

    list_ip = api.get_resource('ip/address')
    show_ip = list_ip.get()

    data = json.dumps(show_ip, indent=3)
    conn.disconnect()
    d = json.loads(data)
    context = {
        'data': d,
    }
    return render(request, 'coba.html', context)


@login_required(login_url=settings.LOGIN_URL)
def pcq1(request, id):

    for i in Routerm.objects.filter(id=id):
        user = i.user
        passw = i.password
        host = i.host
        speed = i.kecepatan_internet

    send = sendcom.Remote(host, user, passw, speed)
    v = send.pcq1()

    # send = sendcom.Remote(host, user, passw, speed)
    # v=send.scanip()
    messages.success(request, v)
    return redirect('show')
    # return HttpResponseRedirect(reverse('show'))


@login_required(login_url=settings.LOGIN_URL)
def pcq2(request, id):

    for i in Routerm.objects.filter(id=id):
        user = i.user
        passw = i.password
        host = i.host
        speed = i.kecepatan_internet

    HttpResponseRedirect(reverse())

    send = sendcom.Remote(host, user, passw, speed)
    v = send.pcq2()

    # send = sendcom.Remote(host, user, passw, speed)
    # v=send.scanip()

    context = {
        'data': v,
    }

    return render(request, 'pcq2.html', context)


@login_required(login_url=settings.LOGIN_URL)
def autosettingview1(request, router, id):
    from .forms import Manualform
    f = Manualform

    context = {
        'data': f,
    }

    return render(request, 'autosettingview.html', context)



@login_required(login_url=settings.LOGIN_URL)
def manualcommand(request):
    from .forms import Manualform
    routerside = Routerm.objects.all()
    if request.method == "POST":
        form = Manualform(request.POST)
        if form.is_valid():
            form.save()
            redirect('manual')

    context = {
        'form': Manualform,
        'routerside': routerside
    }
    return render(request, 'manualc.html', context)

@login_required(login_url=settings.LOGIN_URL)
def manualcommandajax(request):
    from .forms import Manualform
    if request.method == "POST":
        form = Manualform(request.POST)
        if form.is_valid():
                id = request.POST['host']
                command = request.POST['command']
                router = Routerm.objects.filter(id=id)
                for i in router:
                    user = i.user
                    passw = i.password
                    host = i.host
                    speed = i.kecepatan_internet
                comen=sendcom.Remote(host,user,passw,speed)
                outnya=comen.command(command)

                return JsonResponse(data={"data": host}, status=200)

def loginya(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('show')
        else:
            # Return an 'invalid login' error message.
            ...
            return redirect('login')
    else:

        context = {
            'form' : LoginForm,
        }
        return render(request, 'registration/login.html', context)