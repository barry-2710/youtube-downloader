import sqlite3
from datetime import date,datetime

def show():
    with sqlite3.connect("test.db") as db:
                    cursor=db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS download(id INTEGER PRIMARY KEY,name VARCHAR(20) NOT NULL,date VARCHAR(20) NOT NULL,time VARCHAR(20) NOT NULL);
    """)
                
    db.commit()


    cursor.execute("SELECT 'id' AS id,'name' AS name, 'date' AS date,'time' AS time UNION ALL SELECT id, name, date, time FROM download")
    data=cursor.fetchall()
    return data
