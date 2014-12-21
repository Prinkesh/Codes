for i in range(int(raw_input())):
	n=int(raw_input())
	a=map(int,raw_input().split())
	k=int(raw_input())
	for j in range(k):
		l,u=map(int,raw_input().split())
		ans=a[l]
		for m in range(l+1,u+1):
			ans=ans^a[m]
		print ans
			
