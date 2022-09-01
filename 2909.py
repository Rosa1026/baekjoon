import sys

C, K = map(int, sys.stdin.readline().split())
A = 10**K

if K == 0:
    print(C)

else:
    if C % A >= A/2:
        print(((C//A)+1)*A)
    else:
        print((C//A)*A)