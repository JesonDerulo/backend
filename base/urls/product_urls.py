from django.urls import path
from ..views import product_views as views

urlpatterns = [
    path('', views.product_list, name='product-list')
]
