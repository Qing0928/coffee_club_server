import re
from sanic import Sanic, app
from sanic.response import json, text
import pymysql.cursors

app = Sanic("coffee_club")

def db_fetchall(sql):
    result = ''
    try:
        db_conn = pymysql.Connect(
        host='127.0.0.1', 
        user='pmauser', 
        password='game0934', 
        db='coffee', #db='game_sql'
        cursorclass=pymysql.cursors.DictCursor)

        with db_conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
        return result

    except Exception as e:
        return e

def db_fetchone(sql):
    result = ''
    try:
        db_conn = pymysql.Connect(
        host='127.0.0.1', 
        user='pmauser', 
        password='game0934', 
        db='coffee', #db='game_sql'
        cursorclass=pymysql.cursors.DictCursor)

        with db_conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchone()
        return result

    except Exception as e:
        return e

def db_modify(sql):
    result = ''
    try:
        db_conn = pymysql.Connect(
        host='127.0.0.1', 
        user='pmauser', 
        password='game0934', 
        db='coffee', #db='game_sql'
        cursorclass=pymysql.cursors.DictCursor)

        with db_conn.cursor() as cur:
            result = cur.execute(sql)
        db_conn.commit()
        return result

    except Exception as e:
        return e 

@app.get("/test")
async def test(request):
    try:
        return text("Hello World")
    except Exception as e:
        return text(str(e))

@app.get("/favicon.ico")
async def fav(request):
    return text("nothing")

@app.post("/member_info")
async def member_info(request):
    try:
        id = request.json['id']
        sql = 'SELECT * FROM `member_list` WHERE `id`={}'.format(id)
        result = db_fetchone(sql)
        return json(result)
    except Exception as e:
        print(e)
        return text(e)

@app.options("/member_info")
async def member_info(request):
    try:
        return text("got you")
    except Exception as e:
        print(e)
        return text(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8467', debug=False, access_log=True)
    app.config['workers'] = '2'