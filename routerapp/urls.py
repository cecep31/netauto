from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('command',views.manualcommand, name='manual'),
    path('<int:id>/router',views.detailrouter, name='router'),
    path('<int:id>/autoconfig1',views.auto1, name='urlauto1'),
    path('<int:id>/autoconfig2',views.auto2, name='urlauto2'),
    path('', views.homepage, name='show'),
    path('addrouter',views.addrouter, name='addrouter'),
    path('login',views.loginya, name='login'),
    path('logout',LogoutView.as_view(next_page='login'), name='logout'),
    path('auto/<int:router>/<int:id>',views.autosettingview1, name='autosetting1'),
    path('delrouter/<int:idr>',views.delrouter,name='delrouter'),
    path('updaterouter/<int:idr>',views.updaterouter,name='uprouter'),
    path('commandajax',views.manualcommandajax, name='manualajax'),
    path('delauto1/<int:id>',views.delauto1, name='delauto1url'),
    path('delauto2/<int:id>',views.delauto2, name='delauto2url'),
    path('configlog',views.configlog, name='configlogurl')
    
]