import json
import requests
from os import makedirs
from datetime import date, timedelta
import pprint

def get_article(region, number):
    query = region + ' AND ("market" OR "asset") AND ("bonds" OR "commodity" OR "currency" OR "equity" OR "property")'
    MY_API_KEY = "213db595-6e95-4c7a-b51f-98164d13faea"
    API_ENDPOINT_EQ = 'http://content.guardianapis.com/search?section=business&order-by=newest&q='+query
    my_params = {
        'from-date': "",
        'to-date': "",
        'order-by': "newest",
        'show-fields': 'trailText,thumbnail', #changed from all to only get the article abstract/summary
        'page-size': 200,
        'api-key': MY_API_KEY
    }

    # day iteration from here:
    # http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates
    start_date = date(2014, 1, 1)
    end_date =  date.today()
    my_params['from-date'] = start_date.strftime('%Y-%m-%d')
    my_params['to-date'] = end_date.strftime('%Y-%m-%d')

    adapter = []

    current_page = 1
    total_pages = 1
    while current_page <= total_pages:
        my_params['page'] = current_page
        resp = requests.get(API_ENDPOINT_EQ, my_params)
        data = resp.json()
        articles = data['response']['results'][0:number]
        #print articles
        for article in articles:
            adapDict = {}
            for key, value in article.items():
                adapDict['Source'] = 'Guardian'
                adapDict['URL'] = article['webUrl']
                adapDict['Title'] = article['webTitle']
                adapDict['Summary'] = article['fields']['trailText']
                adapDict['Published on'] = article['webPublicationDate']
                if len(article['multimedia'])>0:
                    adapDict['Thumbnail'] = article['fields']['thumbnail']
                else:
                    adapDict['Thumbnail'] = 'http://fontslogo.com/wp-content/uploads/2013/03/The-Guardian-Logo-Font.jpg'


            adapter.append(adapDict)

            current_page += 1
            total_pages = data['response']['pages']
        return adapter

#pprint.pprint(get_article("south america", 3))
#pprint.pprint(get_article('equities "south america"'))
