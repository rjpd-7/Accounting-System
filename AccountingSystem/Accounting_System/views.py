from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

#Landing Page / Dashboard
def index(request):
    return render(request, "Front_End/index.html")

def journals(request):
    return render(request, "Front_End/journal.html")
