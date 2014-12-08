import sqlite3

defaultdb = 'pred.db'


class Evaluation(object):
    @staticmethod
    def _add_corrects(total):
        correct, incorrect = 0, 0
        for x in total:
            if x[0] == "correct":
                correct += 1
            elif x[0] == "incorrect":
                incorrect += 1
        return {"correct":correct, "incorrect":incorrect}

    @staticmethod
    def correct_percent(websites):
        all_results = []
        for website in websites:
            total = Database.total_correct(website)
            c_n_i = Evaluation._add_corrects(total)
            all_results.append({"percent":c_n_i["correct"]/(c_n_i["correct"] + c_n_i["incorrect"]) * 100, "website":website})
        return all_results

    @staticmethod
    def non_marginal_correct(websites):
        all_results = []
        for website in websites:
            total = Database.correct_non_negligable(website)
            c_n_i = Evaluation._add_corrects(total[1:])
            all_results.append({"percent":c_n_i["correct"]/total[0] * 100, "website":website})
        return all_results

#here we'd show the stocks that consistenly perform as predicted
    @staticmethod
    def consistent_winnners(websites):
        pass


class Stock_history(object):
    def __init__(self, symbol, the_date, change):
        self.symbol = symbol
        self.the_date = the_date
        self.change = change


class Prediction(object):
    def __init__(self, symbol, the_date, prediction, website, correct="unknown", actual_change="unknown"):
        self.symbol = symbol
        self.the_date = the_date
        self.website = website
        self.correct = correct
        self.prediction = prediction
        self.actual_change = actual_change


class Database(object):
    @staticmethod
    def insert_changes(s):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""UPDATE predictions SET actual_change = (?) WHERE the_date =
            (?) AND symbol = (?)""",(s.change, s.the_date, s.symbol))   
        conn.commit()
        c.close()
        return s

    @staticmethod
    def insert_pred(pred):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""INSERT INTO predictions(symbol, the_date, prediction, 
            website, correct) VALUES (?,?,?,?,?)
            """,(pred.symbol, pred.the_date, pred.prediction, pred.website, pred.correct))        
        conn.commit()
        c.close()
        return pred

    @staticmethod
    def daily_corrections(stock):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT id,prediction FROM predictions WHERE the_date=(?) AND 
            symbol = (?)""", (stock.the_date, stock.symbol))
        predictions = c.fetchall()
        for prediction in predictions:
            if (prediction[1] == "Up" and stock.change > 0) or (prediction[1] == "Down" and stock.change < 0):
                c.execute("""UPDATE predictions SET correct = (?) WHERE 
                    id = (?)""", ("correct", prediction[0]))
            else:
                c.execute("""UPDATE predictions SET correct = (?) WHERE 
                    id = (?)""", ("incorrect", prediction[0]))
        conn.commit()
        c.close()
        return stock

    @staticmethod
    def all_predicts_by_date(date):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT * FROM predictions WHERE the_date=(?)""", (date,))
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

    @staticmethod
    def correct_non_negligable(website):
        conn = sqlite3.connect(defaultdb)
        c  = conn.cursor()
        c.execute("""SELECT COUNT(prediction) FROM predictions WHERE website = (?)""", (website,))
        count = c.fetchone()[0]
        c.execute("""SELECT correct FROM predictions WHERE website=(?)
            AND (actual_change > .1 OR actual_change < -.1)""", (website,))
        total = c.fetchall()
        conn.commit()
        c.close()
        return [count] + total