# Таблица умножения
r, c =4, 6
matrix=[]
for row in range(r):
    l=[]
    for cols in range(c):
        l.append(cols * row)    
    matrix.append(l)

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=' ')
    print()