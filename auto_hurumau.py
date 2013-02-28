import urllib2
import time
import sys
from BeautifulSoup import BeautifulSoup
cookie = raw_input('input konmai cookie: ')
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', cookie))
opener.addheaders.append(('Host', 'p.eagate.573.jp'))

while True:
	try:
		page = opener.open('http://p.eagate.573.jp/game/bemani/cafedetran/p/')
		soup = BeautifulSoup(page)
		hurumau_part = soup.find(id="action_btn_container")
		print hurumau_part
		for link in hurumau_part.findAll('a'):
			print link
			newurl = link.get('href')
			opener.open(newurl)
		time.sleep(60)
	except Exception, e:
		print sys.exc_info()[0], e
		time.sleep(240)
