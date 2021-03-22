from django.contrib.auth.views import LoginView,LogoutView
from django.forms import widgets
from django.urls import path
from . import views

urlpatterns = [
    path('command',views.manualcommand, name='manual'),
    path('<int:id>/router',views.router, name='router'),
    path('<int:id>/pcq1',views.pcq1, name='conpcq1'),
    path('', views.homepage, name='show'),
    path('addrouter',views.addrouter, name='addrouter'),
    path('addr', views.addr, name='addr'),
    path('addc/', views.addcontoh, name='addcontoh'),
    path('beta/',views.apiip, name='beta'),
    path('login',LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(next_page='login'), name='logout'),
    path('auto/:router/:id',views.pcq2, name='pcq2'),
    
]