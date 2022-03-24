import re


def register_validator(email, password, password2):
    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(reg, email):
        if password == password2:
            return True
        return "Hasła się ze sobą nie zgadzają"
    return "Nieprawidłowy email"
