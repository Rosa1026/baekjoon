N = 3
k = 7
i = 0
j = 0
A=[[1,2,3],
   [2,4,6],
   [3,6,9]]

B=[]

while i < N:
    while j < N:
        B.append(A[i][j])
        if j == N-1:
            j = 0
            break
        else:
            j += 1
    i+=1

B.sort()
print(B[k-1])
