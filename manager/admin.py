from django.contrib import admin
from .models import *
from .forms import *

class AddAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'password']
    form = AccountForm
    search_fields = ['name']

# Register your models here.
admin.site.register(Account,AddAccountAdmin)