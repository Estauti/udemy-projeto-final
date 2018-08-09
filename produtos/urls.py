from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.products_list, name='products_list'),
    path('produtos/cadastro/', views.products_new, name='products_new'),
    path('produtos/delete/<int:id>/', views.products_delete, name='products_delete'),        
    path('produtos/edit/<int:id>/', views.products_edit, name='products_edit'),
]