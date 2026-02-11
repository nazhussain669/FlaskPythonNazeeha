from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Currencytable.html")


@app.route('/greet', methods=['POST'])
def greet():

    amount = request.form.get("amount")
    frm = request.form.get("fromCurrency")
    to = request.form.get("toCurrency")

    # Validate amount (required)
    if amount == "" or float(amount) < 0:
        result = "Please enter a valid non-negative amount."
    else:
        amount = float(amount)

        # Exchange rate dictionary
        rates = {
            "USD": {"USD":1, "EUR":1.18, "GBP":1.36, "JPY":0.0064, "CAD":0.73},
            "EUR": {"USD":0.85, "EUR":1, "GBP":1.15, "JPY":0.54, "CAD":0.62},
            "GBP": {"USD":0.74, "EUR":0.87, "GBP":1, "JPY":0.47, "CAD":0.54},
            "JPY": {"USD":157.05, "EUR":185.47, "GBP":213.59, "JPY":1, "CAD":115.12},
            "CAD": {"USD":1.36, "EUR":1.61, "GBP":1.86, "JPY":0.0087, "CAD":1}
        }

        from_rates = rates[frm] # Get the row for the FROM currency
        rate = from_rates[to] # Get the rate for the TO currency

        converted = amount * rate
        result = "Converted Amount: " + str(converted)

    return render_template("Currencytable.html", result=result)


if __name__ == '__main__':
    app.run()
