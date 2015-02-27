import urllib2
import os
from bs4 import BeautifulSoup
import HTMLParser

def push_note(note_title,note_body):
	url_check="https://api.pushbullet.com/v2/users/me"
	url_pushes="https://api.pushbullet.com/v2/pushes"
	url_devices="https://api.pushbullet.com/v2/devices"
	access_token="###################################"



	check_command="curl -u "+access_token+": "+url_check+" -k"

	#note_title="NOte title"
	#note_body="NoTe BoDy"
	try:
		push_header="'Content-Type: application/json' --data-binary "
		push_details='{"type":"note","title": "'+note_title+'","body": "'+note_body+'"}'
		push_command="curl -u "+access_token+": "+"-X POST "+url_pushes+" --header "+push_header+" '"+push_details+"'"+" -k"
      
		devices_command="curl -u "+access_token+": "+"-X GET "+url_devices+" -k"

		os.system(push_command)
	except:
		pass


algo_cs629_url="http://faculty.cs.tamu.edu/ajiang/629.html"
old_page=""
while True:
	page_resp=urllib2.urlopen(algo_cs629_url)
	new_page=page_resp.read()
	#soup=BeautifulSoup(new_page)
	#body=soup.string
	#print body 
	h = HTMLParser.HTMLParser()
	body= h.unescape(new_page)
	if old_page and new_page != old_page:
		#body=str(new_page).rsplit(str(old_page))
		#body=h.unescape(body)
		push_note("Changes on Algo 629 page","Possibly next HW posted")
	old_page=new_page

