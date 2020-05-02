from django.urls import path
from . import views

app_name = "bubble"

urlpatterns = [
    path("", views.index, name="index"),
]
