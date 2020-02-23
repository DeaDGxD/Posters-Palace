import sqlite3
from flask import request
import datetime
def make_comment():
    car = datetime.datetime.now()
    far = f"{car.month}-{car.day}-{car.year}  {car.hour}:{car.minute}  {car.second}"
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    # c.execute('''create table post(
    #             name message_text ,
    #             comment message_text,
    #             time time ,
    #
    # )''')
    c.execute('insert into post(name , comment, time) values (?,?,?)',(request.form['username'], request.form['message'], far))
    conn.commit()
    conn.close()
def get_comment():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute('select * from post')
    return c.fetchall()