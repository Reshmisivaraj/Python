#efficient power of a number
e=2.7182
n=eval(input("Enter exponent value n:"))
def exp(n):
  if n!=0:
    return e*exp(n-1)
  else:
    return 1
print(exp(n),”is the required value.”)


#factorial
n=eval(input("Enter value to find factorial:"))
def fac(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fac(n-1)
print(fac(n),"is the factorial")

#fibonacci
def fib(n):
  if n==0 or n==1:
    return n
  else:
    return fib(n-1)+fib(n-2)
n=eval(input("Enter how many terms of fibonacci series are to be printed:"))
for i in range(n):
  print(fib(i))


