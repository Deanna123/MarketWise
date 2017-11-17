#Marketwise

Marketwise was a group project created as part of the Code First: Girls Advanced Python Community Course. 
We wanted to create a financial news website that provides short snippets of the latest news stories relating to markets and assets specific to each region.

Using Python, HTML and CSS, we created a Flask app, which is [deployed on Heroku](https://lit-everglades-83313.herokuapp.com/).


##How it works

###APIs
We used the [Guardian API](http://open-platform.theguardian.com/) and the [New York Times Article Search API](https://developer.nytimes.com/article_search_v2.json).

For the Guardian API, we found an incredibly helpful [Python script](https://gist.github.com/dannguyen/c9cb220093ee4c12b840), which we edited to suit our needs and to pull relevant information.
For the NYTimes API, we initially used the [nytimesarticle package](https://pypi.python.org/pypi/nytimesarticle/0.1.0), however once we deployed it on heroku, the app stopped working. 
So instead we used our script for the Guardian API as a guide to create a similar script for the NYTimes.

###How we used the APIs

Both scripts search the business section of each news site for a chosen number of articles, for our app we used 3, that match the following:
* Region name i.e Africa, Asia, Austrailia, Europe, North America or South America
* Market OR Asset
* Asset types i.e. Bonds, Commodity, Currency, Equity OR property

From each article, the scripts create a dictionary with the following information:
* Source i.e Guardian or NYTimes
* URL
* Title
* Summary
* Date it was published
* Thumbnail URL
	* If the article doesn't have a thumbnail, this defaults to the source's logo

We then used an _Adapter_, which takes the dictionaries from both scripts and combines them. 
This new dictionary is imported into our Flask app and the entries are combined with the HTML templates to create our webpages.


###Limitations
Since we only had 4 weeks to complete this project, there are a few things we didn't have enough time for/was beyond our scope:

* Creating a working contact us page, newsletter (we were hoping to use Mailgun) and search bar
* Overall polishing of the code - commenting, condensing the app using functions, using iteration to search for articles
* Better use of CSS


##The team
* [Deanna](https://github.com/Deanna123)
*[Najma](https://github.com/codenajma)
*[Ninamma](https://github.com/ASTG17)