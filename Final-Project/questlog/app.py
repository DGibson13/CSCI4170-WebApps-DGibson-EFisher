from flask import Flask, render_template, request
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/questlog'
db = sqlalchemy(app)


@app.route('/')
def index():
    return render_template('index.html')