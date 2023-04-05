from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
import requests


def main():
    return requests.get(url='https://www.google.com')


if __name__ == '__main__':
    print(f'Текущая дата {date.today()}')
    calculate_salary()
    get_employees()
    print(main())