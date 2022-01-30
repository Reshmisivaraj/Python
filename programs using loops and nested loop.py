n1=int(input("enter an integer:"))
n2=int(input("Enter the second integer:"))
m=min(n1,n2)
for i in range(1,m+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print("the gcd of",n1,n2,"is",gcd)

# prime number
n=int(input("enter a number:"))
i=0 
for i in range(2,n):
    if n%i==0:
        print("the no. is not prime ")
       break
    else:
        print("the number is prime ")
	

#sum of individual numbers
num=int(input("enter the number:"))
sum=0
result=0
while num >0:
    sum=num%10
    num=num//10
    result+=sum  
print("the sum of individual numbers is:",result)    


#multiplication table
n=int(input("enter the number the number for which multiplication is performe:"))
i=0
a=0
for i in range(1,21):
  a=n*i
  print("the multiplication table of",n,"is",a)    

#sum of series
def fac(n):
    f=1 
    for i in range(1,n+1):
        f=f*i 
    return f 
n=int(input("enter a number:"))
sum=0
for m in range(n+1):
    sum+= m*m/fac(m)
print(sum)

# upper left triangle
def upper_left_triangle(n):
    for i in range(n,0,-1):
        print(" "*(i-1),"*"*(n-i+1))
rows=int(input("Enter the number of rows: "))
upper_left_triangle(rows)


#upper right triangle
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    print((i)*'x',' '*(n))

    #upper pyramid
    def upper_pyramid(n):
    for i in range(n,0,-1):
        print(" "*(i-1),"* "*(n-i+1))
rows=int(input("Enter the number of rows:"))
upper_pyramid(rows)



#newtons square root
def NewtonSqrt(n):
    approx=1
    for i in range(n):
        better_approx=0.5*(approx+(n/approx))
        if (approx==better_approx):
            break
        approx=better_approx
    return better_approx
n=int(input("Enter the number: "))
print("Square root =",NewtonSqrt(n))
