"""choiceProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('choiceApp.urls')),
    path('auth/',include('user.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
urlpatterns+=[
    path('pass-reset/',authViews.PasswordResetView.as_view(template_name='pass_reset.html'),
         name='pass-reset'),

    path('password_reset_confirm/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset_complete/',authViews.PasswordResetCompleteView.as_view(template_name='password-reset_complete.html'),
         name='password-reset_complete'),

    path('password-reset/done/',authViews.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

]

