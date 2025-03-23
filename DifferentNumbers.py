N = int(input("¬ведите количество чисел: "))
numbers = list(map(int, input(f'¬ведите через пробел {N} чисел: ').split()))
number_list = set(numbers)
print(len(number_list))