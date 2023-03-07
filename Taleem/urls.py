"""Taleem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path, include

from Taleem import settings
from User.views import SignupCreateView, ApplicationCreateView, ProfileUpdateView
from books.views import BookListView
from common_functions.BaseView import BaseView
def hoc(num):
  def error(request,exception=None):
    context = {}
    print(f'/errors/{num}_page.html',"Profile\profile.html")
    return render(request,f'{num}_page.html', context)
  return error


urlpatterns = [
  path("", BaseView.as_view(template_name="Landing.html"),name="Landing"),
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  path("accounts/profile/", BaseView.as_view(template_name="registration/profile.html"),name="profile"),
  path("accounts/profile-Update/<int:pk>", ProfileUpdateView.as_view(),name="profile_update"),
  path("accounts/Signup/", SignupCreateView.as_view(),name="SignupCreateView"),
  path("accounts/ApplicationCreation/", ApplicationCreateView.as_view(),name="ApplicationCreateView"),
  path('Feed/', include('Questions.urls')),
  path('book/',  BookListView.as_view(),name="book"),
  path('reward/', include('Reward.urls')),
  path('404/',hoc(404),name="404_page"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404=hoc(404)
