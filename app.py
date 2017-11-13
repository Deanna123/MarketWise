from flask import Flask, render_template, request
from APIs import Adapter
import os
app = Flask("MyApp", static_folder='static')
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about") #maybe we could make an about the site/about us page?
def about():
    return render_template("about.html")

@app.route("/newsletter") #page for making a signup page for relevant newsletters with mailgun?
def news():
    return render_template("newsletter.html")

@app.route("/northamerica")
def northamerica():
    return render_template("northamerica.html", entries = Adapter.final_adapter('bonds AND "north america"',1) + Adapter.final_adapter('commodity AND "north america"',1) + Adapter.final_adapter('currency AND "north america"',1) + Adapter.final_adapter('equity AND "north america"',1) + Adapter.final_adapter('property AND "north america"',1))

@app.route("/southamerica")
def southamerica():
    return render_template("southamerica.html", entries = Adapter.final_adapter('bonds AND "south america"',1) + Adapter.final_adapter('commodity AND "south america"',1) + Adapter.final_adapter('currency AND "south america"',1) + Adapter.final_adapter('equity AND "south america"',1) + Adapter.final_adapter('property AND "south america"',1))

@app.route("/europe")
def europe():
    return render_template("europe.html", entries = Adapter.final_adapter('bonds AND europe',1) + Adapter.final_adapter('commodity AND europe',1) + Adapter.final_adapter('currency AND europe',1) + Adapter.final_adapter('equity AND europe',1) + Adapter.final_adapter('property AND europe',1))

@app.route("/africa")
def africa():
    return render_template("africa.html", entries = Adapter.final_adapter('bonds AND africa',1) + Adapter.final_adapter('commodity AND africa',1) + Adapter.final_adapter('currency AND africa',1) + Adapter.final_adapter('equity AND africa',1) + Adapter.final_adapter('property AND africa',1))

@app.route("/asia")
def asia():
    return render_template("asia.html", entries = Adapter.final_adapter('bonds AND asia',1) + Adapter.final_adapter('commodity AND asia',1) + Adapter.final_adapter('currency AND asia',1) + Adapter.final_adapter('equity AND asia',1) + Adapter.final_adapter('property AND asia',1))

@app.route("/australia")
def australia():
    return render_template("australia.html", entries = Adapter.final_adapter('bonds AND australia',1) + Adapter.final_adapter('commodity AND australia',1) + Adapter.final_adapter('currency AND australia',1) + Adapter.final_adapter('equity AND australia',1) + Adapter.final_adapter('property AND australia',1))


if __name__ == '__main__':
    app.run(debug = True)
