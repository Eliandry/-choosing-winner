from django.urls import path
from .views import *
urlpatterns = [
    path('',TestList.as_view()),
    path('createTest/',CreateTest.as_view(),name='createTest'),
    path('createTest/<int:pk>',AddPhoto.as_view(),name='addPhoto'),
    path('createSession/<int:pk>/',addSession),
    path('start/test/',ChoicePhoto.as_view(),name='choice'),
    path('delete/<int:pk>/',deletePhoto,name='delete')
]
