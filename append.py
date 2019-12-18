#appending element of two arrays
import numpy as np
x=input("enter array elemts of x")
y=input("enter array element of y")
print "elements of x array",x
print "elements of y array",y
c=np.append(x,y)
print"appending two matrices using numpy",c
for i in range (0,len(y)):
	if(y[i]<0):
		continue
	else:
		x.append(y[i])
print "element of x array after appending",x
