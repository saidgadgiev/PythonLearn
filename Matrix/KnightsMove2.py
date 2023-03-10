# Ходы коня 2 вариант решения
# На шахматной доске 8×8 стоит конь. Напишите программу, 
# которая отмечает положение коня на доске и все клетки, 
# которые бьет конь. Клетку, где стоит конь, отметьте 
# английской буквой N, клетки, которые бьет конь, отметьте 
# символами *, остальные клетки заполните точками.

# Формат входных данных
# На вход программе подаются координаты коня на шахматной 
# доске в шахматной нотации (то есть в виде e4, где сначала 
# записывается номер столбца (буква от a до h, слева направо), 
# затем номеру строки (цифра от 11 до 88, снизу вверх)).

# Формат выходных данных
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

# Sample Input 1:

# b6
# Sample Output 1:

# 8 * . * . . . . .
# 7 . . . * . . . .
# 6 . N . . . . . .
# 5 . . . * . . . .
# 4 * . * . . . . .
# 3 . . . . . . . .
# 2 . . . . . . . .
# 1 . . . . . . . .
#   a b c d e f g h

x, y = "h5"

n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'
        
for row in board:
    print(*row)