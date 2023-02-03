# Больше среднего
n = int(input())
l = [input().split() for _ in range(n)]
counter = 0
for i in l:
    sr = (sum(list(map(int, i)))) / len(i)
    for j in i:
        if int(j) > sr:
            counter += 1
    print(counter)
    counter = 0
