from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Signup
from .serializers import Signupserializers

class Signuplist(APIView):
    def get(self, request):
        signup1 = Signup.objects.all()
        serializer = Signupserializers(signup1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

from Webapp.models import Signup


# Create your views here.


def index(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        password1 = request.POST['password']
        from django.contrib import auth
        x = auth.authenticate(username=email1, password=password1)
        if x is None:
            return redirect('login')
        else:
            return redirect('signup')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        x = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=password)
        x.save()
        signups = Signup(fname=fname, lname=lname, email=email, password=password)
        signups.save()
    return render(request, "signup.html")


def fpassword(request):
    if request.method == 'POST':
        y = PasswordChangeForm(user=request.email, data=request.POST)
        if y.is_valid():
            y.save()
            return render('login')
    else:
        PasswordChangeForm(user=request.email)
    return render(request, 'fpassword.html')
