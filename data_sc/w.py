"""import urllib
import urllib2
import sys 
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import re
from random import randint
import time
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import csv 
from selenium import webdriver
import mechanize

#url1="http://us.rd.yahoo.com/dailynews/rss/weather/College_Station__TX/*http://weather.yahoo.com/forecast/USTX0270_f.html"
city=raw_input("enter location: ")
state=raw_input("enter state: ")
city=city.replace(" ","%20")
state.replace(" ","%20")
url="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22"+city+"%2C%20"+state+"%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

print url
page=urllib2.urlopen(url)
content=page.read()
print content
"""

import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid=2370857"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
#print yql_url
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
print data['query']['results']['channel']['item']['title']+"  "+ "lat:"+data['query']['results']['channel']['item']['lat']+ " long:"+ data['query']['results']['channel']['item']['long']

#for i in  data['query']['results']['channel']['item']['condition']:
#	print  i+"  "+data['query']['results']['channel']['item']['condition'][i]


 
print data['query']['results']['channel']['item']['description']

