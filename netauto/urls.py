
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='show'),

    path('addc/', views.addcontoh, name='addcontoh'),
    
]