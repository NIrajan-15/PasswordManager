from django.contrib import admin
from .models import *
from .forms import *

class AddAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'password']
    form = AccountForm
    search_fields = ['name']

class UpdateHistoryAdmin(admin.ModelAdmin):
    list_display=('name','updated_column','updated_on')
    list_filter = ('updated_on',)

# Register your models here.
admin.site.register(Account,AddAccountAdmin)
admin.site.register(UpdateHistory,UpdateHistoryAdmin)