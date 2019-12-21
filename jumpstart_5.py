import requests
from collections import namedtuple 
from bs4 import BeautifulSoup


def print_the_header():
    print("----------------------------------------")
    print("               WEATHER APP              ")
    print("----------------------------------------")


def get_html(zip_code):
    url = f"http://www.wunderground.com/weather-forecast/{zip_code}"
    response = requests.get(url)
    return response.text


def forecast(html):
    soup = BeautifulSoup(html, "html.parser")
    location = soup.find(class_="region-content-top")\
               .find("h1").find("span").get_text()
    condition = soup.find(class_="condition-icon").get_text()
    temp = soup.find(class_="conditions-circle")\
               .find(class_="wu-value").get_text()
    scale = soup.find(class_="conditions-circle")\
               .find(class_="wu-label").get_text()
    frame = namedtuple("Forecast", "loc , cond, tmp, scl")
    report = frame(loc=location, cond=condition, tmp=temp, scl=scale)
    return report
    
       
def main():
    # print header
    print_the_header()
    # get zipcode
    zip_code = input("What zipcode do you want the weather for?")
    # get html
    html = get_html(zip_code)
    # parse html
    report = forecast(html)
    # display forecast
    print(f"{report.loc}:\n{report.cond} / {report.tmp} {report.scl}")


if __name__ == "__main__":
    main()
