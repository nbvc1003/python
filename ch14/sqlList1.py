import sqlite3, sys
import pandas as pd

dbpath = 'test.sqlite'
try:
    con = sqlite3.connect(dbpath)
    csr = con.cursor()
    # items 테이블이 존재 하면 삭제
    # 필드 (name, price 생성) 데이터 입력
    # execute 한줄 명령
    # executescript 여러줄 명령어 입력
    csr.executescript("""
    drop table if exists items;
    create table items(item_id integer primary key autoincrement, 
    name text, price integer);
    insert into items(name, price) values('apple',800);
    insert into items(name, price) values('orange',780);
    insert into items(name, price) values('banana',400);
    """)
    con.commit()
except:
    print('에러',sys.exc_info())
else:
    print('성공')
finally:
    con.close()