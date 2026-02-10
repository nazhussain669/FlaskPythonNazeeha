from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('Currencytable.html')

@app.route('/greet', methods=['POST'])
def greet():
    amount = request.form.get("amount")
    frm = request.form.get("fromCurrency")
    to = request.form.get("toCurrency")

    if amount == "" or float(amount) < 0:
        result = "Please enter a valid non-negative amount."
    else:
        amount = float(amount)

    if frm == "USD":
        if to == "USD":
            rate = 1
        else:
            if to == "EUR":
                rate = 1.18
            else:
                if to == "GBP":
                    rate = 1.36
                else:
                    if to == "JPY":
                        rate = 0.0064
                            else:
                                if to == "CAD":
                                    rate = 0.73
                                        else:
                                            rate = 1
    else:
        if frm == "EUR":
            if to == "USD":
                rate = 0.85
            else:
                if to == "EUR":
                    rate = 1
                else:
                    if to == "GBP":
                        rate = 1.15
                    else:
                        if to == "JPY":
                            rate = 0.54
                        else:
                            if to == "CAD":
                                rate = 0.62
                            else:
                                rate = 1
    else:
        if frm == "GBP":
            if to == "USD":
                rate = 0.74
            else:
                if to == "EUR":
                    rate = 0.87
                else:
                    if to == "GBP":
                        rate = 1
                    else:
                        if to == "JPY":
                            rate = 0.47
                        else:
                            if to == "CAD":
                                rate = 0.54
                            else:
                                rate = 1
    else:
        if frm == "JPY":
            if to == "USD":
                rate = 157.05
            else:
                if to == "EUR":
                    rate = 185.47
                else:
                    if to == "GBP":
                        rate = 213.59
                    else:
                        if to == "JPY":
                            rate = 1
                        else:
                            if to == "CAD":
                                rate = 115.12
                            else:
                                rate = 1
    else:
        if frm == "CAD":
            if to == "USD":
                rate = 1.36
            else:
                if to == "EUR":
                    rate = 1.61
                else:
                    if to == "GBP":
                        rate = 1.86
                    else:
                        if to == "JPY":
                            rate = 0.0087
                        else:
                            if to == "CAD":
                                rate = 1
                            else:
                                rate = 1
                else:
                    rate = 1



    converted = amount * rate
    result = "Converted Amount: " + str(converted)

    return render_template("Currencytable.html", result=result)


if __name__== '__main__':
    app.run()
