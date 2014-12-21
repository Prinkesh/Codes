def C(n,r):
    if (r==0): return 1
    else: return C(n-1,r-1)*n/r
for i in range(int(raw_input())):
    a=raw_input().split()
    print C(int(a[0]),int(a[1]))
