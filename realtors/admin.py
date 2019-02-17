from django.contrib import admin
from .models import Realtor

class RealtorsModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'hire_date')
    list_display_links = ('id', 'name')

admin.site.register(Realtor, RealtorsModel)
