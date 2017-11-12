from datetime import date, timedelta
import requests
import pprint

def get_article(query):
    API_key = "522e4e6f593d44baaf69a87cdff70548"
    today = date.today()
    prev_date = date(2014, 1, 1)
    API_endpoint = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+query+"&begin_date="+prev_date.strftime('%Y%m%d')+"&end_date="+today.strftime('%Y%m%d')+"&api-key=522e4e6f593d44baaf69a87cdff70548"


    results = requests.get(API_endpoint)
    data = results.json()
    articles = data['response']['docs'][0:3]

    adapter = []

    for article in articles:
        adapDict = {}
        for key, value in article.items():
             adapDict['Source'] = 'Times'
             adapDict['URL'] = article['web_url']
             adapDict['Title'] = article['headline']['main']
             adapDict['Summary'] = article['snippet']
             adapDict['Published on'] = article['pub_date']
        adapter.append(adapDict)
    return adapter
#pprint.pprint(get_article("assets AND europe"))
