from django.contrib import admin
from .models import Contohmodel, Routerm, Automation, Automationon

# Register your models here.
@admin.register(Contohmodel)
class Contohadmin(admin.ModelAdmin):
    list_display = ['nama','pub_date']
    search_fields = ['nama']
    list_per_page = 4


@admin.register(Automationon)
class AutomationonAdmin(admin.ModelAdmin):
    list_display= ('auto','router', 'create_at')
    list_per_page = 10
    



admin.site.register(Routerm)

admin.site.register(Automation)
