def progression(a1, d, n: int) -> list:
    result_list = []
    res = 0
    for i in range(1 , n + 1):
        res = a1 + (i - 1) * d
        i +=1
        result_list.append(res)
    return result_list

a1 = int(input('Введите первый элемент массива: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов массива: '))
result_list = progression(a1, d , n)
print(result_list)