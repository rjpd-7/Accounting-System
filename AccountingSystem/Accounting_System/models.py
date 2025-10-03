from django.db import models
from datetime import date

# Create your models here.
class JournalEntry(models.Model):
    date = models.DateField(default=date.today)
    description = models.TextField(max_length=None, null=True)
    account_name_1 = models.TextField(max_length=None, null=True)
    debit_1 = models.DecimalField(max_digits=18, decimal_places=9, blank=True)
    credit_1 = models.DecimalField(max_digits=18, decimal_places=9, blank=True)
    account_name_2 = models.TextField(max_length=None, null=True)
    debit_2 = models.DecimalField(max_digits=18, decimal_places=9, blank=True)
    credit_2 = models.DecimalField(max_digits=18, decimal_places=9, blank=True)

    class Meta:
        db_table = "sample"

class Accounts(models.Model):
    account_code = models.BigIntegerField(primary_key=True)
    account_name = models.TextField(max_length=None, null=True)
    account_type = models.TextField(max_length=None, null=True)

    class Meta:
        db_table = "sample_accounts"

class USN_Accounts(models.Model):
    usn = models.TextField(max_length=None, null=True)
    password = models.TextField(max_length=None, null=True)

    class Meta:
        db_table = "sample_usn_accounts"
