from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('url_for.html')

@app.route('/output')
def CollectInfo():
    global fullname
    fullname = ""

    firstname = request.args.get("txtfirstname")
    lastname = request.args.get("txtlastname")
    midinit = request.args.get("txtmidinit")

    if (midinit == ""):
        fullname = firstname + " " + lastname
    else:
        fullname = firstname + " " + midinit + ". " + lastname

    return render_template("url_for_out.html", fullname=fullname)

if __name__ == "__main__":
    app.run()
