a=str(input("enter a word:"))
x=""
for i in range(len(a)-1,-1,-1):
    x=x+a[i]
if x==a:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
        