# Rotate a N x N Matrix by 90 degree

# Trick Mathematics ??? Rotation of a point around another point 


def rotate(i,j,n):
	return (abs(-j),-i+n)

arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in xrange(len(arr)/2):
	for j in xrange(i,len(arr)-(i+1)):
		#i=0
		currloc=(i,j)
		temp=arr[currloc[0]][currloc[1]]
		for i in xrange(4):
			nextloc=rotate(currloc[0],currloc[1],len(arr)-1)
			temp1=arr[nextloc[0]][nextloc[1]]
			arr[nextloc[0]][nextloc[1]]=temp
			temp=temp1
			currloc=nextloc
