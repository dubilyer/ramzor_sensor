import requests
import csv
import sys
sys.path.append('../rest_client')
from rest_client.ramzor_rest_client import get_suggestions

def cities_by_letter(letter):
    suggestions = get_suggestions(letter)
    cities = []
    for city in suggestions:
        cities.append(
            [city['data']['cityDescriptionHE'], city['data']['cityDescriptionEN'], city['data']['cityCode']]
        )
    return cities

def cities():
    cities = []
    for letter in "א ב ג ד ה ו ז ח ט י כ ל מ נ ס ע פ צ ק ר ש ת":
        cities = cities + cities_by_letter(letter)
    return cities

def write_cities():
    with open('cities.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['Hebrew name', 'English name', 'code'])
        writer.writerows(cities())

write_cities()