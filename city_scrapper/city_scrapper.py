import csv
import sys
from pathlib import Path
if __package__ is None:
    DIR = Path(__file__).resolve().parent
    print(DIR)
    print(str(DIR.parent))
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name
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
    for letter in "אבגדהוזחטיכלמנסעפצקרשת":
        cities = cities + cities_by_letter(letter)
    return cities

def write_cities():
    with open('cities.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['Hebrew name', 'English name', 'code'])
        writer.writerows(cities())

write_cities()