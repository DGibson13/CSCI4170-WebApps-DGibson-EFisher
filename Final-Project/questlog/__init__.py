import os
import psycopg2
from flask import Flask, render_template, request


def create_app(test_config=None):    
    app = Flask(__name__)

    def get_db_connection():
        conn = psycopg2.connect("dbname=questlog user=postgres password=password")
        return conn

    def insert_into_table(cur, conn):
        pass

    def test_insert_into_table():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS games')
        cur.execute("CREATE TABLE games (title varchar PRIMARY KEY, favorite integer DEFAULT 0, logo varchar, genre varchar, hours integer, completion integer, notes varchar DEFAULT '---')")
        cur.execute("INSERT INTO games (title, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s)",('Elden Ring', 'https://quiviracoalition.org/wp-content/uploads/2019/02/generic-person-icon.png', 'RPG', 250, 0))
        cur.execute("INSERT INTO games (title, favorite, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s, %s)",('Dark Souls', 0, 'logo.com', 'RPG', 250, 1))
        cur.execute("INSERT INTO games (title, favorite, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s, %s)",('Donkey Kong', 1, 'logo.com', 'RPG', 250, 2))
        conn.commit()        
        cur.close()
        conn.close()
        return

    # a simple page that says hello
    @app.route('/')
    def index():
        test_insert_into_table()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS games (title varchar PRIMARY KEY, favorite integer DEFAULT 0, logo varchar, genre varchar, hours integer, completion integer, notes varchar DEFAULT '---')") 
        
        cur.execute("SELECT * FROM games")
        games = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', games=games)

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/import/', methods=('GET', 'POST'))
    def importform():
        return render_template('import.html')

    return app