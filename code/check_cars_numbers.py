import requests
import pandas as pd

from typing import List

from json_unpacking import iterative_json_unpacking

API_KEY = 'c9a8220ef3daeee290555beecb91c198'
headers = {'Accept': 'application/json',
           'X-Api-Key': API_KEY}
api_url = 'https://baza-gai.com.ua/nomer/'


def check_car_number(car_number: str):
    """Make a get request with the car number to API.
       Returns json"""
    url = f'{api_url}{car_number}'
    response = requests.get(url, headers=headers)
    return response.json()


def get_checked_numbers_list(cars_numbers: List[str]) -> List[dict]:
    """Сalls a function check_car_number for each of the car numbers from the list,
       checks if an empty json is returned, returns a list of checked cars"""
    checked_numbers_list = []
    for car in cars_numbers:
        result = check_car_number(car)
        if result.get('digits') is None:
            continue
        checked_numbers_list.append(result)
    return checked_numbers_list


def get_unpacked_numbers_list(checked_numbers_list: List[dict]) -> List[dict]:
    """Returns a list of unpacked json for each element in the list of checked numbers"""
    unpacked_numbers_list = []
    for number in checked_numbers_list:
        unpacked_number = iterative_json_unpacking(number)
        unpacked_numbers_list.append(unpacked_number)
    return unpacked_numbers_list


def main():
    """Checks the numbers from the list, unpacks all values from the json, creates a dataframe with the received
       information and writes it to an excel file """
    cars_numbers = ['CE1789BA', 'CE1786BA', 'CB8136AX', 'AE8181EX']
    checked_numbers_list = get_checked_numbers_list(cars_numbers)
    unpacked_numbers_list = get_unpacked_numbers_list(checked_numbers_list)

    df = pd.DataFrame(unpacked_numbers_list)
    df.to_excel('checked_cars.xlsx', index=False)


if __name__ == '__main__':
    main()
