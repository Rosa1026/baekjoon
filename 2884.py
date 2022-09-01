import sys

H, M = [int(x) for x in sys.stdin.readline().split()]

if M >= 45:
    M -= 45
    print(H, end=' ')
    print(M)

else:
    if H == 0:
        H = 23
        M += 15
        print(H, end=' ')
        print(M)

    else:
        H -= 1
        M += 15
        print(H, end=' ')
        print(M)