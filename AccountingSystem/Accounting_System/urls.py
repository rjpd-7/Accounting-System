from django.urls import path
from . import views

# name of the Django app.
app_name = "AccountingSystem"

# URL configuration for Accounting_System.
urlpatterns = [
    path("", views.index, name="index"),
    path("journal/", views.journals, name="journals"),
    path("insert_journals/", views.insert_journals, name="insert_journals"),
    path("accounts/", views.chart_of_accounts, name="accounts")
]