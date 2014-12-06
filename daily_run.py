import model
import collect_info
import datetime

#every weekday at 8am this script will run

class Daily_duties(object):
    self.todays_predicts = daily_check()
    self.save_predicts()
    self.yesterdays_predicts = model.Database.get_symbols_by_date(datetime.datetime.today() - datetime.timedelta(days=1))
    self.yesterday_changes()

    def daily_check(self):
        todays_symbols = []
        pws = collect_info.Scrape_predictwallstreet()
        for stock in pws.todays_predictions:
            todays_symbols.append(stock["symbol"])
        ssf = Scrape_stockforcasting(todays_symbols)
        return pws.todays_predictions + ssf.predictions

    def save_predicts(self):
        for pred in self.todays_predicts:
            p = model.Prediction(pred["symbol"], datetime.datetime.today(), pred["prediction"], pred["website"])
            model.Database.insert_pred(p)

    def yesterday_changes
        pass
        #store actual stocks from yesterday
        #update prediction results (correct or no)


today = Daily_duties()