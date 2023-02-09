# Сложение матриц
# Напишите программу для вычисления суммы двух матриц.

# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк 
# и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, 
# далее следуют элементы второй матрицы.

# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

# Sample Input 1:
# 2 4
# 1 2 3 4
# 5 6 7 1

# 3 2 1 2
# 1 3 1 3
# Sample Output 1:
# 4 4 4 6
# 6 9 8 4
# ---------------
# for _ in range(n):
#     l= input().split()
#     matrix.append(l)


s = "2 4".split()
n, m = int(s[0]), int(s[1])
matrix_1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 1]
]
matrix_2 = [
    [3, 2, 1, 2],
    [1, 3, 1, 3]
]
for r in range(n):
    for c in range(m):
        matrix_1[r][c] = matrix_1[r][c]+matrix_2[r][c]

for row in matrix_1:
    print(*row)


# n, m = [int(i) for i in input().split()]
# matrixA = [[int(i) for i in input().split()] for _ in range(n)]
# input()
# matrixB = [[int(i) for i in input().split()] for _ in range(n)]
# matrixC = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

# for row in matrixC:
#     print(*row)