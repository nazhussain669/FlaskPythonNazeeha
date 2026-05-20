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
        fcreate.write("Account Number: " + accountnum + "\n")
        fcreate.write("Account Type: " + accounttype + "\n")
        fcreate.write("Current Balance: " + balance + "\n")
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
    pin = request.args.get("pin")

    bankingfile = accnum + "_banking.txt"
    bankingpath = os.path.join(checkfiles, bankingfile)

    if os.path.exists(bankingpath):

        with open(bankingpath, 'r') as fread:
            lines = fread.readlines() # reads all lines from the banking file and stores them into a list

        personalfile = accnum + "_personal.txt"
        personalpath = os.path.join(checkfiles, personalfile)

        with open(personalpath, 'r') as fread:
            personallines = fread.readlines() # reads all lines from the personal file and stores them into a list

        savedpin = personallines[6] # gets the PIN from the seventh line in the personal file

        if savedpin == "PIN: " + pin + "\n":

            balance = float(lines[2]) # gets the balance from the third line in the banking file

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
                fcreate.write(transtype + " $" + str(amount))

        else:
            message = "Incorrect PIN"
            balance = 0

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

        username = personalinfo[4] # gets the username from line 5 in the personal file
        password = personalinfo[5] # gets the password from line 6 in the personal file
        pin = personalinfo[6] # gets the PIN from line 7 in the personal file

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
