from django.db import models
from datetime import date

# Create your models here.
class JournalEntry(models.Model):
    date = models.DateField(default=date.today())
    description = models.TextField(max_length=None, null=True)
    account_name = models.TextField(max_length=None, null=True)
    debit = models.DecimalField(decimal_places=10, max_digits=19, default=0)
    credit = models.DecimalField(decimal_places=10, max_digits=19, default=0)

    class Meta:
        db_table = "sample"
