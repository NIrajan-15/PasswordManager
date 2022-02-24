from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields = ('email',)
    ordering = ('-start_date',)
    list_display = ('email','is_superuser')
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2')
        }),
        ('Permissions',{'fields':('is_staff','is_superuser')}),
    )



class UpdateHistoryAdmin(admin.ModelAdmin):
    list_display=('email','updated_column','updated_on')
    list_filter = ('updated_on',)

# Register your models here.
admin.site.register(User,UserAdminConfig)
admin.site.register(Account)
admin.site.register(UpdateHistory,UpdateHistoryAdmin)
