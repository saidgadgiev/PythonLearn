# Побочная диагональ
# На вход программе подается натуральное число nn. Напишите 
# программу, которая создает матрицу размером n \times nn×n 
# и заполняет её по следующему правилу:

# числа на побочной диагонали равны 11;
# числа, стоящие выше этой диагонали, равны 00;
# числа, стоящие ниже этой диагонали, равны 22.
# Полученную матрицу выведите на экран. Числа в строке 
# разделяйте одним пробелом.

# Формат входных данных
# На вход программе подается натуральное число nn — количество 
# строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести матрицу в соответствии с условием задачи.

# Примечание. Побочная диагональ — это диагональ, идущая из правого 
# верхнего в левый нижний угол матрицы.

# Тестовые данные 
# Sample Input 1:

# 4
# Sample Output 1:

# 0 0 0 1
# 0 0 1 2
# 0 1 2 2
# 1 2 2 2

n = 4
count = n-1
for r in range(n):
    for c in range(n):
        if count == c:
            print(1, end= " ")
            count = count -1
        elif count>c:
            print(0, end= " ")
        else:
            print(2, end= " ")

    print()