from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import *

# Create your views here.

@login_required(login_url='login')
def frontpage(request):

    accounts = Account.objects.all()
    account_filter = AccountFilter(request.GET, queryset=accounts)
    accounts = account_filter.qs
    context={
        'accounts' : accounts,
        'account_filter' : account_filter
    }

    return render(request,'manager/frontpage.html',context)


@login_required(login_url='login')  
def kennedypage(request):
    accounts = Account.objects.all()
    account_filter = AccountFilter(request.GET, queryset=accounts)
    accounts = account_filter.qs
    context={
        'accounts' : accounts,
        'account_filter' : account_filter
    }
    return render(request,'manager/kennedy_account.html',context)

@login_required(login_url='login')
def neighborspage(request):
    accounts = Account.objects.all()
    account_filter = AccountFilter(request.GET, queryset=accounts)
    accounts = account_filter.qs
    context={
        'accounts' : accounts,
        'account_filter' : account_filter
    }
    return render(request,'manager/neighbor_accounts.html',context)

@login_required(login_url='login')
def account_info(request, key):
    
        account = Account.objects.get(id=key)
        context = {
            'key' : key,
            'account' : account,
        }

        return render(request, 'manager/account_info.html',context)
    
@login_required(login_url='login')
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

@login_required(login_url='login')
def UpdateAccount(request, key):
    
    account = Account.objects.get(id=key)

    form = AccountForm(instance=account)
    if request.method == 'POST':

        form = AccountForm(request.POST, instance=account)

        if form.is_valid():
            form.save()

            if form.has_changed():
                for i in form.changed_data:
                    UpdateHistory.objects.create(
                        email=request.user.email, updated_column=i)
            return redirect('/')
    context={
        'form' : form,
        
        
    }

    return render(request,'manager/update_page.html',context)

@login_required(login_url='login')
def DeleteAccount(request, key):

    account = Account.objects.get(id=key)

    if request.method=='POST':
        account.delete()
        return redirect('/')
    context = {
        'account' : account
    }

    return render(request,'manager/delete_page.html', context)

# login user
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'manager/loginpage.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')