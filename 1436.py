import sys

N = int(sys.stdin.readline())
cnt = 0
six = 666
while True:
    if '666' in str(six):
        cnt += 1
    if cnt == N:
        print(six)
        break
    six += 1