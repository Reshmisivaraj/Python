import math 
a = float(input("Enter the coefficient of x**2 :"))
b =float(input("Enter the coefficient of b :"))
c =float(input("Enter the constant term :"))
d =b**2-4ac
x1 =((-b)+ (math.sqrt(d)))/(2*a)
x2 =(-b)- (math.sqrt(d)))/(2*a)
print("Rootsofthe quadratic equation are :",x1,x2)
