import os
import psycopg2
from flask import Flask, render_template


def create_app(test_config=None):    
    app = Flask(__name__)

    def get_db_connection():
        conn = psycopg2.connect("dbname=questlog user=postgres password=password")
        return conn

    # a simple page that says hello
    @app.route('/')
    def index():
        # Test db code, final code should be in their own functions
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS games')
        cur.execute("CREATE TABLE games (title varchar PRIMARY KEY, favorite integer, logo varchar, genre varchar, hours integer, completion integer, notes varchar)")
        cur.execute("INSERT INTO games (title, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s)",('Elden Ring', 'logo.com', 'RPG', 250, 0))        
        cur.execute("SELECT * FROM games WHERE title = %s", ('Elden Ring',))
        games = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return render_template('index.html', games=games)

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/import')
    def importform():
        return render_template('import.html')

    return app