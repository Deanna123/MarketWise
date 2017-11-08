import json
import requests
from os import makedirs
from datetime import date, timedelta

def get_article():
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
    end_date =  date(2017, 11, 7) #date.today()
    dayrange = range((end_date - start_date).days + 1)
    adapter = []

    for daycount in dayrange:
        dt = start_date + timedelta(days=daycount)
        datestr = dt.strftime('%Y-%m-%d')
        my_params['from-date'] = datestr
        my_params['to-date'] = datestr

    #    entries.append('test')
        current_page = 1
        total_pages = 1
        while current_page <= total_pages:
            my_params['page'] = current_page
            resp = requests.get(API_ENDPOINT_EQ, my_params)
            data = resp.json()
            x = data['response']['results']
            import pprint
            #pprint.pprint( x[0].items())
            if len(x) > 1:
                articles = x[0]
                adapDict = {}
                for key, value in articles.items():
                    adapDict['URL'] = articles['webUrl']
                    adapDict['Title'] = articles['webTitle']
                    adapDict['Summary'] = articles['fields']['trailText']
                adapter.append(adapDict)

                #    if key == "webUrl":
                #        urlGuardian = value #"URL: ",
                #    if key == "webTitle":
                        #print value
                #        entries.append(value)
                        #print entries
                #        headlineGuardian = value #"Title: ",
                #    if key == "fields":
                #        f = value
                #        for key, value in f.items():
                #            summaryGuardian = value #"Summary: ",
                #    if key == "webPublicationDate":
                #        dateGuardian = value #"Published on: ",
        # need to work out what happens with no articles, simplify dates
        #   else:



            current_page += 1
            total_pages = data['response']['pages']
        return adapter
    #print entries
