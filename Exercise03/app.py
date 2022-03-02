# References:
# https://tutorial.eyehunts.com/python/python-global-dictionary-example-code/
# https://www.fullstackpython.com/flask-globals-g-examples.html
# https://www.w3schools.com/python/python_dictionaries.asp 
# https://www.guru99.com/python-dictionary-append.html

from flask import Flask, render_template, request, g


app = Flask(__name__)

#results = []

dictionary = {"Name":[]} #key=name:value=organization

@app.get('/')
def index():
    integer = request.args.get('integer')
    return render_template('index.html', integer=integer)


@app.get('/students')
def get_students():
    return render_template('students.html')

@app.post('/students')
def post_students():
    name = request.form.get('name', 'Nothing')
    organization = request.form.get('organization', 'nothing')
    dictionary['Name'].append('organization')
    
    return render_template('students.html', name=name, organization=organization, dictionary=dictionary)