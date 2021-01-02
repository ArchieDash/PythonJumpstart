import pyfiglet
import collections
import requests


Location = collections.namedtuple("Location", "city state country")
Weather = collections.namedtuple("Weather", "location units temp condition")


def main():
    print(pyfiglet.figlet_format("Weather App"))
    location_text = input("Where do you want the weather report (e.g. Portland, US)? ")
    location = convert_plain_text(location_text)
    report_weather(location)
    

def convert_plain_text(location_text):
    if not location_text or not location_text.strip():
        return None
    location_text = location_text.lower().strip()
    parts = location_text.split(",")
    city = ""
    state = ""
    country = "us"
    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()
        country = parts[2].strip()
    else:
        return None
    return Location(city, state, country)


def call_weather_api(loc):
    url = "https://weather.talkpython.fm/api/weather"
    params = {
        "city": loc.city,
        "state": loc.state,
        "country": loc.country
    }
    resp = requests.get(url, params=params)
    if resp.status_code in {400, 404, 500}:
        print(f"Error: {resp.text}.")
    data = resp.json()
    return convert_api_to_weather(data, loc)


def convert_api_to_weather(data, loc):
    temp = data.get("forecast").get("temp")
    w = data.get("weather")
    condition = f"{w.get('category')}: {w.get('description').capitalize()}."
    weather = Weather(loc, data.get("units"), temp, condition)
    return weather


def get_location_name(location):
    if not location.state:
        return f"{location.city.capitalize()}, {location.country.upper()}"
    else:
        return f"{location.city.capitalize()}, {location.state.upper()} {location.country.upper()}"


def get_scale(weather):
    if weather.units == "imperial":
        return "F"
    else:
        return "C"


def report_weather(location):
    weather = call_weather_api(location)
    scale = get_scale(weather)
    print(f"The weather in {get_location_name(location)} is {weather.temp} {scale} and {weather.condition}")


if __name__ == "__main__":
    main()