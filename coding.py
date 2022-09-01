a = 0
M = int(input("테스트 케이스 개수 : "))

while a < M:
    N = int(input())
    K = int(input())

    print("수열 갯수는 %d이다."%(N))
    print("라운드 수는 %d이다."%(K))

    w = []
    x = []
    y = []
    z = []
    i = 0
    j = 0
    q = 0
    ans = 1
    num = 0
    answer = []

    while i < N:
        X = int(input())
        x.append(X)
        i += 1
    print(x)

    while j < K:
        Y = input()
        y.append(Y)
        W = int(input())
        w.append(W)
        Z = int(input())
        z.append(Z)
        j += 1

    while num < len(y):
        print(y[num], w[num], z[num])
        num += 1

    num = 0

    while num < len(y):
        q = w[num]
        if y[num] == 'C':
            x[w[num]-1] = z[num]
        elif y[num] == 'P':
            if q == z[num]:
                ans *= x[q-1]
            else:
                while q <= z[num]:
                    ans *= x[q-1]
                    q += 1

            if ans > 0 :
                answer.append("+")
            elif ans < 0 :
                answer.append("-")
            else :
                answer.append("0")
        print(ans)
        num += 1
        ans = 1

    print(answer)
    a += 1