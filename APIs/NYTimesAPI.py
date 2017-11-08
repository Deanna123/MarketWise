#from flask import Flask, render_template, request
from datetime import date, timedelta
from nytimesarticle import articleAPI

#else:
#    today == yesterday
#    yesterday = date.today() - timedelta(2)
def get_article():
     adapter = []
     api = articleAPI("522e4e6f593d44baaf69a87cdff70548")

     today = date.today()
     yesterday = date.today() - timedelta(1)
     articles = api.search( q = 'equity', begin_date = yesterday.strftime('%Y%m%d'), end_date = today.strftime('%Y%m%d'), sort = 'newest', fl = ['web_url','snippet','headline','pub_date'])
     x = articles['response']['docs']
     #import pprint
     #pprint.pprint(articles)
     if len(x) > 1:
         #add loop here for multiple articles
         arts = x[0]
         adapDict = {}
         for key, value in articles.items():
             adapDict['Source'] = 'Times'
             adapDict['URL'] = arts['web_url']
             adapDict['Title'] = arts['headline']['main']
             adapDict['Summary'] = arts['snippet']
         adapter.append(adapDict)
     return adapter
#print get_article()
