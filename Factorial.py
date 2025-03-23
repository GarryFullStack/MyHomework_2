m=[]

def factorial(i): 
    if i == 1:
        return 1 
    else: 
        return i * factorial(i - 1)
        
num = int(input('Введите натуральное целое число: '))

for i in range(num):
    m.append(factorial(num - i))
    
print("Обратная последовательность факториалов факториала числа:", num) 
print(m)   
