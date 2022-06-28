from urllib.parse import urlencode
import requests
import passwords


def get_location_lat_long(adress, data_type='json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {'address': adress, "key": passwords.API_KEY}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return False
    lat_long = r.json()['results'][0]['geometry']['location']
    return [lat_long.get('lat'), lat_long.get('lng')]


def get_distance_time_values(origin, destination):
    url = f"""https://maps.googleapis.com/maps/api/distancematrix/json?origins=
                {origin}&destinations={destination}&mode=DRIVING&language=pl-PL&key={passwords.API_KEY}"""
    r = requests.get(url).json()
    time_distance = []
    for obj in r['rows']:
        for data in obj['elements']:
            time_distance.append(data['distance']['text'])
            time_distance.append(data['duration']['text'])
    return time_distance