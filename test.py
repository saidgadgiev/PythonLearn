x, y  = "h5"


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