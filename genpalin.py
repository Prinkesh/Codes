import sys
import math

def ispalin(num):
        #checks if a number is palindrome
	z=str(num)
	l=len(z)
	if l%2==0:
		if z[:l/2]==z[-l/2:][::-1]:
			return True
	elif z[:l/2 + 1]==z[-l/2:][::-1]:
		return True
	return False

def genpalin(n):
        #Generates a list of palindrome till n 
        k=str(n)
        if len(k)%2==0:
                r=len(k)/2
        else:
                r=len(k)/2 + 1
        gen=set()
        for i in range((10**(r))+1):
                if ispalin(i):
                        gen.add(i)
                j=str(i)
                j=j+j[::-1]
                if int(j)<=n:
                        gen.add(int(j))
                j=str(i)
                j=j+j[:-1][::-1]
                if int(j)<=n:
                        gen.add(int(j))
        return gen

t=int(sys.stdin.readline())
        
a=genpalin(t)
