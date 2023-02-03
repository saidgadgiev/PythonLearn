# Суммы четвертей 
# i = строки  j = столбцы  
# m = стрка n = столбец
n=int(input())
matrix=[]
for _ in range(n):
    l= input().split()
    matrix.append(l)
#print(matrix)
tot1=0 # Верхняя четверть
tot2=0 # Правая четверть
tot3=0 # Нижняя четверть
tot4=0 # Левая четверть
if n > 2:

    for i in range (n):
        for j in range (n):

            # Верхняя четверть
            if i < j and i < n-1-j: 
                res = int(matrix[i][j])
                tot1 += res
            
            # Правая четверть
            if i < j and i > n-1-j: 
                res = int(matrix[i][j])
                tot2 += res

            # Нижняя четверть
            if i > j and i > n-1-j: 
                res = int(matrix[i][j])
                tot3 += res

            # Левая четверть
            if i > j and i < n-1-j: 
                res = int(matrix[i][j])
                tot4 += res
    print('Верхняя четверть:', tot1)
    print('Правая четверть:', tot2)
    print('Нижняя четверть:', tot3)
    print('Левая четверть:', tot4)
else:
    print('Верхняя четверть:', 0)
    print('Правая четверть:', 0)
    print('Нижняя четверть:', 0)
    print('Левая четверть:', 0)
    