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
    pin = request.args.get("pin")

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
        fcreate.write("PIN: " + pin + "\n")

    bankingpath = os.path.join(checkfiles, bankingfile)

    with open(bankingpath, 'w') as fcreate:
        fcreate.write(accountnum + "\n")
        fcreate.write(accounttype + "\n")
        fcreate.write(balance + "\n")
        fcreate.write("Account Created")

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

@app.route('/login')
def LogIn():
    return render_template('onlinebanking6.html')

@app.route('/transact')
def MakeTransaction():

    accnum = request.args.get("accnum")
    accounttype = request.args.get("accounttype")
    transtype = request.args.get("transtype")
    amount = request.args.get("amount")

    bankingfile = accnum + "_banking.txt"
    bankingpath = os.path.join(checkfiles, bankingfile)

    if os.path.exists(bankingpath):

        with open(bankingpath, 'r') as fread:
            lines = fread.readlines()

        balance = float(lines[2]) # lines[2] means the third line because counting starts at 0

        amount = float(amount)

        if transtype == "DEPOSIT":
            balance = balance + amount

        elif transtype == "WITHDRAWAL":
            balance = balance - amount

        with open(bankingpath, 'w') as fcreate:
            fcreate.write(accnum + "\n")
            fcreate.write(accounttype + "\n")
            fcreate.write(str(balance) + "\n")
            fcreate.write(transtype + " $" + str(amount))

    return render_template('onlinebanking7.html',
                           accnum=accnum,
                           accounttype=accounttype,
                           transtype=transtype,
                           amount=amount,
                           balance=balance)

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

@app.route('/forgot')
def ForgotPassword():
    return render_template('onlinebanking8.html')

@app.route('/recover')
def RecoverPassword():

    accountnum = request.args.get("accountnum")

    personalfile = accountnum + "_personal.txt"

    personalpath = os.path.join(checkfiles, personalfile)

    if os.path.exists(personalpath):

        with open(personalpath, 'r') as fread:
            personalinfo = fread.readlines()

        username = personalinfo[4]
        password = personalinfo[5]
        pin = personalinfo[6]

    else:
        username = "Account Not Found"
        password = "Account Not Found"
        pin = "Account Not Found"

    return render_template('onlinebanking9.html',
                           username=username,
                           password=password,
                           pin=pin,
                           accountnum=accountnum)

if __name__ == "__main__":
    app.run()
