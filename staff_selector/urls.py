from django.urls import path
from . import views

urlpatterns = [
    path("hasil/", views.hasil_wp, name="hasil_wp"),
]
