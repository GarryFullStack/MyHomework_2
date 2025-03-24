import random  
n = int(input ("Введите число строк "))
m = int(input ("Введите число столбцов "))
matrix_1 = [[random.randint(-50, 200) for _ in range(n)] for _ in range(m)]  
matrix_2 = [[random.randint(-50, 200) for _ in range(n)] for _ in range(m)]  
print('matrix_1')  
for row1 in matrix_1:  
    print(*row1)  
print('matrix_2')    
for row2 in matrix_2:  
    print(*row2)  
matrix_3 = [[0 for _ in range(n)] for _ in range(m)]  
for i in range(n):  
    for j in range(m):  
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]  
print('matrix_3')  
for row3 in matrix_3:  
    print(*row3)  




































