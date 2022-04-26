import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="questlog",
        user='postgres',
        password='password')
        
        
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS games;')
"""
cur.execute('CREATE TABLE games (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('CREATE TABLE IF NOT EXISTS library.games (title character varying COLLATE pg_catalog."default" NOT NULL,'
                                'favorite integer,'
                                'logo character varying COLLATE pg_catalog."default",'
                                'genre character varying COLLATE pg_catalog."default",'
                                'hours integer,'
                                'notes character varying COLLATE pg_catalog."default",'
                                'completion integer,'
                                'CONSTRAINT games_pkey PRIMARY KEY (title))'
                                )
"""
cur.execute("CREATE TABLE games (title varchar PRIMARY KEY, favorite integer, logo varchar, genre varchar, hours integer, completion integer, notes varchar);")
# Insert data into the table
"""
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )
"""
cur.execute('INSERT INTO games (title, logo, genre, hours, completion) VALUES (%s, %s, %s, %s, %s)',
                "'Elden Ring', 'logo.com', 'RPG', '250', 'No')")

conn.commit()

cur.close()
conn.close()