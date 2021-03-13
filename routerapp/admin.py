from django.contrib import admin

# Register your models here.

from .models import Contohmodel, Routerm, Automation

# Register your models here.
class Contohadmin(admin.ModelAdmin):
    list_display = ['nama','pub_date']
    search_fields = ['nama']
    list_per_page = 4

admin.site.register(Contohmodel, Contohadmin )

admin.site.register(Routerm)

admin.site.register(Automation)