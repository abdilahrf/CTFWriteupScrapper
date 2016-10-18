from project import app,db
from flask import Flask, render_template
from models import Writeups
from datetime import datetime
from BeautifulSoup import BeautifulSoup
import urllib2,requests,cookielib,mechanize


@app.route('/')
def index():

	# Browser
	br = mechanize.Browser()

	# Cookie Jar
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	br.addheaders = [('User-agent', 'Chrome')]
	x=1

	event = []
	task = []
	tags = []
	author = []
	writeupUrl = []

	url = []

	while True:
		temp=[]
		#content = br.open('https://ctftime.org/writeups?page='+str(x)).read()
		#https://ctftime.org/writeups?page='+str(x)+'&hidden-tags=reverse+engineering'

		
		try:
			#get all web writeup
			content = br.open('https://ctftime.org/writeups?page='+str(x)+'&hidden-tags=web').read()
		except Exception, e:
			break

		
		soup = BeautifulSoup(content)
		x+=1

		datas = soup.findAll('td')
		for r in datas:
			temp.append(r.next)

		idx = 0
		for c in range(len(temp)/5):
			event.append(temp[idx])
			task.append(temp[idx+1])
			tags.append(temp[idx+2])
			author.append(temp[idx+3])
			writeupUrl.append(temp[idx+4])
			idx+=5

	return render_template('index.html',data=zip(event,task,tags,author,writeupUrl));






