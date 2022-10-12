# pylint: disable=missing-docstring,invalid-name

import requests

URL = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"
response = requests.get(URL, timeout=15).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
