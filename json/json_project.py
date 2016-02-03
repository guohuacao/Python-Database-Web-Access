import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_187133.json'
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
info = json.loads(data)
#print 'User count:', len(info)
#print json.dumps(info, indent = 4)
lst = info["comments"]
print len(lst)

for item in lst:
    Sum += int(item["count"])

print Sum
