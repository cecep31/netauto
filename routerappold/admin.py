from django.contrib import admin
from .models import Contohmodel, Manualcommand, Routerm, Automation, Automationon

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
    

@admin.register(Automation)
class AutomationAdmin(admin.ModelAdmin):
    list_display= ('autokey', 'nama')

@admin.register(Manualcommand)
class manualAdmin(admin.ModelAdmin):
    list_display= ['host']

admin.site.register(Routerm)

