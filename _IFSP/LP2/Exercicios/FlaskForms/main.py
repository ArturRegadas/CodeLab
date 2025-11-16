from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/ans", methods = ["POST"])
def ans():
    name = request.form.get("name")
    age = request.form.get("age")
    return render_template("ans.html", name=name, age=age)

app.run()