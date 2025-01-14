from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("fuck", views.fuck, name="fuck")
]