from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.urls import reverse
from .models import JournalEntry

# Create your views here.

# Landing Page / Dashboard
def index(request):
    return render(request, "Front_End/index.html")

# Journal Entries Page
def journals(request):
    return render(request, "Front_End/journal.html", {
        "journals": JournalEntry.objects.all()
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

    return render(request, "Front_End/journal.html")
