#     Заполнение 4
# На вход программе подается натуральное число nn. Напишите программу, которая создает 
# матрицу размером n×n заполнив её в соответствии с образцом.

# Формат входных данных
# На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на 
# каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и 
# без ljust(), система примет и такое решение

# Sample Input 1:
# 5
# Sample Output 1:
# 1  1  1  1  1
# 0  1  1  1  0
# 0  0  1  0  0
# 0  1  1  1  0
# 1  1  1  1  1

n = 9
count = n-1
for r in range(n):
    for c in range(n):
        if r <= c <= count:
            print("1".ljust(3), end=" ")
            if c == count:
                count = count -1
        elif r >= c >= count:
            print("1".ljust(3), end=" ")
            if c == count:
                count = count -1
        else:
            print("0".ljust(3), end = " ")
    print()