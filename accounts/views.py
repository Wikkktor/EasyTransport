from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from .validators import register_validator
from django.contrib.auth.models import User
from TransportApp.models import Account
from .geolocation import get_location_lat_long


class Register_view(View):
    def get(self, request):
        user = request.user.is_authenticated
        if user:
            return redirect("main_page")
        return render(request, 'accounts/register.html')

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        address = request.POST.get("address")
        if register_validator(request, email, password, password2):
            user = User(username=email, email=email)
            user.set_password(password)
            user.save()
            try:
                geolocation = get_location_lat_long(address)
            except IndexError:
                messages.add_message(request, messages.ERROR, 'Nie możemy znaleźc adresu Twojej firmy')
                return redirect('register')
            account = Account(user=user, location=address, lat=geolocation[0], long=geolocation[1])
            account.save()
            return redirect('main_page')
        return redirect('register')


class Login_view(View):
    def get(self, request):
        user = request.user.is_authenticated
        if user:
            return redirect("main_page")
        return render(request, 'accounts/login.html')


class Logout_view(View):
    def get(self, request):
        user = request.user.is_authenticated
        if user:
            logout(request)
            return redirect("main_page")
        else:
            return redirect("main_page")
