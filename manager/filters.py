import django_filters


from . models import *

# Django-filter to filter those accounts whose name contains the string that is searched
class AccountFilter(django_filters.FilterSet):
    
    class Meta:
        model = Account
        fields= {
            'name':['icontains']
        }