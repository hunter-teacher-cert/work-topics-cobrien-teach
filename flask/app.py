from flask import Flask, request, session, render_template

import random

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
  ip = request.environ['REMOTE_ADDR']
  return render_template("home.html", ip = ip)

@app.route("/coolsite",methods=['GET','POST'])
def coolsite():
    message = ""
    if request.method=="GET":
        return render_template("coolsite.html")

    else:
        choice = request.form['choice']
        if choice =="great":
            message = "We're happy you love the website! If you have any comments  please click this link."
        else:
            message = "We're sorry you don't love the website! If you have any ideas for improvement  please click this link."




        return render_template("coolsite.html", message=message)

@app.route("/comments", methods=['GET', 'POST'])
def comments():

    if request.method=="GET":
        return render_template("comments.html", message="")
    else:
        comment = request.form['comment']

        print(comment)
        message = "Your comment was: '" + comment + "'. Thank you for your feedback!"
        return render_template("comments.html", message=message)

app.run(host="127.0.0.1",port=5000,debug=True)
