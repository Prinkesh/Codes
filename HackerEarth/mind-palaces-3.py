n,m=map(int,raw_input().split())
mydic=dict()
for i in range(n):
    row=map(int,raw_input().split())
    #print row
    for j in range(m):
        #row
        mydic[row[j]]=(i,j)
q=int(raw_input())
for i in range(q):
    val=int(raw_input())
    if mydic.has_key(val):
        print str(mydic[val][0])+" "+str(mydic[val][1])
    else:
        print "-1 -1"
