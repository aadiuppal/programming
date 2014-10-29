import json
import requests
import urllib2
import bs4

#api_key = '6kfcvgrshs9sa8yfwxeeeg3h'

url = 'https://en.wikipedia.org/wiki/Elections_in_India'#'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/top_rentals.json?apikey=' + api_key
data = urllib2.urlopen(url).read()
## create dictionary from JSON 
#dataDict = json.loads(data)
soup = bs4.BeautifulSoup(data)
#print soup.prettify
#td=soup.findAll('td')
#print td
#tdsoup = bs4.BeautifulSoup(td)
l=[]
total_seats=[]
winner=[]
start =0
n=4
for i in soup.findAll('td'):
	if start == 2:
		winner.append(i)
		start=0
	if start == 1:
        	total_seats.append(i)
		start=2
	
	if i.find('a'):
		try:
			pos=i.find('a')		
			if pos.get('href') == '/wiki/'+str(n)+'th_Lok_Sabha':
				print i
				start =1
				n=n+1
		except:
			print 1
	#	print i[pos:pos+20]
	#	print i.get('href')#== '/wiki/1st_Lok_Sabha':
	#		print i
			#l.append(i)
	

#trin=total_seats[0]
print total_seats
print winner

for i in range(0,n-2):
	print str(total_seats[i])[4:7]
	print str(winner[i])[4:7]	

## expore dictionary
#print dataDict.keys()
