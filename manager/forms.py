from django import forms
from .models import Account

# account addd form
class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields= '__all__'

class SearchForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['name']