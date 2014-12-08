import sqlite3

def create():
    conn = sqlite3.connect("pred.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS 'stocks'")
    c.execute("DROP TABLE IF EXISTS 'predictions'")
    c.execute(""" CREATE TABLE 'predictions'(
        'id' INTEGER PRIMARY KEY,
        'symbol' INTEGER,
        'the_date' DATE,        
        'website' VARCHAR,
        'correct' VARCHAR,
        'prediction' VARCHAR,
        'actual_change' INTEGER
        )""")    
    conn.commit()
    c.close()

create()