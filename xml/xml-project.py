import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_187129.xml'
Count = 0
Sum = 0
# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break
#
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)


lst = tree.findall('comments/comment')
Count = len(lst)
print Count
for item in lst:
    Sum += int(item.find('count').text)


print Sum
