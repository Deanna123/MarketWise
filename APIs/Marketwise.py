from flask import Flask, render_template, request
import Adapter
app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("homepage.html")

@app.route("/equity")
def equity():
    return render_template("equity.html", entries = Adapter.final_adapter)

app.run(debug = True)
