
def unswap(string):
    dic=dict()
    
    oddpos=len(string)-1
    evenpos=0
    for i in range(len(string)):
        if i%2!=0:
            s[oddpos]=string[i]
            oddpos-=1
        else:
            s[evenpos]=string[i]
            evenpos+=1
        #print s
    return s

k=int(raw_input())
string=list((raw_input()))
string1=string
s=['']*len(string)
stp=0
flag=0
for i in range(k):
	h=unswap(string)
	string=h
	stp+=1
    if string==string1:
    	   	flag=1
    	   	break
if flag==1:
    for i in range(k%stp):
#        print i
        string=unswap(string)
print ''.join(string)
    
