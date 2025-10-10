from django.urls import path
from . import views

# name of the Django app.
app_name = "AccountingSystem"

# URL configuration for Accounting_System.
urlpatterns = [
    path("", views.login_view, name="login"),
    path("journal/", views.journals, name="journals"),
    path("insert_journals/", views.insert_journals, name="insert_journals"),
    path("edit_journal/", views.edit_journal, name="edit_journal"),
    path("accounts/", views.chart_of_accounts, name="accounts"),
    path("create_account/", views.create_account, name="create_account"),
    path("files/", views.files, name="files"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("index/", views.index, name="index"),
    path("balance/", views.trial_balance, name="balance"),
]