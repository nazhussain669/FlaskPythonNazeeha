from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('url_for_loops.html')

@app.route('/output')
def CollectInfo():
    courselist=[]
    courselist = ["Calculus", "Science", "History"]
    return render_template("url_for_loop_out.html", courses=courselist)

if __name__ == "__main__":
    app.run()
                  
