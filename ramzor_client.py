import requests
import sys
sys.path.append('../rest_client')
from rest_client.ramzor_rest_client import get_data

class RamzorClient:

    def __init__(self, city):
        self.city = city

    def get_all_data(self):
        return get_data(self.city)

    def get_current(self):
        return self.get_all_data()['CurrentChart']

    def get_grades(self):
        return self.get_current()['grades']

    def get_latest_grade(self):
        return self.get_grades()[0]

