from flask import Flask, render_template, request
from mortgage_calculation import mortgage_calc

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    price, initial_fee = 0, 0
    term, term_type = 0, ""
    percent = 0

    if request.method == 'POST':
        price = request.form.get('price_input')
        initial_fee = request.form.get('initial_fee_input')
        term = request.form.get('term_input')
        term_type = request.form.get('term_type')
        percent = request.form.get('percent_input')

    result = mortgage_calc(price, initial_fee, percent, term, term_type)

    if result:
        return render_template('index.html', ans1=result[0], ans2=result[1], ans3=result[2], ans4=result[3])
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
