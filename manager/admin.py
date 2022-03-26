from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

# A class for User configuration in admin panel
# Fields required to add admin
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


# A class for any Updates on account's information
# the list_display represents all the fileds on admin panel
class UpdateHistoryAdmin(admin.ModelAdmin):
    list_display=('email','updated_column','updated_on','updated_to')
    list_filter = ('updated_on',)

# Registering models on Admin Panel so that they can be modeified via admin panel too
admin.site.register(User,UserAdminConfig)
admin.site.register(Account)
admin.site.register(UpdateHistory,UpdateHistoryAdmin)

admin.site.site_header = "Password Manager"
admin.site.site_title = "Password Manager Admin Portal"
admin.site.index_title = "Welcome to Password Manager Admin Portal"