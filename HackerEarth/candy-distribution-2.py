t=int(raw_input())
for i in xrange(t):
	n=int(raw_input())
	a=map(int,raw_input().split())
	#mina=min(a)
	#maxa=max(a)
	print sum(a)-(n-1)
