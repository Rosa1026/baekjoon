import sys

A, B = sys.stdin.readline().split()
ans = []

if A in B:
    print(0)

else:
    for i in range(len(B) - len(A) + 1):
        cnt = 0
        for j in range(len(A)):
            if A[j] != B[i+j]:
                cnt += 1
        ans.append(cnt)

    print(min(ans))