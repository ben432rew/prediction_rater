import requests
import bs4

class scrape_predictwallstreet(object):
    def __init__(self):
        self.response = requests.get('http://www.predictwallstreet.com/Forecasts/')
        self.html_string = self.response.text
        self.soup = bs4.BeautifulSoup(self.html_string)
        self.todays_predictions = self.get_todays()

    def get_todays(self):
        todays = []
        return todays


class scrape_stockforcasting(object):
    pass
