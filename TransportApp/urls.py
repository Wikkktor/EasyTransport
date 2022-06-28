from django.contrib import admin
from django.urls import path
from TransportApp import views as v
urlpatterns = [
    path('', v.MainPage.as_view(), name="main_page"),
    path('dodaj-zamowienie/', v.Add_order.as_view(), name='add_order'),
    path('zamowienia/', v.Orders_view.as_view(), name='orders'),
    path('analiza/', v.Analysis.as_view(), name='analysis'),
    path('ustawienia/', v.Settings.as_view(), name='settings'),
    path('kontakt-pomoc/', v.Contact.as_view(), name='contact')
]