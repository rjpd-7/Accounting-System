from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import JournalEntry, Accounts, USN_Accounts
from django.contrib.auth import authenticate, login, logout
from .forms import UpdateJournalForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages 

# Create your views here.

# Landing Page / Dashboard
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("AccountingSystem:login"))
    return render(request, "Front_End/index.html")

# Login Page
def login_view(request):
    if request.method == "POST":
        usn = request.POST["usn"]
        password = request.POST["password"]
        user = authenticate(request, username=usn, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("AccountingSystem:index"))
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("AccountingSystem:login")

    return render(request, "Front_End/login.html")

def logout_view(request):
    
    return render(request, "Front_End/login.html")

# Journal Entries Page
def journals(request):
    accounts = Accounts.objects.all()
    journals = JournalEntry.objects.all()
    return render(request, "Front_End/journal.html", {
        "journals" : journals, 
        "accounts": accounts
    })

# Journal Entry Modal Submit
def insert_journals(request):
    j_entry_date = request.POST['entry_date']
    j_description = request.POST['description']
    j_account_name_1 = request.POST['account_name_1']
    j_debit_1 = request.POST['debit']
    j_account_name_2 = request.POST['account_name_2']
    j_credit_2 = request.POST['credit']
    journal = JournalEntry(date = j_entry_date, description = j_description, account_name_1 = j_account_name_1, debit = j_debit_1, account_name_2 = j_account_name_2, credit = j_credit_2)
    journal.save()

    return HttpResponseRedirect(reverse("AccountingSystem:journals"))

# Edit Journal Modal Submit
def edit_journal(request, id):
    # Passing values onto Edit Journal Modal
    
    journal =JournalEntry.objects.get(pk = id)

    if request.method == 'POST':
        form = UpdateJournalForm(request.POST, instance = journal)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("AccountingSystem:journals"))
    
    else:
        pass

    return HttpResponseRedirect(reverse("AccountingSystem:journals"))


# Accounts Page
def chart_of_accounts(request):
    results = Accounts.objects.all()
    return render(request, "Front_End/accounts.html", {
        "accounts" : results
    })

# Create Account Modal Submit
def create_account(request):
    account_code_submit = request.POST['account_code']
    account_name_submit = request.POST['account_name']
    account_type_submit = request.POST['account_type']
    account = Accounts(account_code = account_code_submit, account_name = account_name_submit, account_type = account_type_submit)
    account.save()

    return HttpResponseRedirect(reverse("AccountingSystem:accounts"))

# Balance Page
def trial_balance(request):
    balances = JournalEntry.objects.all()
    accounts = Accounts.objects.all()
    return render(request, "Front_End/balance.html", {
        "balances": balances,
        "accounts": accounts,
    })

# Files Page
def files(request):
    return render(request, "Front_End/files.html")
