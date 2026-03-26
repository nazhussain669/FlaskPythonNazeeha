from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('scheduleclass1.html')

@app.route('/output')
def Grab():
    return render_template('scheduleclass2.html')

@app.route('/final')
def CollectInfo():

    pdone = request.args.get("one")
    pdtwo = request.args.get("two")
    pdthree = request.args.get("three")
    pdfour = request.args.get("four")
    pdfive = request.args.get("five")
    pdsix = request.args.get("six")
    pdseven = request.args.get("seven")
    pdeight = request.args.get("eight")

    schedule = [
        {"period": "1", "course": pdone},
        {"period": "2", "course": pdtwo},
        {"period": "3", "course": pdthree},
        {"period": "4", "course": pdfour},
        {"period": "5", "course": pdfive},
        {"period": "6", "course": pdsix},
        {"period": "7", "course": pdseven},
        {"period": "8", "course": pdeight},
    ]

    return render_template("scheduleclass3.html",
                           schedule=schedule)

if __name__ == "__main__":
    app.run()
