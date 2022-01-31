#linear search
def linear_search(list1,search):
    found=False
    for i in range(len(list1)):
        current_elt=list1[i]
        if (search==current_elt):
            found=True
            break
    if found==True:
        print("Element found. Index =",i)
    else:
        print("Element not present in the list")
if __name__=="__main__":    
    n=int(input("Enter the number of elements: "))
    print("Enter the elements: ")
    list1=[input() for x in range(n)]
    search=input("Enter the element to be searched: ")
linear_search(list1,search)

#binary search
n=int(input("Enter the number of elements in the list:"))
l=[int(input())for x in range(n)]
l.sort()
print("Sorted list:",l)
n1=int(input("Enter the number to be searched:"))
low,high,i=0,len(l)-1,0
f=0
while i<=len(l):
    mid=(low+high)//2
    i=i+1
    if l[mid]==n1:
        print(" A match found at index ",mid)
        f=1
        break
    elif l[mid]>n1:
        high=mid-1
    else:
        low=mid+1
if f==0:
    print(" Match not found ")

#selection sort
n=int(input("Enter the number of elements in the list"))
L=[int(input())for i in range(n)]
for i in range(len(L)):
    m=min(L[i:])
    ind=L.index(m)
    L[i],L[ind]=L[ind],L[i]
print("Sort",i+1,":",L)

#insertion sort
n=int(input("Enter the number of elements in the list"))
L=[int(input())for i in range(n)]
for i in range(1, len(L)):
    key = L[i]
    j=i-1
    while j>=0 and key<L[j]:
        L[j+1]=L[j]
        j=j-1
        L[j+1]=key
    print("Pass:",i,":",L)

#quick sort
def quickSort(L,low,high):
    if low < high:
        i =low-1
        pivot=L[high]
        for j in range(low,high):
            if L[j]<pivot:
                i=i+1
                L[i],L[j]=L[j],L[i]
        L[i+1],L[high] = L[high],L[i+1]
        quickSort(L,low,i)
        quickSort(L, i+2, high)
n=int(input("Enter the number of elements in the list:"))
L=[int(input())for x in range(n)]
quickSort(L,0,len(L)-1)
print("Sorted list:",L)