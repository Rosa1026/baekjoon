num_lst = list(range(1, 10001))
answer_lst = []

for i in num_lst:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        answer_lst.append(i)

for i in set(answer_lst):
    num_lst.remove(i)

for i in num_lst:
    print(i)