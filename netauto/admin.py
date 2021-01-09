from django.contrib import admin
from .models import Contohmodel, Routerm

# Register your models here.
class Contohadmin(admin.ModelAdmin):
    list_display = ['nama','pub_date']
    search_fields = ['nama']
    list_per_page = 4

admin.site.register(Contohmodel, Contohadmin)

admin.site.register(Routerm)