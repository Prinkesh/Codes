st=str(raw_input())
le=len(st)
t=int(raw_input())
for test in xrange(t):
	a,b=map(int,raw_input().split())
	if st[(a%le)-1]==st[(b%le)-1]:
		print 'Yes'
	else:
		print 'No'
