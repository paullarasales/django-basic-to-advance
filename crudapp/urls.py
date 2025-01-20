from django.urls import path
from . import views

app_name = "crudapp"
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:id>/edit/', views.product_edit, name='product_edit'),
    path('<int:id>/delete/', views.product_delete, name="product_delete")
]