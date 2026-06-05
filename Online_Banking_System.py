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

    if int(age) < 16:
        return render_template("onlinebanking2.html",
                           message="Age must be at least 16.")

    if len(accountnum) != 7:
        return render_template("onlinebanking2.html",
                           message="Account Number must be exactly 7 digits.")

    if float(balance) < 50:
        return render_template("onlinebanking2.html",
                           message="Starting Balance must be at least $50.")

    if len(pin) != 4:
        return render_template("onlinebanking2.html",
                           message="PIN must be exactly 4 digits.")

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
        fcreate.write("Recent Activity: " + "Account Created")

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
    pin = request.args.get("pin")

    if len(accnum) != 7:
        return render_template("onlinebanking6.html",
                           message="Account Number must be exactly 7 digits.")

    if len(pin) != 4:
        return render_template("onlinebanking6.html",
                           message="PIN must be exactly 4 digits.")

    if float(amount) < 20:
        return render_template("onlinebanking6.html",
                           message="Transaction amount must be at least $20.")

    bankingfile = accnum + "_banking.txt"
    bankingpath = os.path.join(checkfiles, bankingfile)

    foundaccount = os.path.exists(bankingpath)

    if foundaccount:

        with open(bankingpath, 'r') as fread:
            lines = fread.readlines()

        personalfile = accnum + "_personal.txt"
        personalpath = os.path.join(checkfiles, personalfile)

        with open(personalpath, 'r') as fread:
            personallines = fread.readlines()

        # gets the PIN from line 7 in the personal file
        savedpin = personallines[6]

        if savedpin == "PIN: " + pin + "\n":

            # gets the balance from line 3 in the banking file
            balance = float(lines[2])

            amount = float(amount)

            if transtype == "DEPOSIT":
                balance = balance + amount
                message = "Deposit Successful"

            else:

                if amount > balance:
                    message = "Not Enough Money"

                else:
                    balance = balance - amount
                    message = "Withdrawal Successful"

            with open(bankingpath, 'w') as fcreate:
                fcreate.write(accnum + "\n")
                fcreate.write(accounttype + "\n")
                fcreate.write(str(balance) + "\n")
                fcreate.write("Recent Activity: " + transtype + " $" + str(amount))

        else:
            message = "Incorrect PIN"

            # gets the balance from line 3 in the banking file
            balance = lines[2]

    else:
        message = "Account Not Found"
        balance = 0

    return render_template('onlinebanking7.html',
                           accnum=accnum,
                           accounttype=accounttype,
                           transtype=transtype,
                           amount=amount,
                           balance=balance,
                           message=message)

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

    foundpersonal = os.path.exists(personalpath)
    foundbanking = os.path.exists(bankingpath)

    if foundpersonal:
        with open(personalpath, 'r') as fread:
            personalinfo = fread.read()
    else:
        personalinfo = "Personal file not found."

    if foundbanking:
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

    foundpersonal = os.path.exists(personalpath)

    if foundpersonal:

        with open(personalpath, 'r') as fread:
            personalinfo = fread.readlines()

        # gets the username from line 5 in the personal file
        username = personalinfo[4]

        # gets the password from line 6 in the personal file
        password = personalinfo[5]

        # gets the PIN from line 7 in the personal file
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
