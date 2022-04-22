from flask import Flask, render_template, request
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/questlog'
#db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')