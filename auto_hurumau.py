import urllib
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
		for link in hurumau_part.findAll('form'):
			print link
			newurl = link.get('action')
			if newurl[0] == '/':
				newurl = 'http://p.eagate.573.jp' + newurl
			else:
				newurl = 'http://p.eagate.573.jp/game/bemani/cafedetran/p/' + newurl
			values = {}
			for inp in link.findAll('input'):
				if inp.get('type') == 'hidden':
					values[inp.get('name')] = inp.get('value')
			data = urllib.urlencode(values)
			req = urllib2.Request(newurl, data)
			response = urllib2.urlopen(req)
			response.read()
		time.sleep(60)
	except Exception, e:
		print sys.exc_info()[0], e
		time.sleep(240)
