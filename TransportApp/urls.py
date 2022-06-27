from django.contrib import admin
from django.urls import path
from TransportApp import views as v
urlpatterns = [
    path('', v.MainPage.as_view(), name="main_page"),
    path('dodaj-zamowienie/', v.Add_order.as_view(), name='add_order')
]