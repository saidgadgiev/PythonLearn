# Магическим квадратом порядка nn называется квадратная таблица размера 
# n×n, составленная из всех чисел 1, 2, 3,... так, что суммы по каждому 
# столбцу, каждой строке и каждой из двух 
# диагоналей равны между собой. Напишите программу, которая проверяет, 
# является ли заданная квадратная матрица магическим квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и 
# столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в 
# каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим 
# квадратом, и слово NO в противном случае.

# Sample Input 1:   Sample Output 1:    Sample Input 2: Sample Output 2:


# 3                 YES                 3               NO
# 8 1 6                                 8 2 6
# 3 5 7                                 3 5 7
# 4 9 2                                 4 9 1

# 4+5+6 = 15
# 7+8+9+10 = 34
# 11+12+15+16+17 = 65
# 18+19+20+21+22+23 = 111
# 24+25+26+27+28+29+30 = 175

num = 3
matrix = [["8", "1", "6"],
        ["3", "5", "7"],
        ["4", "9", "2"]
        ]
for r in range (len(matrix)):
    for c in range(len(matrix)):
        matrix[r][c] = int(matrix[r][c])
def magic_square(matrix, cols):
    sum_main_diag = 0
    sum_semi_diag = 0
    check = []


    for i in range(cols):                                # заполняем проверочный список всеми элементами матрицы
        check += matrix[i]

    for i in range(1, len(check) + 1):                   # проверяем проверочный список на наличие всех чисел в промежутке от 1 до n ** 2
        if i not in check:
            return print("NO")                           # если нет какого-то числа, то значит дальше нет смысла проверять равенство, завершаем с NO

    for i in range(cols):                                # проверяем равенство диагоналей
        sum_main_diag += matrix[i][i]
        sum_semi_diag += matrix[i][cols - 1 - i]

    for i in range(cols):                                # проверяем равенство строк, столбцов и диагоналей
        sum_cols = 0
        sum_rows = 0
        for j in range(cols):
            sum_cols += matrix[i][j]
            sum_rows += matrix[j][i]
        if not sum_cols == sum_rows == sum_main_diag == sum_semi_diag:
            return print("NO")                           # если что-то не равно, завершаем с NO
    else:
        return print("YES")                              # если всё хорошо, завершаем с YES

magic_square(matrix, num)

# Другие решения

# n = int(input()); m = []; b=[]
# for i in range(n):
#     a = [int(j) for j in input().split()]
#     m.append(a)
#     b += a
# t = 'YES'    
# if sorted(b) != list(range(1, n**2 + 1)): t = 'NO' 
# mm = [[m[i][j] for i in range(n)] for j in range(n)]
# s = sum(m[0])
# for i in range(n):
#     if sum(m[i]) != s or sum(mm[i]) != s:
#         t = 'NO'
#         break
# print(t)

# Решение 2

# n = int(input())
# mt = [[int(x) for x in input().split()] for _ in range(n)]

# def test(mt):
#     n = len(mt)
#     t1 = [1]*(n**2)
#     s = sum(mt[0]) # контрольная сумма
#     s2 = sum(mt[i][i] for i in range(n)) # сумма главной диагонали
#     s3 = sum(mt[i][n-i-1] for i in range(n)) # сумма диагонали
#     for i in range(n):
#         if s != sum(mt[i]): # сумма строк
#             return False
#         if s != sum(mt[k][i] for k in range(n)): # сумма столбцов
#             return False
#         for j in range(n):
#             if mt[i][j] < 1 or mt[i][j] > n*n: # что бы не вылететь на списке t1
#                 return False
#             t1[mt[i][j]-1] = 0 # отмечаем числа 1..n^2
#     if s2 != s or s3 != s or sum(t1):
#         return False
#     return True

# print('YES' if test(mt) else 'NO')
