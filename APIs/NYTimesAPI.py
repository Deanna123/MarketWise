from datetime import date, timedelta
import requests
import pprint

def get_article(region, number):
    query = region+" AND" + " market OR asset" + " bonds OR commodity OR Currency OR equity OR property"
    API_key = "522e4e6f593d44baaf69a87cdff70548"
    today = date.today()
    prev_date = date(2016, 1, 1)
    API_endpoint = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+query+'&begin_date='+prev_date.strftime('%Y%m%d')+"&end_date="+today.strftime('%Y%m%d')+'&facet_field=section_name&fq=section_name:"business"&api-key=522e4e6f593d44baaf69a87cdff70548'


    results = requests.get(API_endpoint)
    data = results.json()
    articles = data['response']['docs'][0:number]
    adapter = []

    for article in articles:
        adapDict = {}
        #print article['multimedia'][0]
        for key, value in article.items():
             adapDict['Source'] = 'Times'
             adapDict['URL'] = article['web_url']
             adapDict['Title'] = article['headline']['main']
             adapDict['Summary'] = article['snippet']
             adapDict['Published on'] = article['pub_date']
             if len(article['multimedia'])>0:
                 adapDict['Thumbnail'] = 'http://www.nytimes.com/'+article['multimedia'][0]['url']
             else:
                 adapDict['Thumbnail'] = 'https://www.famouslogos.net/images/new-york-times-logo.jpg'
        adapter.append(adapDict)
    return adapter
#pprint.pprint(get_article("north america" ,1))
