#References: 
#https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
#https://www.dataquest.io/blog/python-datetime-tutorial/#:~:text=Datetime%20will%20give%20us%20the,and%20a%20method%20called%20day_name%20.
#https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
#https://www.programiz.com/python-programming/datetime/strftime


from flask import Flask, render_template, request
import datetime #importing datetime module for now()

app = Flask(__name__)

@app.get('/')
def index():
    current_time = datetime.datetime.now()
    time = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%A %B %d, %Y")
    return render_template('index.html', date=date, time=time)



