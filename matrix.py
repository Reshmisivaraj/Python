#matrix addition
n=int(input("Enter the number of rows in matrix:"))
L1=[[int(input())for i in range(n)]for j in range(n)]
L2=[[int(input())for i in range(n)]for j in range(n)]
R=[[0 for i in range(n)]for j in range(n)]
for i in range(len(L1)):
    for j in range(len(L1[0])):
        R[i][j]=L1[i][j]+L2[i][j]
for i in range(len(R)):
    for j in range(len(R[0])):
        print(R[i][j],end='\t')
    print(end="\n")
#matrix subraction
n=int(input("Enter the number of rows in matrix:"))
L1=[[int(input())for i in range(n)]for j in range(n)]
L2=[[int(input())for i in range(n)]for j in range(n)]
R=[[0 for i in range(n)]for j in range(n)]
for i in range(len(L1)):
    for j in range(len(L1[0])):
        R[i][j]=L1[i][j]-L2[i][j]
for i in range(len(R)):
    for j in range(len(R[0])):
        print(R[i][j],end='\t')
    print(end="\n")

#transpose 
n=int(input("Enter the number of rows in matrix:"))
L1=[[int(input())for i in range(n)]for j in range(n)]
R=[[0 for i in range(n)]for j in range(n)]
for i in range(len(L1)):
    for j in range(len(L1[0])):
        R[j][i]=L1[i][j]
for i in range(len(R)):
    for j in range(len(R[0])):
        print(R[i][j],end='\t')
    print(end="\n")
#multiplication
R1=int(input("Enter the num of rows(MATRIX-1):"))
C1=int(input("Enter the num of columns(MATRIX-1):"))
C2=int(input("Enter the num of cols(MATRIX-2):"))
L1=[[int(input())for i in range(C1)]for j in range(R1)]
L2=[[int(input())for i in range(C2)]for j in range(C1)]
R=[[0 for i in range(C2)]for j in range(R1)]
for i in range(len(L1)):
    for j in range(len(L2[0])):
        for k in range(len(L2)):
            R[i][j]+=L1[i][k]*L2[k][j]
for i in range(len(R)):
    for j in range(len(R[0])):
        print(R[i][j],end='\t')
    print(end="\n")