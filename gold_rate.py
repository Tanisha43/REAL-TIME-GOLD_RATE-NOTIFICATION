from plyer import notification
from bs4 import BeautifulSoup
import requests

def notifyme(title,message):
	notification.notify(title=title,message=message,app_icon='C://Users//Tanisha Goel//Desktop//notification//images.ico',timeout=10)

def getdata(url):
	r=requests.get(url)
	return r.text	

if __name__=="__main__":

	data=getdata("https://www.goodreturns.in/gold-rates/#Indian+Major+Cities+Gold+Rates+Today")
	soup=BeautifulSoup(data,'html')
	gold_list=soup.find_all('div',{'class':'gold_silver_table'})
	print(len(gold_list))
	data=gold_list[2].text.split('\n\n')
	city=['Mumbai']
	for item in data:
	    if item=='' or item=='\n':
	        continue
	    else:
	        final=item.split('\n')[1:]
	        if final[0] in city:
	        	print(final)
	        	ntitle="GOLD RATES"
	        	ntext=f"CITY : {final[0]}\n 22 Carat Gold Today : {final[1]}\n 24 Carat Gold Today : {final[2]}"
	        	notifyme(ntitle,ntext)
