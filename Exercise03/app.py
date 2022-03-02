# References:

from flask import Flask, render_template, request


app = Flask(__name__)

results = []



@app.get('/')
def index():
    integer = request.args.get('integer')
    return render_template('index.html', integer=integer)


@app.get('/students')
def get_students():
    return render_template('students.html')

@app.post('/students')
def post_students():
    return render_template('students.html')