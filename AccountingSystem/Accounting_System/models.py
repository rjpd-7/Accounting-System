from django.db import models
from datetime import date

# Create your models here.
class Accounts(models.Model):
    account_code = models.TextField(primary_key=True, max_length=None)
    account_name = models.TextField(max_length=None, null=False)
    account_type = models.TextField(max_length=None, null=False)

    class Meta:
        db_table = "sample_accounts"

class JournalEntry(models.Model):
    date = models.DateField(default=date.today)
    description = models.TextField(max_length=None, null=True)
    account_name_1 = models.TextField(max_length=None, null=True)
    debit = models.DecimalField(max_digits=18, decimal_places=9, blank=True)
    account_name_2 = models.TextField(max_length=None, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=9, blank=True)

    class Meta:
        db_table = "sample"


class USN_Accounts(models.Model):
    usn = models.TextField(max_length=None, null=True)
    password = models.TextField(max_length=None, null=True)

    class Meta:
        db_table = "sample_usn_accounts"
