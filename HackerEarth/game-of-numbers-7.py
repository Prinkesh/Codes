for test in xrange(int(raw_input())):
    lowbnd,upbnd=map(int,raw_input().split())
    #lowbnd=10
    #upbnd=20
    #print (ip)
    #cnt=0
    ip=[True]*(upbnd-lowbnd+1)
    for n in xrange(2,upbnd+1):
        #print (n)
        k=n*n
        if k>upbnd:
        	break
        mo=lowbnd%k
        if mo==0:
            bs=lowbnd
        else:
            bs=lowbnd+(k-mo)
        #print (str(bs) +" base")
        for i in xrange(bs, upbnd+1, k):
            #print (i)
            #print (i-lowbnd)
            #if !(ip[i-lowbnd]):
            #	cnt+=1
            ip[i-lowbnd] = False
            
    cnt=0
    #print (ip[:upbnd-lowbnd+2])
    for i in xrange(upbnd-lowbnd+1):
        if ip[i]:
            cnt+=1
       
    
    print cnt
