t = int(raw_input())
for i in xrange(t):
	st=str(raw_input())
	l=len(st)
	#print st
	st=st[4:]
	#print st
	j=len(st)
	for k in st:
		if k in ['a','e','i','o','u']:
			j=j-1
	print str(j+1)+"/"+str(l)
