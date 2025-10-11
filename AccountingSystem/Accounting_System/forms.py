from django import forms
from .models import JournalEntry, USN_Accounts

class UpdateJournalForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = '__all__'

class InsertJournalForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = USN_Accounts
        fields = '__all__'