import sys

def prime(n):
    if n == 1:
        return False

    for j in range(2,int(n**0.5)+1):
        if n % j == 0:
            return False
    return True

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    n1 = N // 2
    n2 = N // 2

    while n1 > 0:
        if prime(n1) and prime(n2):
            print(n1, n2)
            break

        else:
            n1 -= 1
            n2 += 1