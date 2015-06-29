import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#link="http://www.autotrader.com/cars-for-sale/Used+Cars/Coupe/Austin+TX-78726?endYear=2016&listingType=used&listingTypes=used&maxPrice=9000&minPrice=7000&searchRadius=200&showcaseOwnerId=73408&sortBy=derivedpriceASC&startYear=1981&vehicleStyleCodes=COUPE,SEDAN&Log=0&showcaseOwnerId=73408&captureSearch=true&fromSIP=F7ADAF203F94F23FBA8DDE4A6AFD6C69&showToolbar=true&Log=0"
base_link="http://www.autotrader.com/cars-for-sale/Used+Cars/Coupe/Austin+TX-78726?endYear=2016&listingType=used&listingTypes=used&maxPrice=9000&minPrice=7000&numRecords=100&searchRadius=200&showcaseOwnerId=73408&sortBy=derivedpriceASC&startYear=1981&vehicleStyleCodes=COUPE,SEDAN&Log=0"
link="http://www.autotrader.com/cars-for-sale/Used+Cars/Coupe/Volvo/Austin+TX-78726?endYear=2016&listingType=used&listingTypes=used,certified&makeCode1=VOLVO&makeCode2=MAZDA&makeCode3=TOYOTA&maxMileage=150000&maxPrice=9000&minPrice=7000&mmt=%5BACURA%5B%5D%5B%5DAUDI%5B%5D%5B%5DBMW%5B%5D%5B%5DHONDA%5B%5D%5B%5DHYUND%5B%5D%5B%5DINFIN%5B%5D%5B%5DKIA%5B%5D%5B%5DLEXUS%5B%5D%5B%5DMAZDA%5B%5D%5B%5DMB%5B%5D%5B%5DMIT%5B%5D%5B%5DNISSAN%5B%5D%5B%5DSCION%5B%5D%5B%5DSUB%5B%5D%5B%5DSUZUKI%5B%5D%5B%5DTOYOTA%5B%5D%5B%5DVOLKS%5B%5D%5B%5DVOLVO%5B%5D%5B%5D%5D&numRecords=100&searchRadius=200&showcaseListingId=0&showcaseOwnerId=0&sortBy=distanceASC&startYear=2004&vehicleStyleCodes=COUPE,SEDAN&Log=0"
req=urllib2.Request(link,headers={'User-Agent':'Firefox'})
response=urllib2.urlopen(req)
#print response
page=response.read()
#print page
soup=BeautifulSoup(page,'html5lib')
#print soup.prettify()
car_details_h2=[]
for i in soup.find_all("h2"):
    car_details_h2.append(i)
print len(car_details_h2)


car_price_h4=[]
soup=BeautifulSoup(page,'html5lib')
for i in soup.find_all("h4"):
    car_price_h4.append(i)
print len(car_price_h4)
#temp= car_details_h2[14]
temp=car_price_h4[14]
#print temp
#soup1=BeautifulSoup(temp)
#print soup1

temp_div=[]
#for i in soup.find_all("div"):
#    soup1=BeautifulSoup(i,"html5lib")
#    for j in soup1.find_all("div"):
#        temp_div.append(
#print temp_div[0]
#print car_details_h2[-10]

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
#next=False
global car_dat
car_dat=[]
global l
l=[]
global car_links
car_links=[]
class MyHTMLParser(HTMLParser):
    #def __init__(self):
    #    self.next=False
    def handle_data(self, data):
        global car_dat
        global l
        #if self.next:
        if not data.isspace():
            #if data[-27:-17]=="catch(e){}":
            if data[-29:-13]=="jQuery, window);":
                l=[]
            elif data[-27:-17]=="catch(e){}":
                car_dat.append(l)
            else:
                l.append(data)
                #print "Data     :", data#[-29:]
        #    self.next=False
    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        for attr in attrs:
            if tag=="a":
                if attr[0]=="href":
                    car_links.append(attr[1])
                    #print("     attr:", attr)
            

parser = MyHTMLParser()
#next=False
parser.feed(page.decode("utf-8","ignore"))
car_mileage=[]
car_price=[]
car_make=[]
#print car_dat
count=0
for i in range(0,len(car_dat)):
    #print car_dat[i]
    for j in range(0,len(car_dat[i])):
        if car_dat[i][j][-5:]=="miles":
            #print car_dat[i][j-1]
            car_mileage.append(car_dat[i][j-1])
            if car_dat[i][j-2]=="Reduced!":
                car_price.append(car_dat[i][j-3])
            elif car_dat[i][j-2]=="View additional terms":
                car_price.append(car_dat[i][j-7])
            else:
                car_price.append(car_dat[i][j-2])
            if car_dat[i][-3][:2]=="1-" or car_dat[i][-3][:3]=="Get":
                car_make.append(car_dat[i][-2])
            elif car_dat[i][-3][0]=="\n":
                car_make.append(car_dat[i][-2])
            else:
                car_make.append(car_dat[i][-3])
#print re.match(r'mileage',str(soup),re.M|re.I)
#parser.feed(str(temp))
#for i in range(14,len(car_details_h2)):
#    parser.feed(str(car_details_h2[i]))

#for j in range(0,24):
#    print car_details_h2[len(car_details_h2)-24+j],
#    print car_price_h4[len(car_price_h4)-24+j],
#    print car_mileage[j]

#for j in range(0,len(car_mileage)):
print len(car_mileage),car_mileage[0],car_mileage[-1]
print len(car_price),car_price[0],car_price[-1]
print len(car_make),car_make[0],car_make[-1]

#import html2text
parser1=MyHTMLParser()
for i in car_details_h2:
    parser1.feed(str(i))
#parser1.feed(html2text.html2text(car_details_h2[-10]))

print len(car_links)

link_len=len("/cars-for-sale/vehicledetails")
car_links_fin=[]
for i in car_links:
    if i[:link_len]=="/cars-for-sale/vehicledetails":
        car_links_fin.append(i)
print len(car_links_fin)
#print car_links_fin[-1]
#print car_links_fin[-2]

car_links_new=[]
for i in range(len(car_links_fin)-len(car_make)-1,len(car_links_fin)):
    car_links_new.append(car_links_fin[i])
print len(car_links_new)
#print car_links_new

import csv
wr=csv.writer(open("out.csv","wb"))
wr.writerow(["Year","Make","Model","Price","Mileage","Link"])
for j in range(0,len(car_make)-1):
    try:
        wr.writerow([car_make[j].split()[1],car_make[j].split()[2],car_make[j].split()[3],car_price[j+1],car_mileage[j+1],"http://autotrader.com"+car_links_new[j+1]])
    except:
        continue


