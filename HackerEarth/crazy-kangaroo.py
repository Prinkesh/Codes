t=int(raw_input())
for i in xrange(t):
	a,b,k=map(int,raw_input().split())
	a_mod=a%k
	if a_mod!=0:
		a+=(k-a_mod)
	b-=b%k
	if a>b:
		print "0"
	else:
		print ((b-a)/k)+1
