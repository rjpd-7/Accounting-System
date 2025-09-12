from django.urls import path
from . import views

# name of the Django app.

# URL configuration for Accounting_System.
urlpatterns = [
    path("", views.index, name="index"),
]