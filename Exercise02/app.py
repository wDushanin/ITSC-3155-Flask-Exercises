# References:
# https://kanchanardj.medium.com/redirecting-to-another-page-with-button-click-in-python-flask-c112a2a2304c
# https://testbook.com/blog/how-do-i-link-a-submit-button-to-another-webpage-using-html/#:~:text=In%20HTML%2C%20linking%20submit%20buttons,property%20of%20the%20Anchor%20element.
# https://note.nkmk.me/en/python-list-clear-pop-remove-del/
# https://stackoverflow.com/questions/12551526/cast-flask-form-value-to-int


from flask import Flask, render_template, request


app = Flask(__name__)

results = []



@app.get('/')
def index():
    integer = request.args.get('integer')
    return render_template('index.html', integer=integer)


@app.get('/result')
def result():
    integer = request.args.get('integer', 'ERROR 400: No query parameter entered')
    results.clear()  # Removes the current items in results so that the server won't print repeated inputs
    try:
        results.append(int(integer))
    except:
        breakpoint
    return str(render_template('result.html', integer=integer, results=results))
