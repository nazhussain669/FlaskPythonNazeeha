from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    SendInfo();
    return render_template('studentinfotable1.html', #populate the dropdowns in the html
                           schools=schools,
                           programs=programs,
                           paths=paths) 
@app.route('/')
def SendInfo():

    global schools
    global programs
    global paths

    schools = ["", "Hillcrest High School"]

    programs = ["", "CTE", "Non CTE"]

    paths = ["", "CAD - Computer Aided-Design",
             "CNA - Certified Nursing Assisting",
             "EMS - Emergency Medical Services",
             "SWE - Software Engineering",
             "VE - Virtual Enterprise/Entrepreneur"]

@app.route('/output')
def CollectInfo():

    fname = request.args.get("fname")
    midinit = request.args.get("midinit")
    lname = request.args.get("lname")
    bday = request.args.get("bday")
    id = request.args.get("id")
    school = request.args.get("school")
    program = request.args.get("program")
    path = request.args.get("path")

    if fname:
        fullname = fname + " " + midinit + " " + lname
    else:
        fullname = "invalid"
        

    return render_template("studentinfotable2.html",
                           fullname=fullname,
                           lname=lname,
                           bday=bday,
                           id=id,
                           school=school,
                           program=program,
                           path=path)

if __name__ == "__main__":
    app.run()
