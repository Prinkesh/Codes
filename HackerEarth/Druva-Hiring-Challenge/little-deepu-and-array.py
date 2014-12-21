t=int(raw_input())
for test in xrange(t):
    n=int(raw_input())
    a=map(int,raw_input().split())
    onleft=[0]*n
    onright=[0]*n
    max_so_far=0
    
    for i in xrange(n):
            if(a[i]>=max_so_far):
                max_so_far=a[i]
                onleft[i]=0
            else:
                onleft[i]=max_so_far
    max_so_far=0
    for i in xrange(n-1,-1,-1):
            if(a[i]>=max_so_far):
                max_so_far=a[i]
                onright[i]=0
            else:
                onright[i]=max_so_far
    p_sum=0
    for i in xrange(n):
        if (onleft[i]!=0 and onright[i]!=0):
                    p_sum+=min(onleft[i],onright[i])-a[i]
    print p_sum
