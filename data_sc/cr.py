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
import csv
from selenium import webdriver
import mechanize

#"""
count=0
exit=0
days=[]
#tues=[]
#wed=[]
#golf=[]
#dinner=[]

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
#        print "Start tag:", tag
        for attr in attrs:
	    global count
	    global st
	    global days
	    global tues
	    global wed
	    global golf
	    global dinner
	    exit=0
	    for i in attr:
		if i == "checked" and count ==0:
			#print "tue"
			#days.append("tuesday")
			tues=1
			count=1
			exit=1
			st=1
		elif i == "checked" and count ==1 and exit==0:
			#print "wed"
			#days.append("wednesday")
			wed=1
			count=2
			exit=1
			st=1
		elif i == "checked" and count ==2 and exit==0:
			#print "golf"
			#days.append("golf")
			golf=1
			count=3
			exit=1
			st=1
		elif i == "checked" and count ==3 and exit==0:
			#print "dinner"
			#days.append("dinner")
			dinner=1
			count=4
			exit=1
			st=1
	   # print days
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
####################  HTML Parser class ends here #################

parser=MyHTMLParser()
#"""


url="http://sec.tamu.edu/students/careerfair/Search.aspx?fastOps=0"
###############     THE URL ######################


br=mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False) 
response = br.open(url)
#print response.read()      # the text of the page
response1 = br.response()  # get the response again
#print response1.read()
#for form in br.forms():
    #print "Form name:", form.name
    #print form
br.select_form("aspnetForm") 
#for control in br.form.controls:
    #print control
    #print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
day_control = br.form.find_control("ctl00$ctl00$ctl00$MasterMain$Content$Content$ddlDays")
maj_control = br.form.find_control("ctl00$ctl00$ctl00$MasterMain$Content$Content$ddlMajor")
deg_control = br.form.find_control("ctl00$ctl00$ctl00$MasterMain$Content$Content$ddlDegree")
emp_control = br.form.find_control("ctl00$ctl00$ctl00$MasterMain$Content$Content$ddlEmployment")
#if deg_control.type == "select":  # means it's class ClientForm.SelectControl
    #for item in deg_control.items:
    	#print " name=%s values=%s" % (item.name, str([label.text  for label in item.get_labels()]))
#print control.value
#print control  # selected value is starred
day_control.value = ["A"]
maj_control.value = ["7"]   ##7=computer engg     8= computer science     9=electrical engg
deg_control.value = ["M"]  ##M=masters
emp_control.value = ["IC"] ##IC=intern /co-op
#print control
#br[control.name] = ["Tuesday"]  # equivalent and more normal
response = br.submit()
#print response.read()
content=response.read()


###################  CSV generation  after reading web page ############################
#"""
#page=urllib2.urlopen(url)
#content=page.read()
#print content
soup=BeautifulSoup(content,'html5lib')
#print soup
writer1 = csv.writer(open("comp"+".csv", 'wb'))
writer1.writerow(["Companies","Tuesday","Wednesday","Golf","Dinner"])
ccc=0
for entry in soup.find_all('td'):
	s=BeautifulSoup(str(entry))
	#print s
	global count
	global st
	global days
	st=0
	this=0
	if s.a:
		#print s.a.contents[0]
		if str(s.a.contents[0]) != "?":
			comp=s.a.contents[0]
			ccc=ccc+1
		count =0
		this=1
		#print days
		#days=[]
		if str(s.a.contents[0]) =="?":
			#print days
			days.insert(0,comp)
			days.insert(1,tues)
			days.insert(2,wed)
			days.insert(3,golf)
			days.insert(4,dinner)
	                writer1.writerow(days)
			days=[]
			tues=[]
			wed=[]
			golf=[]
			dinner=[]
			st =1
	if parser.feed(str(s)):
		#print "<<<<<<<<<<<<<<<<<<"
		#print str(s)
		#print "###########"
		parser.feed(str(s))
		#print ">>>>>>>>>>>>>>>>>"
	elif this==0 and st==0:
		#print "!!!!!!!!!!!!!!"
		#print str(s)
		#print "@@@@@@@@@@@@@"
		#days.append("no")
		count =count +1
		if count==1:
			tues=0
		elif count==2:
			wed=0
		elif count==3:
			golf=0
		elif count==4:
			dinner=0
#print sys.getsizeof(soup)
print ccc
#"""
