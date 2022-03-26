from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import *
from .admin import *

# views


# Returns landing page after loggin in
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


# Custom Search Function return results of search in landing page
@login_required(login_url='login')
def search(request):


    accounts = Account.objects.all()

    form = SearchForm()

    if request.method == 'POST':
        name = request.POST.get('name')

        context={
            'accounts' : accounts,
            'form' : form,
            'name' : name
        }

        return render(request,'manager/frontpage.html',context)


# Returns all the accounts associated with kennedy Rice Mill
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

# Returns all the accounts associated with Neighbors cookies
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

# Returns the detail info page of the account selected
@login_required(login_url='login')
def account_info(request, key):
    
        account = Account.objects.get(id=key)
        context = {
            'key' : key,
            'account' : account,
        }

        return render(request, 'manager/account_info.html',context)
    
# Add account to the database
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

# Update account in database and track all the updates
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
                        email=request.user.email, updated_column=i, updated_to=request.POST.get(i))
            return redirect('/')
    context={
        'form' : form,
        
        
    }

    return render(request,'manager/update_page.html',context)

# Remove any account from the database
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

# Login User into the system
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

# Logout user out of system
def logoutUser(request):
    logout(request)
    return redirect('login')