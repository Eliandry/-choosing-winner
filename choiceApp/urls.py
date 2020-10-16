from django.urls import path
from .views import *
urlpatterns = [
    path('',TestList.as_view()),
    path('createTest/',createTest,name='createTest'),
    path('createTest/<int:pk>',addPhoto,name='addPhoto')
]
