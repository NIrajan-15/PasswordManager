from django.shortcuts import redirect, render
from . import models
from . import forms
from .models import *
from .forms import *

# Create your views here.
def frontpage(request):

    
        accounts = Account.objects.all()
        context = {
            'accounts' : accounts,
        }
        return render(request,'manager/frontpage.html',context)


def account_info(request, key):
    
        account = Account.objects.get(id=key)
        context = {
            'key' : key,
            'account' : account,
        }

        return render(request, 'manager/account_info.html',context)
    

def addAccount(request):

    form = AccountForm()

    if request.method == 'POST':

        form = AccountForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form,
        'title' : "Add Account"
    }
    return render(request, 'manager/addAccount.html', context)

def UpdateAccount(request, key):
    
    account = Account.objects.get(id=key)

    form = AccountForm(instance=account)
    if request.method == 'POST':

        form = AccountForm(request.POST, instance=account)

        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form' : form,
        'key' : key
    }

    return render(request,'manager/update_page.html',context)

def DeleteAccount(request, key):

    account = Account.objects.get(id=key)

    if request.method=='POST':
        account.delete()
        return redirect('/')
    context = {
        'account' : account
    }

    return render(request,'manager/delete_page.html', context)