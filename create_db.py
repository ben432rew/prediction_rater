import sqlite3

def create():
    conn = sqlite3.connect("pred.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS 'stocks'")
    c.execute(""" CREATE TABLE 'stocks'(
        'id' INTEGER PRIMARY KEY,
        'symbol' VARCHAR,
        'date' DATE,
        'change' VARCHAR,
        'change_number' INTEGER
        )""")
    c.execute("DROP TABLE IF EXISTS 'predictions'")
    c.execute(""" CREATE TABLE 'predictions'(
        'id' INTEGER PRIMARY KEY,
        'symbol' INTEGER,
        'date' DATE,        
        'prediction' VARCHAR,
        'prediction_number' INTEGER,
        'website' VARCHAR,
        )""")    
    conn.commit()
    c.close()

create()