import requests

BASE_URL = 'https://corona.health.gov.il/umbraco/surface/Traffic/'


def get_suggestions(letter):
    url = BASE_URL + 'AreaGetSuggestions?culture=he-IL&query={}'.format(letter)
    return requests \
        .get(url) \
        .json()['suggestions']


def get_data(city):
    url = BASE_URL + 'RenderChartData?cityCode={}'.format(city)
    return requests \
        .get(url) \
        .json()
