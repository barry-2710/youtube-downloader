import os
import sqlite3
from datetime import date,datetime
from pytube import YouTube
from kivymd.toast import toast
import re
def write_history(url,option):
    try:
        yt = YouTube(url)
        title = yt.title
        name1 = ""
        j=0
        for elem in str(title):
            j+=1
            if(j==30):
                break
            else:
                name1 += elem
        line = str(name1)
        line = re.sub('[|]', ',', line)
        if(option=="mp3"):
            name1 = line+".mp3"
        else:
            name1 = line+".mp4"
        print("saving",name1)
    
    
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
   

        with sqlite3.connect("test.db") as db:
                    cursor=db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS download(id INTEGER PRIMARY KEY,name VARCHAR(20) NOT NULL,date VARCHAR(20) NOT NULL,time VARCHAR(20) NOT NULL);
        """)

        cursor.execute("""
        INSERT INTO download(name, date, time)
        VALUES (?,?,?)
        """, (name1, today, current_time))



        db.commit()
    except Exception as e:
        toast("error")
        print(e)

  
