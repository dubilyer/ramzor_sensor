import requests

class RamzorClient:
    URL = 'https://corona.health.gov.il/umbraco/surface/Traffic/RenderChartData?cityCode={}'

    def __init__(self, city):
        self.city = city

    def get_all_data(self):
        return requests.get(self.URL.format(self.city)).json()

    def get_current(self):
        return self.get_all_data()['CurrentChart']

    def get_grades(self):
        return self.get_current()['grades']

    def get_latest_grade(self):
        return self.get_grades()[0]

