import re
from django.contrib.auth.models import User
from django.contrib import messages


def register_validator(request, email, password, password2):
    # TODO: zrobić walidacje rejestracji
    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(reg, email):
        check_user = User.objects.filter(email=email)
        if check_user:
            messages.add_message(request, messages.ERROR, "Podany email jest zajęty")
            return False
        if password == password2:
            return True
        messages.add_message(request, messages.ERROR, "Podane hasła się różnią")
        return False
    messages.add_message(request, messages.ERROR, "Nie prawidłowy email")
    return False
