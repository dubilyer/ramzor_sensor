from pathlib import Path
import sys
if __package__ is None:
    DIR = Path(__file__).resolve().parent
    print(DIR)
    print(str(DIR.parent))
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name
from .rest_client.ramzor_rest_client import get_data
from .colors import Colors

class RamzorClient:

    def __init__(self, city):
        self.city = city

    def get_all_data(self):
        return get_data(self.city)

    def get_current(self):
        return self.get_all_data()['CurrentChart']

    def get_grades(self):
        return self.get_current()['grades']

    def get_color(self):
        return Colors(self.get_current()['color'])

    def get_latest_grade(self):
        return self.get_grades()[0]

