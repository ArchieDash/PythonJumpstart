import requests


def print_the_header():
    print("----------------------------------------")
    print("               WEATHER APP              ")
    print("----------------------------------------")


def get_html(zip_code):
    url = f"http://www.wunderground.com/weather-forecast/{zip_code}"

    
def main():
    # print header
    print_the_header()
    # get zipcode
    zip_code = input("What zipcode do you want the weather for?")
    # get html
    get_html(zip_code)
    # parse html
    # display forecast


if __name__ == "__main__":
    main()
