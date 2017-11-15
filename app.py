from flask import Flask, render_template, request
from APIs import Adapter
import os
app = Flask("MyApp", static_folder='static')
#def create_mailing_list():
#    return requests.post(
#        "https://api.mailgun.net/v3/lists",
#        auth=('api', '8824cc46530d7251c20db860bac28e0f'),
#        data={'address': 'LIST@sandboxd8902be4c4fb4758bc2650cc7f6dee9d.mailgun.org',
#              'description': "Marketwise newsletter list"})

#def add_list_member(address, name, region, asset):
#    return requests.post(
#        "https://api.mailgun.net/v3/lists/LIST@sandboxd8902be4c4fb4758bc2650cc7f6dee9d.mailgun.org/members",
#        auth=('api', 'key-8824cc46530d7251c20db860bac28e0f'),
#        data={'subscribed': True,
#              'address': '<address>',
#              'name': '<name>',
#              'description': 'Member',
#              'vars': '{"interests": <region> <asset>}'})

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
    return render_template("northamerica.html", entries = Adapter.final_adapter('"north america"',3) )

@app.route("/southamerica")
def southamerica():
    return render_template("southamerica.html", entries = Adapter.final_adapter('"south america"',3))

@app.route("/europe")
def europe():
    return render_template("europe.html", entries = Adapter.final_adapter('"europe"',3))

@app.route("/africa")
def africa():
    return render_template("africa.html", entries = Adapter.final_adapter('"africa"',3))

@app.route("/asia")
def asia():
    return render_template("asia.html", entries = Adapter.final_adapter('"asia"',3))

@app.route("/australia")
def australia():
    return render_template("australia.html", entries = Adapter.final_adapter('"australia"',3))


if __name__ == '__main__':
    app.run(debug = True)
