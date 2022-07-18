import datetime
from django.db.models.functions import TruncMonth
from django.db.models.aggregates import Count
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .geocode import get_location_lat_long, get_distance_time_values
from .models import Order, Transport, Car, Driver, Account

today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)


class MainPage(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        account = Account.objects.get(user_id=user)
        not_done_orders = Order.objects.filter(user_id=user, status__lt=3)
        today_orders = Order.objects.filter(user_id=user, delivery_time__range=(today_min, today_max))
        return render(request, "main_page.html",
                      {'orders': not_done_orders, 'today': today_orders, 'account': account})


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
        delivery_address = f"{address}, {post_code} {city}" if post_code else f"{address}, {city}"
        geocode = get_location_lat_long(delivery_address)
        time_dist = get_distance_time_values(Account.objects.get(user_id=user.id).location, delivery_address)
        try:
            distance = float(time_dist[0].split(" ")[0].replace(",", "."))
        except ValueError:
            distance = 0
        if not geocode:
            messages.add_message(request, messages.INFO,
                                 "Niestety nie możemy przekonwertować tego adresu, spróbuj dodać więcej danych")
            return redirect('add_order')
        order = Order.objects.create(user_id=user.id, client_name=f_name, client_surname=l_name, phone_number=phone,
                                     delivery_address=delivery_address, delivery_time=delivery_dt, opis=info,
                                     lat=geocode[0],
                                     lon=geocode[1], distance=distance, time=time_dist[1])
        order.save()
        return redirect('main_page')


class Orders_view(LoginRequiredMixin, View):
    def get(self, request, status=None):
        user = request.user.id
        if status:
            orders = Order.objects.filter(user_id=user, status=status).order_by('delivery_time')
            return render(request, 'orders_list.html', {'orders': orders})
        orders = Order.objects.filter(user_id=user).order_by('delivery_time')
        return render(request, 'orders_list.html', {'orders': orders})


class Analysis(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        orders = Order.objects.filter(user_id=user)
        ranges = [
            (orders.filter(distance__lte=20).count(), "0-20"),
            (orders.filter(distance__lte=40, distance__gt=20).count(), "20-40"),
            (orders.filter(distance__lte=80, distance__gt=40).count(), "40-80"),
            (orders.filter(distance__lte=140, distance__gt=80).count(), "80-140"),
            (orders.filter(distance__lte=220, distance__gt=140).count(), "140-220"),
            (orders.filter(distance__lte=320, distance__gt=220).count(), "220-320"),
            (orders.filter(distance__gt=320).count(), "+320"),
        ]
        current_date = datetime.date.today()
        months_ago = 6
        six_month_previous_date = current_date - datetime.timedelta(days=(months_ago * 365 / 12))
        bar_chart = orders.filter(delivery_time__gte=six_month_previous_date).annotate(
            month=TruncMonth('delivery_time')).values('month').annotate(sum=Count('id'))
        drivers = Driver.objects.raw(f"""
        
          SELECT {user} 
              AS id, "TransportApp_driver".name, SUM(distance::numeric), COUNT("TransportApp_order")
            FROM "TransportApp_order"
            JOIN "TransportApp_transport"
              ON "TransportApp_transport".order_id= "TransportApp_order".id
            JOIN "TransportApp_driver"
              ON "TransportApp_driver".id = "TransportApp_transport".driver_id
            JOIN "auth_user"
              ON "auth_user".id = {user}
        GROUP BY name
        ORDER BY SUM(distance::numeric) DESC;

        """)
        cars = Car.objects.raw(f"""
        
        SELECT {user}
            AS id, "TransportApp_car".name, SUM(distance::numeric), COUNT("TransportApp_order")
          FROM "TransportApp_order"
          JOIN "TransportApp_transport"
            ON "TransportApp_transport".order_id= "TransportApp_order".id
          JOIN "TransportApp_car"
            ON "TransportApp_car".id = "TransportApp_transport".car_id
          JOIN "auth_user"
            ON auth_user.id = 1
        GROUP BY name
        ORDER BY SUM(distance::numeric) DESC;
        
        """)
        context = {'drivers': drivers, 'cars': cars, 'ranges': ranges, 'bar_chart': bar_chart}
        return render(request, 'analysis.html', context)


class Settings(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        return render(request, 'settings.html')


class Payments(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        return render(request, 'payments.html')


class Contact(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user.id
        return render(request, 'help.html')


def delete_order(request, pk):
    user = request.user.id
    order = Order.objects.get(id=pk)
    if order.user_id == user:
        order.delete()
    return redirect('orders')
