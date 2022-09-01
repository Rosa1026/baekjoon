test = input("테스트 케이스 개수\n")

test_int = int(test)

input_n = []

i = 0
j = 0
check = 2
E = 0
F = 0

while i < test_int:
    B = int(input("4와 10000 사이의 짝수 n을 입력하세요.\n"))

    if(B % 2 == 1):
        print("잘못 입력하셨습니다.")
        B = int(input("4와 10000 사이의 짝수 n을 입력하세요.\n"))
        while B < 4 or B > 10000:
            print("잘못 입력하셨습니다.")
            B = int(input("4와 10000 사이의 짝수 n을 입력하세요.\n"))

    else:
        while B < 4 or B > 10000:
            print("잘못 입력하셨습니다.")
            B = int(input("4와 10000 사이의 짝수 n을 입력하세요.\n"))

    input_n.append(B)
    i+=1

i = 0

while i < test_int:
    num1 = int(input_n[i]/2)
    num2 = int(input_n[i]/2)

    while check > 0:
        for j in range(2, num1-1):
            if num1 == 2 or num1 == 3:
                break

            if num1 % j == 0:
                num1 -= 1
                continue
        check -= 1

        for j in range(2, num2-1):
            if num2 % j == 0:
                num2 += 1
                continue
        check -= 1

        if num1 + num2 == int(input_n[i]):
            break
        else :
            num1 -= 1
            check = 2

    print(num1, num2)
    check = 2
    i+=1