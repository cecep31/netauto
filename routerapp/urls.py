from django.contrib.auth.views import LoginView,LogoutView
from django.forms import widgets
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path('command',views.manualcommand, name='manual'),
    path('<int:id>/router',views.detailrouter, name='router'),
    path('<int:id>/pcq1',views.pcq1, name='conpcq1'),
    path('', views.homepage, name='show'),
    path('addrouter',views.addrouter, name='addrouter'),
    path('beta/',views.apiip, name='beta'),
    path('login',views.loginya, name='login'),
    path('logout',LogoutView.as_view(next_page='login'), name='logout'),
    path('auto/<int:router>/<int:id>',views.autosettingview1, name='autosetting1'),
    path('delrouter/<int:idr>',views.delrouter,name='delrouter'),
    path('updaterouter/<int:idr>',views.updaterouter,name='uprouter'),
    path('commandajax',views.manualcommandajax, name='manualajax'),
    
]