# Максимальный в области 2 
# i = строки  j = столбцы  
# m = стрка n = столбец
n=int(input())
matrix=[]
for _ in range(n):
    l= input().split()
    matrix.append(l)
#print(matrix)
tot=-999
if n > 2:

    for i in range (n):
        for j in range (n):
            if i >= j and i <= n-1-j or i<=j and i >= n-1-j:
                res = int(matrix[i][j])
                if res >= tot:
                    tot = res
    print(tot)
else:
    for i in range (n):
        for j in range (n):
            res = int(matrix[i][j])    
            if res >= tot:
                tot = res
    print(tot)