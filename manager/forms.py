from django import forms
from .models import Account

# From to add accounts to the database
class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields= '__all__'

# Form to take input to search for account
class SearchForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['name']