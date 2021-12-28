l1=input("enter a string:")
l2=input("enter the second string")
l1_new=sorted(l1)
l2_new=sorted(l2)
if l1_new==l2_new:
    print("it is a anogram")
else:
    print("it is not a anogram")