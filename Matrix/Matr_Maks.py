# Матрица. Максимальный в области 1
n=3
matrix=[]
for _ in range(n):
    l= input().split()
    matrix.append(l)
print(matrix)
tot=-999
for i in range(n):
    for j in range(n):
        if j <=i:
            res = int(matrix[i][j])
            if res >= tot:
                tot = res
print(tot)