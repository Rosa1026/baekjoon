a = int(input("100000 이하의 자연수 N을 입력하세요:\n"))
i = 1
if a <= 100000:
    while i <= a:
        print(i)
        i += 1

else :
    input("다시 입력해주세요\n")