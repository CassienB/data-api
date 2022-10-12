# pylint: disable=missing-module-docstring

import sys
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       #Return one city (or None)
    '''
    url = f"{BASE_URI}/geo/1.0/direct?q={query}&limit=5"
    response = requests.get(url, timeout=15).json()

    if len(response) == 0:
        print("Sorry, we didn't find this city")
        return None

    if len(response) >= 2:
        for index, rep in enumerate(response):

            print(f'{index + 1} - {rep["name"].capitalize()}, {rep["country"]}')
        choice = input("Multiple matches found, which city did you mean? \n >")
        city = response[int(choice) -1]
        return city

    city = response[0]
    return city


def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    urlw = f"{BASE_URI}/data/2.5/forecast?lat={lat}&lon={lon}&units=metric"
    liste = []
    weathers = requests.get(urlw, timeout=15).json()

    for weather in weathers["list"]:
        if weather["dt_txt"][-8:] == '12:00:00':
            liste.append(weather)
    return liste



def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    if city is not None:
        fivedays = weather_forecast(float(city["lat"]), float(city["lon"]))

        print(f"Here's the weather in {city['name']}")
        for day in fivedays:
            print(
                f'{day["dt_txt"][:10]}: {day["weather"][0]["main"].capitalize()} ({day["main"]["temp_max"]}°C)'

                )


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
