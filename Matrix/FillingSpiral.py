# Заполнение спиралью 😈😈
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, 
# которая создает матрицу размером n×m заполнив её "спиралью" в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа nn и mm — 
# количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести матрицу в соответствии образцом.

# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 
# 33 символа на каждый элемент. Для этого используйте строковый метод 
# ljust(). Можно обойтись и без ljust(), система примет и такое решение 

# Sample Input 1:
# 4 5
# Sample Output 1:
# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8

s = "3 3".split()
n,m = int(s[0]), int(s[1])


matrix = [[0] * m for _ in range(n)] 
print(matrix)