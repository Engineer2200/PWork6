input_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minimum = int(input('Введите минимальное число:'))
maximum = int(input('Ведите максимальное число:'))

results_list = []
for i in range(len(input_list)):
    if minimum <= input_list[i] <= maximum:
        results_list.append(i)

print(input_list)
print()
print(*results_list)