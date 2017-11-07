import json
import requests
from os import makedirs
from datetime import date, timedelta
from flask import Flask, render_template, request

MY_API_KEY = "213db595-6e95-4c7a-b51f-98164d13faea"
API_ENDPOINT_EQ = 'http://content.guardianapis.com/search?section=business&order-by=newest&q=equity' #changed to get relevant results
my_params = {
    'from-date': "",
    'to-date': "",
    'order-by': "newest",
    'show-fields': 'trailText', #changed from all to only get the article abstract/summary
    'page-size': 200,
    'api-key': MY_API_KEY
}

# day iteration from here:
# http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates
start_date = date(2017, 11, 3) #date.today() - timedelta(1)
end_date = date(2017, 11, 7) #date.today()
dayrange = range((end_date - start_date).days + 1)
for daycount in dayrange:
    dt = start_date + timedelta(days=daycount)
    datestr = dt.strftime('%Y-%m-%d')
    my_params['from-date'] = datestr
    my_params['to-date'] = datestr

    current_page = 1
    total_pages = 1
    while current_page <= total_pages:
        my_params['page'] = current_page
        resp = requests.get(API_ENDPOINT_EQ, my_params)
        data = resp.json()
        x = data['response']['results']
        if len(x) > 1:
            for key, value in x[0].items():
                if key == "webUrl":
                    u = value #"URL: ",
                if key == "webTitle":
                    t = value #"Title: ",
                if key == "fields":
                    f = value
                    for key, value in f.items():
                        s = value #"Summary: ",
                if key == "webPublicationDate":
                    d = value #"Published on: ",



        current_page += 1
        total_pages = data['response']['pages']


app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("homepage.html")

@app.route("/equity")
def equity():
    return render_template("equity.html", title=t, summary=s, date=d, url=u)

app.run(debug = True)
