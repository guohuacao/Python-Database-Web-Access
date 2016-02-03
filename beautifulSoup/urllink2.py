# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_187132.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   # print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   #print type(tag.contents[0])
   sum += int(tag.contents[0])
print sum
   # print 'Attrs:',tag.attrs
#table = soup.find("table", attrs = {"Name": "Comments"})

# print table
# for row in table.findAll("tr"):
#     cells = row.findAll("td")
#     if len(cells) == 2:
#         amount = cells[2].find(text = True)
#         print amount
   # Look at the parts of a tag

   #print 'Contents:',tag.comments
