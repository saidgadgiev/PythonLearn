# Ходы коня
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

def PrintMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            print(matrix[r][c], end=' ')
        print()

def KnightMove(matrix, pos):
    print(pos[0]+2, pos[1]+1)
    if (pos[0]+2 >= 0 and pos[0]+2 <= 7) and pos[1]+1 <= 7:
        matrix[pos[0]+2][pos[1]+1] = '*' # 1 пра 2 вниз
    if pos[0]-2 >= 0 and pos[1]+1 <= 7:
        matrix[pos[0]-2][pos[1]+1] = '*' # 1 пра 2 верх
    if (pos[0]+2 >= 0 and pos[0]+2 <= 7) and pos[1]-1 >= 0:
        matrix[pos[0]+2][pos[1]-1] = '*' # 1 лев 2 вниз
    if pos[0]-2 >= 0 and pos[1]-1 >= 0:
        matrix[pos[0]-2][pos[1]-1] = '*' # 1 лев 2 верх
    if (pos[0]+1 >= 0 and pos[0]+1 <= 7) and pos[1]+2 <= 7:
        matrix[pos[0]+1][pos[1]+2] = '*' # 2 пра 1 вниз
    if pos[0]-1 >= 0 and pos[1]+2 <= 7:
        matrix[pos[0]-1][pos[1]+2] = '*' # 2 пра 1 верх
    if (pos[0]+1 >= 0 and pos[0]+1 <= 7) and pos[1]-2 >= 0:
        matrix[pos[0]+1][pos[1]-2] = '*' # 2 лев 1 вниз
    if pos[0]-1 >= 0 and pos[1]-2 >= 0:
        matrix[pos[0]-1][pos[1]-2] = '*' # 2 лев 1 верх

    return matrix
    

xy = "h5"
x = xy[0]
y = xy[1]
matrix = []
board_ch = '.'
number = {'1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0} # строки
character ={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7} # столбцы
for r in range(8):
    lis = []
    for c in range(8):
        lis.append(board_ch)
    matrix.append(lis)

matrix[number[y]][character[x]] = 'N'
PosN = number[y],character[x]
print (PosN)
KnightMove(matrix, PosN)
PrintMatrix(matrix)

