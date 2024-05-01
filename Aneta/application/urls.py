from django.urls import path

from . import views

urlpatterns = [
    path("", views.applicant_list_create_view, name="index"),
]