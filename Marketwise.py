from flask import Flask, render_template, request
from APIs import Adapter
app = Flask("MyApp")

@app.route("/")
def home():
    return render_template("index.html")

#@app.route("/about") #maybe we could make an about the site/about us page?
#def about():
#    return render_template("about.html")

#@app.route("/newsletter") #page for making a signup page for relevant newsletters with mailgun?
#def news():
#    return render_template("newsletter.html")

@app.route("/northamerica")
def northamerica():
    return render_template("northamerica.html", entries = Adapter.final_adapter('assets AND "north america"'))

@app.route("/southamerica")
def southamerica():
    return render_template("southamerica.html", entries = Adapter.final_adapter('assets AND "south america"'))

@app.route("/europe")
def europe():
    return render_template("europe.html", entries = Adapter.final_adapter('assets AND europe'))

@app.route("/africa")
def africa():
    return render_template("africa.html", entries = Adapter.final_adapter('assets AND africa'))

@app.route("/asia")
def asia():
    return render_template("asia.html", entries = Adapter.final_adapter('assets AND asia'))

@app.route("/australia")
def australia():
    return render_template("australia.html", entries = Adapter.final_adapter('assets AND australia'))

app.run(debug = True)
