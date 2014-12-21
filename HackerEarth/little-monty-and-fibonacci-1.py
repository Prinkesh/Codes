##fib=[0]*1001
##fib[1]=fib[2]=1
##for f in xrange(3,1001):
##    fib[f]=fib[f-1]+fib[f-2]
##print fib[0:15]
def n_multiples(n,start,end):
    return ((end-start)/n)+1

t=int(raw_input())
for test in xrange(t):
    n=int(raw_input())
    sum_=0
    if n>2:
        for i in xrange(3,n+1):
            sum_+=n_multiples(i,i,n)
        sum_+=2*n
    else:
        sum_=n*n
    print sum_
            
