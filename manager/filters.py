import django_filters
from django_filters import CharFilter

from . models import *

class AccountFilter(django_filters.FilterSet):
    note = CharFilter(field_name="name",lookup_expr='icontains')
    class Meta:
        model = Account
        fields=['name']