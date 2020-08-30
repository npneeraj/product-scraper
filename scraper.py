import requests
from bs4 import BeautifulSoup
import smtplib
import urllib
import re

def check_price():
	#Product to be monitored in url
	url='https://www.flipkart.com/redgear-pro-series-wireless-gamepad/p/itmehwaacnryp3je' #demo example
	#headers as per user machine 
	headers={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

	page=requests.get(url,headers=headers)
	soup=BeautifulSoup(page.content,'html.parser')
	#
	'''outer=soup.find("div",{"class":"bhgxx2 col-12-12"})
				for tag in outer:
					out=tag.find("div",{"class":"_29OxBi"})
					print(out)
					for inner in out:
						inn= inner.find('div',class_="_9E25nV").h1
				out=soup.find('span',class_='_35kyD6')
				print(out)
			'''

	#title=inn.get_text()
	#print(title.strip())
	# <div class="_1vC4OE _3qQ9m1">₹979</div>
	# <div class="">
	title="redgear-pro-series-wireless-gamepad"
	divTag= soup.find_all("div", {"class": "_3iZgFn"})

	for tag in divTag:
		inner = tag.find_all("div", {"class": "_1vC4OE _3qQ9m1"})
		for tag in inner:
			price=tag.text
	#converted_price=float(price[1:])    	
	
	print(price)
	#converted_price=float(price[0:2])
	#print(type(price))
	converted_price=float(price[1:].replace(',',''))
	print(converted_price)
	#print(title.strip())
	if converted_price>970.0:
		send_mail()






def send_mail():
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	email='neeraj.panwar2016@gmail.com' #your email here
	password='yourpassword'		#your app- specific password here not gmail password
	server.login(email,password)
	subject='Price drop down'
	body='Check the link https://www.flipkart.com/redgear-pro-series-wireless-gamepad/p/itmehwaacnryp3je'
	msg=f'Subject:{subject}\n\n{body}'
	server.sendmail(
		email,
		email,
		msg
		)
	#put your email in second parameter
	print("EMAIL HAS BEEN SENT SUCCESSFULLY")
	server.quit()


check_price()

