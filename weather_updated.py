import pyfiglet
import collections


Location = collections.namedtuple("Location", "city state country")


def main():
    print(pyfiglet.figlet_format("Weather App"))
    location_text = input("Where do you want the weather report (e.g. Portland, US)? ")
    location = convert_plain_text(location_text)
    city, state, country = location
    


def convert_plain_text(location_text):
    if not location_text or not location_text.strip():
        return None
    location_text = location_text.lower().strip()
    parts = location_text.split(",")
    city = ""
    state = ""
    country = "usa"
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



if __name__ == "__main__":
    main()