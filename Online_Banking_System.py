from flask import Flask, render_template, request
import os

app = Flask(__name__)

checkfiles = os.path.join('static', 'bankfiles')

if not os.path.exists(checkfiles):
    os.makedirs(checkfiles)

@app.route('/')
def index():
    return render_template('onlinebanking1.html')

@app.route('/create')
def CreateAccount():
    return render_template('onlinebanking2.html')

@app.route('/output')
def Output():

    fullname = request.args.get("fullname")
    age = request.args.get("age")
    email = request.args.get("email")
    accountnum = request.args.get("accountnum")
    accounttype = request.args.get("accounttype")
    balance = request.args.get("balance")
    username = request.args.get("username")
    password = request.args.get("password")

    personalfile = accountnum + "_personal.txt"
    bankingfile = accountnum + "_banking.txt"

    personalpath = os.path.join(checkfiles, personalfile)

    with open(personalpath, 'w') as fcreate:
        fcreate.write("CUSTOMER PERSONAL INFORMATION\n")
        fcreate.write("Full Name: " + fullname + "\n")
        fcreate.write("Age: " + age + "\n")
        fcreate.write("Email: " + email + "\n")
        fcreate.write("Username: " + username + "\n")
        fcreate.write("Password: " + password + "\n")

    bankingpath = os.path.join(checkfiles, bankingfile)

    with open(bankingpath, 'w') as fcreate:
        fcreate.write("BANK ACCOUNT INFORMATION\n")
        fcreate.write("Account Number: " + accountnum + "\n")
        fcreate.write("Account Type: " + accounttype + "\n")
        fcreate.write("Current Balance: $" + balance + "\n")
        fcreate.write("Recent Transaction: Account Created\n")

    return render_template('onlinebanking3.html',
                           fullname=fullname,
                           age=age,
                           email=email,
                           accountnum=accountnum,
                           accounttype=accounttype,
                           balance=balance,
                           username=username,
                           personalfile=personalfile,
                           bankingfile=bankingfile)

@app.route('/retrieve')
def Retrieve():
    return render_template('onlinebanking4.html')

@app.route('/view')
def ViewFiles():

    accountnum = request.args.get("accountnum")

    personalfile = accountnum + "_personal.txt"
    bankingfile = accountnum + "_banking.txt"

    personalpath = os.path.join(checkfiles, personalfile)
    bankingpath = os.path.join(checkfiles, bankingfile)

    if os.path.exists(personalpath):
        with open(personalpath, 'r') as fread:
            personalinfo = fread.read()
    else:
        personalinfo = "Personal file not found."

    if os.path.exists(bankingpath):
        with open(bankingpath, 'r') as fread:
            bankinginfo = fread.read()
    else:
        bankinginfo = "Banking file not found."

    return render_template('onlinebanking5.html',
                           personalinfo=personalinfo,
                           bankinginfo=bankinginfo,
                           personalfile=personalfile,
                           bankingfile=bankingfile)

if __name__ == "__main__":
    app.run()
