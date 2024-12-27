import webbrowser

def find_city_on_google_earth(city_name):
    # format the URL with the search query
    google_earth_url = f'https://earth.google.com/web/search/{city_name}'

    # open google earth in the default web browser
    webbrowser.open(google_earth_url)

city_name = input('Enter city name:')

find_city_on_google_earth(city_name)