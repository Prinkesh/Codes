t=int(raw_input())
while(t>0):
	n=int(raw_input())
	a=[]
	for i in xrange(n):
		a.append(int(raw_input()))
	a.sort()
	pac=0
	b={}
	
	for i in xrange(n):
		if b.has_key(a[i]):
			b[a[i]]+=1
		else:
			b[a[i]]=1
	while(len(b)!=0):
		#print b
		for i in b.keys():
			if (b[i]==1):
				b.pop(i)
			else:
				b[i]=b[i]-1
		pac+=1
	print pac
	t-=1
