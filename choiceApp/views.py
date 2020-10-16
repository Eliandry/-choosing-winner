from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.views.generic import ListView
from .models import *
from django.contrib import auth


class TestList(ListView):
    model = Test


def createTest(request):
    form = AddAvatar()
    if request.method == "POST":
        form = AddAvatar(request.POST, request.FILES)
        if form.is_valid():
            model_test = form.save(commit=False)
            model_test.name = request.POST.get('name')
            model_test.author = auth.get_user(request).username
            model_test.save()
            model = Test.objects.get(name=request.POST.get('name'))
            return redirect(f'/createTest/{model_test.id}')
    return render(request, 'choiceApp/createTest.html', {'form': form, 'user': auth.get_user(request)})


def addPhoto(request, pk):
    form = AddPhoto()


    if request.method == "POST":
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            test=Test.objects.get(id=pk)
            test.photo.add(form)
            if test.photo.count()<11:
                return HttpResponseRedirect(f'createTest/{pk}',{'error':'Недостаточно картинок'})
            return HttpResponseRedirect('/')
    return render(request, 'choiceApp/addPhoto.html', {'form': form, 'user': auth.get_user(request)})