from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/')
def index_1():
    value = int(request.form.get('num_1'))
    return render_template("index.html", range_value=value)


@app.route('/', methods=['post', 'get'])
def form():
    price, initial_fee = 0, 0
    term, term_type = 0, ""
    percent = 0

    if request.method == 'POST':
        price = int(request.form.get('price_input'))
        initial_fee = int(request.form.get('initial_fee_input'))
        term = int(request.form.get('term_input'))
        term_type = request.form.get('term_type')
        percent = float(request.form.get('percent_input'))

    if term_type == "Y":
        term *= 12

    credit_amount = price-initial_fee
    monthly_per = percent / 12 / 100
    total_rate = (1 + monthly_per)**term
    payment = credit_amount * monthly_per * total_rate / (total_rate-1)
    total = payment * term
    charges = total - credit_amount

    return render_template('index.html', ans1=credit_amount, ans2=round(payment), ans3=round(charges), ans4=round(total))


if __name__ == '__main__':
    app.run()
