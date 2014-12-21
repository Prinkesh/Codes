days=dict()
for i in range(1,31):
    days[i]=0
for i in range(int(raw_input())):
    stri=str(raw_input())
    dayse=[int(s) for s in stri.split(' ') if s.isdigit()]
    #print dayse
    if stri[0]=='G':
        for j in dayse:
            days[j]+=2
    else:
        for j in dayse:
            days[j]+=1
v = {}
for key, value in sorted(days.iteritems()):
    v.setdefault(value, []).append(key)
##flag=0
##for i in v:
##    if len(v[i])>1 and i!=0:
##        flag=1
##        break
##if flag==1:
##    print "No Date"
##else:
if len(v[max(v)])==1:
    if v[max(v)][0] in [19,20]:
        print 'Date'
    else:
        print 'No Date'
else:
    print 'No Date'
