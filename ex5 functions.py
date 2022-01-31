#sine and cos
import math
def cosine(x,n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        pi=22/7
        y=x*(pi/180)
        cosx = cosx + (sign*(y**i))/math.factorial(i)
        sign = -sign
        return cosx
#sinx = x – x3/3! + x5/5! - ….
def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
        return sine
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(round(cosine(x,n),2), round(sin(x,n),2))

#pythagorean triplet
from math import sqrt
n=int(input('Enter lower range:'))
m=int(input('Enter upper range:'))
z=0
l=2
while z<m:
    for i in range(1,l+1):
        x=(l**2)-(i**2)
        y=2*l*i
        z=l**2+i**2
        if z>m:
            break
        elif(x==0 or y==0 or z==0):
            break
print(x,y,z, ' are pythagorean triplets.')
l+=1
