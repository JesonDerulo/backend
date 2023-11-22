from django.urls import path 
from base.views import user_views as views 


urlpatterns = [
    path('register/', views.registerUser, name='register'),
]
