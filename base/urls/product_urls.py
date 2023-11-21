from django.urls import path
from ..views import product_views as views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<int:pk>/', views.product_details, name='product-detail'),
]
