from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import JournalEntry, Accounts, USN_Accounts
from django.contrib.auth import authenticate, login, logout
from .forms import UpdateJournalForm

# Create your views here.

# Landing Page / Dashboard
def index(request):
    return render(request, "Front_End/index.html")

# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST["usn"]
        password = request.POST["password"]
        user = authenticate(request, usn=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("AccountingSystem:index"))
        else:
            return render(request, "Front_End/login.html", {
                "message": "Invalid credentials."
            })

    return render(request, "Front_End/login.html")

def logout_view(request):
    
    return render(request, "Front_End/login.html")

# Journal Entries Page
def journals(request):
    accounts = Accounts.objects.all()
    results = JournalEntry.objects.all()
    return render(request, "Front_End/journal.html", {
        "journals" : results, 
        "accounts": accounts
    })

# Journal Entry Modal Submit
def insert_journals(request):
    j_entry_date = request.POST['entry_date']
    j_description = request.POST['description']
    j_account_name_1 = request.POST['account_name_1']
    j_debit_1 = request.POST['debit_1']
    j_credit_1 = request.POST['credit_1']
    j_account_name_2 = request.POST['account_name_2']
    j_debit_2 = request.POST['debit_2']
    j_credit_2 = request.POST['credit_2']
    journal = JournalEntry(date = j_entry_date, description = j_description, account_name_1 = j_account_name_1, debit_1 = j_debit_1, credit_1 = j_credit_1, account_name_2 = j_account_name_2, debit_2 = j_debit_2, credit_2 = j_credit_2)
    journal.save()

    return HttpResponseRedirect(reverse("AccountingSystem:journals"))

# Edit Journal Modal Submit
def edit_journal(request, pk):
    # Passing values onto Edit Journal Modal
    journal =JournalEntry.objects.get(id = pk)

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
    return render(request, "Front_End/balance.html")

# Files Page
def files(request):
    return render(request, "Front_End/files.html")
