from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.views.generic import ListView
from .models import *
from django.contrib import auth


class TestList(ListView):
    model = Test


class CreateTest(View):
    def get(self, request):
        form = AddAvatar()
        return render(request, 'choiceApp/createTest.html', {'form': form, 'user': auth.get_user(request)})

    def post(self, request):
        form = AddAvatar(request.POST, request.FILES)
        model_test = form.save(commit=False)
        model_test.name = request.POST.get('name')
        model_test.author = auth.get_user(request).username
        model_test.save()
        return redirect(f'/createTest/{model_test.id}')


class AddPhoto(View):
    def get(self, request, pk):
        form = AddPhotoForm()
        test = Test.objects.get(id=pk)
        if test.photo.count() > 11:
            bool_count=True
        else:
            bool_count=False
        return render(request, 'choiceApp/addPhoto.html', {'form': form, 'user': auth.get_user(request),'count':test.photo.count(),'bool_count':bool_count})

    def post(self, request, pk):
        test = Test.objects.get(id=pk)
        for f in request.FILES.getlist('photo'):
            photo = Photo(photo=f)
            photo.save()
            test.photo.add(photo)
            test.save()
        return redirect(f'/createTest/{test.id}')

