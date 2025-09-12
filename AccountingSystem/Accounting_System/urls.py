from django.urls import path
from . import views

# name of the Django app.
# This is used to refer to the app in templates and other parts of the Django project.
app_name = "randomNumApp"

# URL configuration for randomNumApp.
urlpatterns = [
    path("", views.index, name="index"),
]