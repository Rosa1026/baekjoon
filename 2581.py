import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

plus = 0
min = 0
cnt = 0

for i in range(M, N+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error +=1

        if error == 0:
            plus += i
            cnt += 1

        if cnt == 1 and error == 0:
            min += i
if min == 0:
    print('-1')
else:
    print(plus)
    print(min)