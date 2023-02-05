# Заполнение змейкой
# На вход программе подаются два натуральных числа nn и mm. 
# Напишите программу, которая создает матрицу размером n×m 
# заполнив её "змейкой" в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных 
# числа nn и mm — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах, отводите 
# ровно 33 символа на каждый элемент. Для этого используйте строковый 
# метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

# Sample Input 2:
# 5 5
# Sample Output 2:
# 1  2  3  4  5
# 10 9  8  7  6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25

s = "2 2".split()
count = 1
n,m = s[0], s[1]
matrix=[]
for r in range(int(n)):
    lis=[]
    for c in range(int(m)):
        lis.append(count)
        count = count+1
    matrix.append(lis)
for r in range(int(n)):
    if r%2!=0:
        matrix[r].reverse()
for r in range(int(n)):
    for c in range(int(m)):
        print(str(matrix[r][c]).ljust(3), end=" ")
    print()

#     Решение 1

#     n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#     if i % 2:
#         matrix[i].reverse()

# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()
