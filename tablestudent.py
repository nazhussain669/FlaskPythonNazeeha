from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    schools = ["Hillcrest High School"]

    programs = ["CTE", "Non CTE"]

    paths = ["CAD - Computer Aided-Design",
             "CNA - Certified Nursing Assisting",
             "EMS - Emergency Medical Services",
             "SWE - Software Engineering",
             "VE - Virtual Enterprise/Entrepreneur"]

    return render_template('tablestudent1.html',
                           schools=schools,
                           programs=programs,
                           paths=paths)

@app.route('/output')
def CollectInfo():

    fname = request.args.get("fname")
    mname = request.args.get("mname")
    lname = request.args.get("lname")
    bday = request.args.get("bday")
    id = request.args.get("id")
    school = request.args.get("school")
    program = request.args.get("program")
    path = request.args.get("path")

    if fname:
        fullname = fname + " " + mname + ". " + lname
    else:
        fullname = "invalid"

    student = {
        "id": id,
        "name": fullname,
        "bday": bday,
        "school": school,
        "program": program,
        "path": path
    }

    return render_template("tablestudent2.html",
                           student=student)

if __name__ == "__main__":
    app.run()
