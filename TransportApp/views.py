from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .geocode import get_location_lat_long, get_distance_time_values
from .models import Order, Transport, Car, Driver

class MainPage(View):
    def get(self, request):
        return render(request, "main_page.html")


class Add_order(View):
    def get(self, request):
        return render(request, "add_order.html")

    def post(self, request):
        user = request.user
        print(user)
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



class Orders_view(View):
    def get(self, request):
        return render(request, 'orders_list.html')
