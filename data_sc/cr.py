import urllib
import urllib2
import sys 
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import re
from random import randint
import time
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser


count=0
exit=0
days=[]

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
#        print "Start tag:", tag
        for attr in attrs:
	    global count
	    global st
	    global days
	    exit=0
	    for i in attr:
		if i == "checked" and count ==0:
			print "tue"
			days.append("tuesday")
			count=1
			exit=1
			st=1
		elif i == "checked" and count ==1 and exit==0:
			print "wed"
			count=2
			exit=1
			st=1
		elif i == "checked" and count ==2 and exit==0:
			print "golf"
			count=3
			exit=1
			st=1
		elif i == "checked" and count ==3 and exit==0:
			print "dinner"
			count=4
			exit=1
			st=1
           # print "     attr:", attr
    #def handle_endtag(self, tag):
      # print "End tag  :", tag
#    def handle_data(self, data):
#       print "Data     :", data
    #def handle_comment(self, data):
       #print "Comment  :", data
#    def handle_entityref(self, name):
#        c = unichr(name2codepoint[name])
#        print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        #print "Num ent  :", c
    #def handle_decl(self, data):
        #print "Decl     :", data


parser=MyHTMLParser()

url="http://sec.tamu.edu/students/careerfair/Search.aspx?fastOps=0"
page=urllib2.urlopen(url)
content=page.read()
#print content
soup=BeautifulSoup(content)

for entry in soup.find_all('td'):
	s=BeautifulSoup(str(entry))
	#print s
	global count
	global st
	global days
	st=0
	this=0
	if s.a:
		print s.a.contents[0]
		count =0
		this=1
		days=[]
		if str(s.a.contents) =="?":
			st =1
	if parser.feed(str(s)):
		print "<<<<<<<<<<<<<<<<<<"
		#print str(s)
		print "###########"
		print parser.feed(str(s))
		print ">>>>>>>>>>>>>>>>>"
	elif this==0 and st==0:
		print "!!!!!!!!!!!!!!"
		#print str(s)
		print "@@@@@@@@@@@@@"
		count =count +1
	

