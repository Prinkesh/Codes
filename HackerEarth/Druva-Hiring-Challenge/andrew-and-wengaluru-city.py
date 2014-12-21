n=int(raw_input())
a=map(int,raw_input().split())
for i in xrange(n):
	a[i]=[a[i],i]
a.sort()
temp=[]
def binary_search(low,high,x):
    global a
    if high>=low:
        mid=low+(high-low)/2
        #print mid,"mid"
        if ((a[mid][0]-findpindex(mid))>x and (mid == low or  (a[mid-1][0]-findpindex(mid-1))<=x)):
            return mid
        if ((a[mid][0]-findpindex(mid))<=x):
            return binary_search((mid + 1), high,x)
        else:
            return binary_search(low, (mid -1),x)
    return -1

def binary_search1(low,high,x):
    global temp
    if high>=low:
        mid=low+(high-low)/2
        #print low,high,mid,"mid"
        if (temp[mid]>x and (mid == low or  temp[mid-1]<=x)):
            return mid
        if (temp[mid]<=x):
            return binary_search1((mid + 1), high,x)
        else:
            return binary_search1(low, (mid -1),x)
    return 0
def findpindex(index):
	global temp
	if len(temp)==0:
		return 0
	if (temp[-1])<=index:
		return len(temp)
	if (temp[0])==index:
		i=0
		while(temp[i]==index):
			i+=1
		return i
	i=1
	if i==len(temp):
		return 0
	while (temp[i]<=index):
		i*=2
		if i>len(temp)-1:
			break
	min_=i/2
	if i>len(temp)-1:
		i=len(temp)-1
	if min_>len(temp)-1:
		return 0
	return binary_search1(min_,i,index)
    
def findfirst(x):
    global a,n
    
    if (a[-1][0]-findpindex(n-1))<=x:
        		return -1
    
    if (a[0][0]-findpindex(0))>x:
        		return 0
    
    
    i=1
    if i==n:
    	return -1
    #print i
    	  	
    while ((a[i][0]-findpindex(i))<=x):
        i*=2
        #print i 
        if i>n-1:
            break
    #print i,"end"
    min_=i/2
    if i>n-1:
        i=n-1
        
    if min_>n-1:
        return -1
    #print min_,i,x,"bsearch"
    return binary_search(min_,i,x)

q=int(raw_input())

for query in xrange(q):
	x=int(raw_input())
	index=findfirst(x)
	#print a,x,index
	if index!=-1:
		temp.append(index)
	temp.sort()
#print temp
for i in xrange(n):
	a[i][0]=a[i][0]-findpindex(i)
from operator import itemgetter
a.sort(key=itemgetter(1))
for i in a:
	print i[0],
