import re
hand = open('regex_sum_187127.txt')
num_list = []
for line in hand:
    line = line.rstrip()
    num_string =  re.findall('[0-9]+', line)
    if (len(num_string) > 0):
        #num_list.append( int(a) for b in num_string if a.isdigit())
        for a in num_string:
            num_list.append(int(a))
#print num_list
print "sum is ", sum(num_list)
