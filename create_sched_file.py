from flask import Flask, render_template, request
import os

app = Flask(__name__)

# create folder (same idea as tutorial 2)
checknotes = os.path.join('static', 'notes')
if not os.path.exists(checknotes):
    os.makedirs(checknotes)

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

    # file names (like tutorial 2)
    file1 = "StudentInformation.txt"
    file2 = "StudentSchedule.txt"

    # create StudentInformation file
    info_file = os.path.join(checknotes, file1)
    with open(info_file, 'w') as f:
        f.write("Student Information\n")
        f.write("Full Name: " + namefull + "\n")
        f.write("OSIS ID: " + osisid)

    # create StudentSchedule file
    sched_file = os.path.join(checknotes, file2)
    with open(sched_file, 'w') as f:
        f.write("Student Schedule\n")
        f.write("Full Name: " + namefull + "\n")
        f.write("OSIS ID: " + osisid + "\n\n")

        f.write("Schedule:\n")
        f.write("Period 1: " + pdone + "\n")
        f.write("Period 2: " + pdtwo + "\n")
        f.write("Period 3: " + pdthree + "\n")
        f.write("Period 4: " + pdfour + "\n")
        f.write("Period 5: " + pdfive + "\n")
        f.write("Period 6: " + pdsix + "\n")
        f.write("Period 7: " + pdseven + "\n")
        f.write("Period 8: " + pdeight + "\n")

    return render_template("scheduleclass3.html",
                           namefull=namefull,
                           osisid=osisid,
                           schedule=schedule,
                           file1=file1,
                           file2=file2)

@app.route('/bell')
def BellInfo():
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
    return render_template('scheduleclass4.html', bellinfo=bellinfo)

if __name__ == "__main__":
    app.run()
