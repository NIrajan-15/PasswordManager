import django_filters


from . models import *

class AccountFilter(django_filters.FilterSet):
    
    class Meta:
        model = Account
        fields= {
            'name':['icontains']
        }