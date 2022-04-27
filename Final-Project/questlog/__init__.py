from lib2to3.pgen2.pgen import generate_grammar
import os
import psycopg2
from flask import Flask, render_template, request, flash, redirect


def create_app(test_config=None):    
    app = Flask(__name__)

    def get_db_connection():
        conn = psycopg2.connect("dbname=questlog user=postgres password=password")
        return conn

    def insert_into_table(cur, conn):
        pass

    def reset_test_table():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS games")       
        cur.execute("CREATE TABLE IF NOT EXISTS games (title varchar PRIMARY KEY NOT NULL, favorite integer DEFAULT 0, logo varchar, genre varchar, hours integer, completion integer, notes varchar)")
        cur.execute("INSERT INTO games (title, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s)",('Elden Ring', 'https://quiviracoalition.org/wp-content/uploads/2019/02/generic-person-icon.png', 'RPG', 250, 0))
        cur.execute("INSERT INTO games (title, favorite, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s, %s)",('Dark Souls', 0, 'logo.com', 'RPG', 250, 1))
        cur.execute("INSERT INTO games (title, favorite, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s, %s)",('Donkey Kong', 1, 'logo.com', 'RPG', 250, 2))
        conn.commit()
        cur.close()
        conn.close()
        return

    # a simple page that says hello
    @app.route('/', methods=["GET"])
    def index():
        #reset_test_table()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS games (title varchar PRIMARY KEY NOT NULL, favorite integer DEFAULT 0, logo varchar, genre varchar, hours integer, completion integer, notes varchar)") 
        
        cur.execute("SELECT * FROM games")
        games = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', games=games)

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/import/', methods=["GET", "POST"])
    def importform():
        if request.method == 'POST':
            conn = get_db_connection()
            cur = conn.cursor()

            title = request.form['title']
            logo = request.form['logo']
            genre = request.form['genre']
            hours = request.form['hours']
            completion = request.form['playing']

            if logo is None:
                logo = "url_for('static', filename='noimage.png')"

           
            cur.execute("INSERT INTO games (title, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s)",(title, logo, genre, hours, completion))
            #cur.execute("INSERT INTO games (title, logo, genre, hours) VALUES (%s, %s, %s, %s)",(title, logo, genre, hours))
            conn.commit()

            cur.close()
            conn.close()
            return redirect('/')

        return render_template('import.html')

    @app.route('/update', methods=["POST"])
    def update():
        conn = get_db_connection()
        cur = conn.cursor()

        title = request.form.get('title')
        favorite = request.form.get('favorite')
        notes = request.form.get('notes')
        #playing = request.form.get('playing')
        if favorite is None:
            favorite = 0
        
        cur.execute("UPDATE games SET favorite=%s, notes=%s WHERE title=%s", (favorite, notes, title))
        conn.commit()

        cur.close()
        conn.close()
        return redirect('/')

    @app.route('/sortTitle', methods=["GET"])
    def sortTitle():
        conn = get_db_connection()
        cur = conn.cursor()        

        cur.execute("SELECT * FROM games ORDER BY title ASC")
        games = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', games=games)

    @app.route('/sortFavorite', methods=["GET"])
    def sortFavorite():
        conn = get_db_connection()
        cur = conn.cursor()        

        cur.execute("SELECT * FROM games ORDER BY favorite DESC")
        games = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', games=games)

    @app.route('/sortHours', methods=["GET"])
    def sortHours():
        conn = get_db_connection()
        cur = conn.cursor()        

        cur.execute("SELECT * FROM games ORDER BY hours ASC")
        games = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', games=games)

    @app.route('/sortGenre', methods=["GET"])
    def sortGenre():
        conn = get_db_connection()
        cur = conn.cursor()        

        cur.execute("SELECT * FROM games ORDER BY genre DESC")
        games = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', games=games)
    
    @app.route('/sortCompletion', methods=["GET"])
    def sortCompletion():
        conn = get_db_connection()
        cur = conn.cursor()        

        cur.execute("SELECT * FROM games ORDER BY completion DESC")
        games = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', games=games)

    return app