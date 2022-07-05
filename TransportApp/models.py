from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)


class Order(models.Model):
    DELIVERY_STATUS = [
        (1, "Nowe"),
        (2, "Zdefiniowano Transport"),
        (3, "Zrealizowane"),
        (4, 'Anulowane')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    client_surname = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    delivery_address = models.CharField(max_length=300)
    delivery_time = models.DateTimeField()
    status = models.IntegerField(choices=DELIVERY_STATUS, default=1)
    opis = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length=300, null=True)
    lon = models.CharField(max_length=300, null=True)
    distance = models.FloatField(null=True, blank=True)
    time = models.CharField(max_length=300, null=True)

    def get_absolute_url(self):
        return reverse('order_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('order_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('order_update_view', args=(self.pk,))

    def client(self):
        return self.client_name + " " + self.client_surname

    def __str__(self):
        return self.client + "\n" " Adres " + self.delivery_address


class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('driver_list_view')

    def get_delete_url(self):
        return reverse('driver_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('driver_update_view', args=(self.pk,))

    def __str__(self):
        return self.name


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('car_list_view')

    def get_delete_url(self):
        return reverse('car_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('car_modify_view', args=(self.pk,))

    def __str__(self):
        return self.name


class Transport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('transport_list_view')

    def get_delete_url(self):
        return reverse('transport_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('transport_update_view', args=(self.pk,))

    def __str__(self):
        name = f"Samochód: {self.car.name} Kierowca: {self.driver.name} zamówienie: {self.order}"
        return name
