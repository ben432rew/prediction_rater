import model
import collect_info
import datetime

#every day Monday-Saturday at 8am this script should be run, for linux set in 
#for testing, change date in the definition of self.yesterdays_symbols
#and in the definition of yesterday from the first line in yesterdays_changes
#to equal today
#yesterday definition doesn't account for weekends!
class Daily_duties(object):
    def __init__(self):
        self.todays_predicts = self.get_predicts()
        self.save_predicts()
        self.yesterdays_symbols = model.Database.symbols_by_date(datetime.date.today() - datetime.timedelta(days=1))
        self.yesterday_changes()

    def get_predicts(self):
        todays_symbols = []
        pws = collect_info.Scrape_predictwallstreet()
        for stock in pws.todays_predictions:
            todays_symbols.append(stock["symbol"])
        ssf = collect_info.Scrape_stockforcasting(todays_symbols)
        return pws.todays_predictions + ssf.predictions

    def save_predicts(self):
        for pred in self.todays_predicts:
            p = model.Prediction(pred["symbol"], datetime.date.today(), pred["prediction"], pred["website"])
            model.Database.insert_pred(p)

    def yesterday_changes(self):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        s = collect_info.Stock_history(self.yesterdays_symbols)
        for stock in s.history:
            st_obj = model.Stock_history(stock["symbol"], yesterday, stock["change"])
            model.Database.insert_changes(st_obj)
            model.Database.daily_corrections(st_obj)
        return s


today = Daily_duties()