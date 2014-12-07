import sqlite3
import datetime

defaultdb = 'pred.db'


#predictions should be weighted by how much they changed, not just whether
#they went up or down
class Evaluation(object):
    @staticmethod
    def correct_not_ratios(websites):
        all_results = []
        for website in websites:
            total = Database.total_correct(website)
            correct = 0
            incorrect = 0        
            for x in total:
                if x == "correct":
                    correct += 1
                elif x == "incorrect":
                    incorrect += 1
            all_results.append({"ratio":correct/incorrect, "website":website})
        return all_results


class Stock(object):
    def __init__(self, symbol, the_date, change):
        self.symbol = symbol
        self.the_date = the_date
        self.change = change

    def get_todays(self):
        return Database.todays_pred(self)


class Prediction(object):
    def __init__(self, symbol, the_date, prediction, website, correct="unknown", prediction_number="None"):
        self.symbol = symbol
        self.the_date = the_date
        self.website = website
        self.correct = correct
        self.prediction = prediction
        self.prediction_number = prediction_number


class Database(object):
    @staticmethod
    def insert_stock(s):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""INSERT INTO stocks(symbol, the_date, change) 
            VALUES (?,?,?)
            """,(s.symbol, s.the_date, s.change))   
        conn.commit()
        c.close()
        return s

    @staticmethod
    def insert_pred(pred):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""INSERT INTO predictions(symbol, the_date, prediction, 
            prediction_number, website, correct) VALUES (?,?,?,?,?,?)
            """,(pred.symbol, pred.the_date, pred.prediction, pred.prediction_number, pred.website, pred.correct))        
        conn.commit()
        c.close()
        return pred

    @staticmethod
    def todays_pred(pred):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT * FROM predictions WHERE the_date=(?) AND 
            symbol = (?)""", (pred.symbol, pred.the_date))
        pred = c.fetchone()[0]
        p = Prediction(pred[1], pred[2], pred[3], pred[4], pred[5], pred[6])
        conn.commit()
        c.close()
        return p

    @staticmethod
    def daily_correct(stock):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT id,prediction FROM predictions WHERE the_date=(?) AND 
            symbol = (?)""", (stock.symbol, stock.the_date))
        predictions = c.fetchall()
        for prediction in predictions:
            if (prediction[1] == "up" and stock.change > 0) or (prediction[1] == "down" and stock.change < 0):
                c.execute("""UPDATE predictions(correct) SET correct = (?) WHERE 
                    id = (?)""", ("correct", prediction[0]))
            else:
                c.execute("""UPDATE predictions(correct) SET correct = (?) WHERE 
                    id = (?)""", ("incorrect", prediction[0]))                
        conn.commit()
        c.close()
        return stock

    @staticmethod
    def all_todays():
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT * FROM predictions WHERE the_date=(?)
            """, (datetime.datetime.today()))
        predictions = []
        preds = c.fetchall()
        for p in preds:
            next_one = Prediction(p[1], p[2], p[3], p[4], p[5], p[6])
            predictions.append(next_one)
        conn.commit()
        c.close()
        return predictions

    @staticmethod
    def get_symbols_by_date(date):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT DISTINCT symbol FROM predictions WHERE the_date=(?)
            """, (date,))
        symbols = c.fetchall()
        conn.commit()
        c.close()
        return symbols

    @staticmethod
    def total_correct(website):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT correct FROM predictions WHERE website=(?)""", (website,))
        total = c.fetchall()
        conn.commit()
        c.close()
        return total

