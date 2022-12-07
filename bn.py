
import sqlite3 as sq
import streamlit as st
import datetime
from datetime import date
import pandas as pd

def func():
    

    conn=sq.connect("data.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS coco(time DATE,name TEXT,count INTEGER)''')
    conn.commit()
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'coco',24))
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'pepsi',19))
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'coco',17))
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'fanta',27))
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'banana',6))
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'lotion',21))
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'cream',21))
    conn.execute('''INSERT INTO coco VALUES(?,?,?) ''',(date.today(),'banana',21))
    conn.commit()
    pic = conn.execute('''SELECT * FROM coco''')

    df = pd.DataFrame(pic,columns=['time','name','count'])
    st.table(df)

    ct=conn.execute('''SELECT name,SUM(count) FROM coco GROUP BY name''')

    ctt = pd.DataFrame(ct,columns=['','count'])
    ctt.set_index('',inplace=True)
    st.table(ctt)

def clear():
    conn=sq.connect("data.db")
    pic=conn.execute('''Delete from coco''')
    pic = conn.execute('''SELECT * FROM coco''')

    df = pd.DataFrame(pic,columns=['time','name','count'])
    st.table(df)

    ct=conn.execute('''SELECT name,SUM(count) FROM coco GROUP BY name''')

    ctt = pd.DataFrame(ct,columns=['','count'])
    ctt.set_index('',inplace=True)
    st.table(ctt)
    


