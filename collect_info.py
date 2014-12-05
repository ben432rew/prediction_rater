import requests
import bs4

class Scrape_predictwallstreet(object):
    def __init__(self):
        self.response = requests.get('http://www.predictwallstreet.com/Forecasts/')
        self.html_string = self.response.text
        self.soup = bs4.BeautifulSoup(self.html_string)
        self.todays_predictions = self.get_todays()

    def get_todays(self):
        todays = []
        rows = self.soup.select("div.one-day-forecasts div table tbody tr")
        for row in rows:
            print (row)
            prediction = {}
            symbol = row.select('td h3')[0].get_text()
            pred = row.select('td span')[0].get_text()
            prediction["symbol"] = symbol
            prediction["prediction"] = pred
            todays.append(prediction)
        return todays


class Scrape_stockforcasting(object):
    pass

h = Scrape_predictwallstreet()
print(h.todays_predictions)