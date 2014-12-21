n=int(raw_input())
line1=[int(i) for i in raw_input().split(' ')]
line2=[int(i) for i in raw_input().split(' ')]
flag='Yes'
for i in range(len(line1)):
    if line1[i]<line2[i]:
        flag='No'
        break;
print flag
