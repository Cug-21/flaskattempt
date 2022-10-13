from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "Cuggo"

@app.route("/hello")
def index():
    flash("Whats your name loserr?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you")
    request.form['name_input']
    return render_template("index.html")
