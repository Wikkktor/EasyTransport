import os
from urllib.parse import urlencode
from passwords import API_KEY
import requests


def get_location_lat_long(address, data_type='json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {'address': address, "key": API_KEY}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}  # TODO: error or something
    lat_long = r.json()['results'][0]['geometry']['location']
    return [lat_long.get('lat'), lat_long.get('lng')]

