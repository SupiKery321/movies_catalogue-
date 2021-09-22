from flask import Flask
import sqlite3
import sqlite3
from flask import Flask
from models import SQL
from flask import abort
from flask import request


app = Flask(__name__)
app.config["SECRET_KEY"] = "mimimimimi"



@app.route("/", methods=["GET"])
def homepage():
    SQL.create()


@app.route("/api/v1/SQL/<int:sql_id>", methods=["GET"])
def get_sql(sql_id):
    sql = SQL.get(sql_id)
    if not sql:
        abort(404)
    return sqlite3({"sql": sql})

@app.route("/api/v1/SQL/", methods=["POST", "GET"])
def create_todo():
    sql = '''INSERT INTO projects(id, expense, price, done)
       VALUES (1,
               "woda",
               "1000",
               "zapłacone");
               INSERT INTO projects(id, expense, price, done)
       VALUES (2,
               "prąd",
               "800",
               "zapłacone");
               INSERT INTO projects(id, expense, price, done)
       VALUES (3,
               "ogrzewanie",
               "200",
               "zapłacone");
               INSERT INTO projects(id, expense, price, done)
       VALUES (4,
               "jedzenie",
               "2000",
               "zapłacone");'''
    SQL.create(sql)

@app.route("/api/v1/SQL/<int:sql_id>", methods=["PUT"])
def update_todo(sql_id):
    sql = SQL.get(sql_id)
    if not sql:
        abort(404)
    if not request(sql):
        abort(400)
    data = sql
    if any([
        'expense' in data and not isinstance(data.get('expense'), str),
        'price' in data and not isinstance(data.get('price'), str),
        'done' in data and not isinstance(data.get('done'), str)
    ]):
        abort(400)
    sql = {
        'expense': data.get('expense', sql['expense']),
        'price': data.get('price', sql['price']),
        'done': data.get('done', sql['done'])
    }
    SQL.update(sql_id, sql)
    


if __name__ == "__main__":
    app.run(debug=True)



