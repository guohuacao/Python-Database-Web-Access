# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re
url = raw_input('Enter - ')
#url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
count = raw_input('Enter count - ')
position = raw_input('Enter position - ')
ct = int(count)
pos = int(position)
while ( ct):
    print "Retrieving:%s ", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    #print tags[2]
    url =  tags[pos-1].get('href', None)

    ct -=1
print "Last Url:%s ", url
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)
name = re.findall('known_by_.+', url)
name1 = str(name).split('.')
print name1[0], "xx", name1[1]
name2 = str(name1[0]).split('_')
print name2[2]
