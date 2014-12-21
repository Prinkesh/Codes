num=int(raw_input())
if num%2==0:
    fac=1
else:
    fac=num
    num-=1
for i in range(num/2):
        fac*=(i+1)*(num-i)
sfac=str(fac)
print len(sfac)-len(sfac.rstrip('0'))
