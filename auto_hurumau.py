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
		page = opener.open('http://p.eagate.573.jp/game/bemani/cafedetran/p/index.html?c=1')
		time.sleep(10)
		opener.open('http://p.eagate.573.jp/game/bemani/cafedetran/p/get.html?c=1')
		soup = BeautifulSoup(page)
		hurumau_part = soup.find(id="action_btn_container")
		print hurumau_part
		time.sleep(150)
	except Exception, e:
		print sys.exc_info()[0], e
		time.sleep(150)
