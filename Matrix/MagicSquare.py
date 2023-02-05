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

num = 3
bul = "YES"
matrix = [[8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
        ]
patter = sum(matrix[0])

def SumMath(matrix, patt, bul):
    for r in range (len(matrix)):
        if patt == sum(matrix[r]):
            bul = "YES"
        else:
            bul = "NO"
            break
    return bul

def MatrRotation(matrix, n):
    MatrR = []
    for r in range (len(matrix)):
        lis = []
        # count = n-1
        for c in range (len(matrix)):
            lis.append(matrix[count][r]) 
            count = count -1
        MatrR.append(lis)
    return MatrR

def MatrDioganal(matrix):
    MatrR1 = []
    MatrR2 = []
    count = len(matrix)-1
    for r in range(len(matrix)):
        lis1 = []
        lis2 = []
        for c in range(len(matrix)):
            if r == c:
                lis1.append(matrix[r][c])
                print(lis1)
            if c == count:
                lis2.append(matrix[r][c])
                print(lis2)
                count = count -1
        MatrR1.append(lis1)    
        MatrR2.append(lis2)
    MatrR1.append(MatrR2)
    print (MatrR1)


MatrDioganal(matrix)