import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .geocode import get_location_lat_long, get_distance_time_values
from .models import Order, Transport, Car, Driver

today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)


class MainPage(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        not_done_orders = Order.objects.filter(user_id=user, status__lt=3)
        today_orders = Order.objects.filter(user_id=user, delivery_time__range=(today_min, today_max))
        return render(request, "main_page.html",
                      {'orders': not_done_orders, 'today': today_orders})


class Add_order(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "add_order.html")

    def post(self, request):
        user = request.user
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        address = request.POST.get('address')
        post_code = request.POST.get('post_code')
        delivery_dt = request.POST.get("deliverydate")
        info = request.POST.get('more_info')
        if not f_name or not l_name or not phone or not city or not address:
            messages.add_message(request, messages.INFO, "Nie prawidłowe dane")
            return redirect('add_order')
        location = f"{address}, {post_code} {city}" if post_code else f"{address}, {city}"
        geocode = get_location_lat_long(location)
        # time_dist = get_distance_time_values(location, ) # TODO: Origin place dodac
        if not geocode:
            messages.add_message(request, messages.INFO,
                                 "Niestety nie możemy przekonwertować tego adresu, spróbuj dodać więcej danych")
            return redirect('add_order')
        order = Order.objects.create(user_id=user.id, client_name=f_name, client_surname=l_name, phone_number=phone,
                                     delivery_address=location, delivery_time=delivery_dt, opis=info, lat=geocode[0],
                                     lon=geocode[1])
        order.save()
        return redirect('main_page')


class Orders_view(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        orders = Order.objects.filter(user_id=user).order_by('delivery_time')
        return render(request, 'orders_list.html', {'orders': orders})


class Analysis(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        orders = Order.objects.filter(user_id=user)
        # TODO: wykres na podstawie zamówień, łączna ilość km ile przejechał etc
        return render(request, 'analysis.html', {'orders': orders})


class Settings(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        return render(request, 'settings.html')


class Contact(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        return render(request, 'help.html')
