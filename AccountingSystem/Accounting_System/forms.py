from django import forms
from .models import JournalEntry

class UpdateJournalForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = '__all__'