from flask import Flask, render_template, request, url_for
import os

app=Flask(__name__)

checknotes = os.path.join('static','notes')
if not os.path.exists(checknotes):
    os.makedirs(checknotes)

@app.route('/')
def index():
    return render_template('fileindex.html')

@app.route('/createfile', methods=['POST'])
def FileCreation():
    information = "Hello. This is the file i created"
    filename = request.form.get("txtfilename")
    filename = filename + ".txt"
    filepath = os.path.join(checknotes,filename)

    with open(filepath, 'w') as fcreate:
        fcreate.write(information)

    return render_template('fileoutput.html',filename=filename)

if __name__== "__main__":
    app.run()
