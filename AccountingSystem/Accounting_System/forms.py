from django import forms
from .models import JournalEntry

class UpdateJournalForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['date', 'description', 'account_name_1', 'debit_1', 'credit_1', 'account_name_2', 'debit_2', 'credit_2']
