import sqlite3

def create():
    conn = sqlite3.connect("pred.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS 'stocks'")
    c.execute(""" CREATE TABLE 'stocks'(
        'id' INTEGER PRIMARY KEY,
        'symbol' VARCHAR,
        'the_date' DATE,
        'change' INTEGER
        )""")
    c.execute("DROP TABLE IF EXISTS 'predictions'")
    c.execute(""" CREATE TABLE 'predictions'(
        'id' INTEGER PRIMARY KEY,
        'symbol' INTEGER,
        'the_date' DATE,        
        'website' VARCHAR,
        'correct' VARCHAR,
        'prediction' VARCHAR,
        'prediction_number' INTEGER
        )""")    
    conn.commit()
    c.close()

create()