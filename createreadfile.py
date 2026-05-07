from flask import Flask, render_template, request, url_for
import os

app=Flask(__name__)

checknotes = os.path.join('static','notes')
if not os.path.exists(checknotes):
    os.makedirs(checknotes)

@app.route('/')
def index():
    return render_template('indexfile.html')

@app.route('/createfile', methods=['POST'])
def Filecreation():
    CheckFile()
    return render_template('outputfile.html', fileinfo=savedinfo, filename=filename)

def CheckFile():
    global filename
    global savedinfo

    filename = request.form.get("txtfilename")
    filename = filename + ".txt"
    filepath = os.path.join(checknotes,filename)

    if os.path.exists(filepath):
        with open(filepath, 'r') as fread:
            savedinfo = fread.read()
        print("Found")
    else:
        information = "hello. this is the file i created"
        with open(filepath, 'w') as fcreate:
            fcreate.write(information)
        with open(filepath, 'r') as fread:
            savedinfo = fread.read()

    print(savedinfo)

if __name__ == "__main__":
    app.run()
