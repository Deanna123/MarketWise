import json
import requests
from os import makedirs
from datetime import date, timedelta
import pprint


def get_article(query):
    MY_API_KEY = "213db595-6e95-4c7a-b51f-98164d13faea"
    API_ENDPOINT_EQ = 'http://content.guardianapis.com/search?section=business&order-by=newest&q='+query
    start_date = date.today() - timedelta(1)
    end_date =  date.today()
    my_params = {
        'from-date': "",
        'to-date': "",
        'order-by': "newest",
        'show-fields': 'trailText', #changed from all to only get the article abstract/summary
        'page-size': 200,
        'api-key': MY_API_KEY
    }

    current_page = 1
    adapter = []

    my_params['from-date'] = start_date.strftime('%Y-%m-%d')
    my_params['to-date'] = end_date.strftime('%Y-%m-%d')
    my_params['page'] = current_page

    resp = requests.get(API_ENDPOINT_EQ, my_params)
    data = resp.json()
    total_pages = data['response']['pages']
    x = data['response']['results']

    while current_page <= total_pages:
        for i in x:
            articles = i
            adapDict = {}
            while len(adapter) < 3:
                for key, value in articles.items():
                    adapDict['URL'] = articles['webUrl']
                    adapDict['Title'] = articles['webTitle']
                    adapDict['Summary'] = articles['fields']['trailText']
                    adapDict['Published on'] = articles['webPublicationDate']
                adapter.append(adapDict)
                current_page += 1
    return adapter
get_arts()

#    while len(adapter) < 3:
#
#        dayrange = range((end_date - start_date).days + 1)
#        print dayrange
#        for day in dayrange:


pprint.pprint (get_article('equity AND europe'))
