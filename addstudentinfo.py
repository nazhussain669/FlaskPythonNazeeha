from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('student_info.html')

@app.route('/output')
def CollectInfo():

    fname = request.args.get("fname")
    lname = request.args.get("lname")
    bday = request.args.get("bday")
    id = request.args.get("id")
    school = request.args.get("school")
    program = request.args.get("program")
    path = request.args.get("path")

    if (fname == ""):
        fname = "No First Name"
    else:
        fname = fname

    if (lname == ""):
        lname = "No Last Name"
    else:
        lname = lname

    if (bday == ""):
        bday = "No Birth Date"
    else:
        bday = bday

    if (id == ""):
        id = "No OSIS ID"
    else:
        id = id

    return render_template("student_out.html",
                           fname=fname,
                           lname=lname,
                           bday=bday,
                           id=id,
                           school=school,
                           program=program,
                           path=path)

if __name__ == "__main__":
    app.run()
