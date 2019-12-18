import datetime


def birthday():
    year = int(input("What year were you born [YYYY]? "))
    month = int(input("What month were you born [MM]? "))
    date = int(input("What date were you born [DD]? "))
    birthday = datetime.date(year, month, date)
    return birthday


def calculation(date):
    today = datetime.date.today()
    current_year = datetime.date(today.year, date.month, date.day)
    return (current_year - today).days


def output(days):
    if days < 0:
        print(f"You had your birthday {-days} days ago this year.")
    elif days > 0:
        print(f"Your birthday is in {days} days!")
    else:
        print("HAPPY BIRTHDAY!!!")


def main():
    output(calculation(birthday()))


if __name__ == '__main__':
    main()
