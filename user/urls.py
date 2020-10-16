from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',register,name='account_signup'),
    path('signin/',logins,name='account_login'),
    path('logout/',LogoutFormView.as_view(),name='account_logout'),
]
