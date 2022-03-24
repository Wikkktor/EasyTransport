from django.urls import include, path
from .views import Register_view, Login_view, Logout_view

urlpatterns = [
    path('rejestracja/', Register_view.as_view(), name='register'),
    path('zaloguj/', Login_view.as_view(), name='sign_in'),
    path('wyloguj/', Logout_view.as_view(), name='sign_out')
]
