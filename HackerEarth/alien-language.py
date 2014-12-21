t=int(raw_input())
for i in xrange(t):
	str1=set(str(raw_input()))
	str2=set(str(raw_input()))
	if len(str1.intersection(str2))==0:
		print "NO"
	else:
		print "YES"
