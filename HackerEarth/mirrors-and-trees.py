t=int(raw_input())
for test in xrange(t):
    n=int(raw_input())
    a=map(int,raw_input().split())
    mark=['n']*n
    k=-1
    N=n+1
    while(N!=0):
        N=N/2
        k+=1
    #print k #level satrting from 0
    right=[]
    left=[]
    right.append(a[0])
    for level_no in xrange(1,k):
        rightmost_ind=(2**(level_no+1)-2)
        leftmost_ind=(2**level_no)-1
        #print level_no,rightmost_ind,leftmost_ind
        right_ind=-1
        left_ind=-1
        for i in xrange(rightmost_ind,leftmost_ind-1,-1):
            #print i
            if a[i]!=0:
                right_ind=i
                break
        for i in xrange(leftmost_ind,rightmost_ind+1,1):
            if a[i]!=0:
                left_ind=i
                break
        if right_ind!=-1:
            if right_ind==left_ind:
                right.append(a[right_ind])
            else:
                right.append(a[right_ind])
                left.append(a[left_ind])
    for i in right:
        print i

    for i in left:
        print i
    print ''
            
