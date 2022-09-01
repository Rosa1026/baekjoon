N = int(input())

i = 1
k = 1
S = 0

def first_star(i, S):
    j = 0
    while i < N:
        print(" ", end='')
        i += 1
    print("*", end='')

    if N > 2 and S != 0:
        while j < (2*S-1):
            print(" ", end='')
            j+=1
        print("*", end='')

    print("")

if N == 1:
    print("*", end='')

else:
    while i < N:
        first_star(i, S)
        i += 1
        S += 1

    if i == N:
        while k <= (N*2 - 1):
            print("*", end='')
            k += 1