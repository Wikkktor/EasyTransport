from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View


class Register_view(View):
    def get(self, request):
        return render(request, 'accounts/register.html')


class Login_view(View):
    def get(self, request):
        return render(request, 'accounts/login.html')


class Logout_view(View):
    def get(self, request):
        user = request.user.is_authenticated
        if user:
            logout(request)
            return redirect("main_page")
        else:
            return redirect("main_page")
