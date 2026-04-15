from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('scheduleclass1.html')

@app.route('/input')
def Grab():
    return render_template('scheduleclass2.html')

@app.route('/output')
def CollectInfo():

    namefull = request.args.get("fullname")
    osisid = request.args.get("osis")
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
                           namefull=namefull,
                           osisid=osisid,
                           schedule=schedule)

@app.route('/bell')
def BellInfo():
    bellinfo = []

    bellinfo = [
        {"Period": 1, "Start": "8:05 am", "End": "8:51 am"},
        {"Period": 2, "Start": "8:55 am", "End": "9:41 am"},
        {"Period": 3, "Start": "9:45 am", "End": "10:33 am"},
        {"Period": 4, "Start": "10:37 am", "End": "11:23 am"},
        {"Period": 5, "Start": "11:27 am", "End": "12:13 pm"},
        {"Period": 6, "Start": "12:17 pm", "End": "1:03 pm"},
        {"Period": 7, "Start": "1:07 pm", "End": "1:53 pm"},
        {"Period": 8, "Start": "1:57 pm", "End": "2:43 pm"},
        ]
    return render_template('scheduleclass4.html',bellinfo=bellinfo)

if __name__ == "__main__":
    app.run()
