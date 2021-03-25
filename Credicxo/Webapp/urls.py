from django.urls import path
from Webapp import views
from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('fpassword', views.fpassword, name='fpassword'),
    path('signup1', views.Signuplist.as_view()),
]
