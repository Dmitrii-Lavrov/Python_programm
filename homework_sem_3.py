# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# data = [2, 3, 5, 9, 3]
# def f(data):
#     '''
#     Функция считает сумму элементов списка, находящихся на нечетных позициях
#     Params:
#     data - заданный список
#     '''
#     sum = 0
#     for i in range(len(data)):
#         if i % 2 > 0:
#             sum += data[i] 
#     return sum    
# print(f"{data} -> {f(data)}")
    


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]

# data =[2, 3, 4, 5, 6]
# def f(data):
#     '''
#     Функция формирует список из произведений пар чисел заданного списка.(Парой считаем первый и последний элемент, второй и предпоследний и т.д.)
#     Params:
#     data - заданный список
#     '''
#     new_list =[]
#     result = 1
#     if len(data) % 2 == 0:
#         for i in range(int(len(data)/2)):
#             result = data[i] * data[len(data) - 1 - i]
#             new_list.append(result)
#     else:
#         for i in range(int(len(data)/2 + 1)):
#             result = data[i] * data[len(data) - 1 - i]
#             new_list.append(result)
#     return new_list
# print(f"{data} => {f(data)}")


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# data = [1.1, 1.2, 3.1, 5, 10.01]
# def difference(data):
#     '''
#     Функция находит разность между максимальной и минимальной дробной части чисел из заданного списка
#     params:
#     data - заданный список
#     '''
#     data_min = data[0] - int(data[0])
#     data_max = data_min
#     for i in data:
#         l = i - int(i)
#         if 0 < l < data_min:
#             data_min = l
#         elif l > data_max:
#             data_max = l
#     result = round((data_max - data_min), 2)
#     return result
# print(f"{data} => {difference(data)}")



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#  45 -> 101101
#  3 -> 11
#  2 -> 10

# number = int(input("Введите число: "))
# def binary(n:int):
#     '''
#     Преобразование десятичного числа в двоичное.
#     params:
#     n - десятичное число
#     '''
#     if n == 1:
#         print(n, end='')
#     else:
#         binary(n//2)
#         print(n % 2, end='')
# binary(number)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input("Введите число: "))
def fib(N):
    '''
    Функция формирует список из чисел Фибоначчи для положительных элементов.
    params:
    N - количество элементов 
    '''
    data = [0, 1]
    for i in range(2, N+1):
        data.append(data[i-1] + data[i-2] )
    return data
print(fib(N))
def negativ_fib(data):
    '''
    Функция формирует список Фибонначи, в том числе из отрицательных элементов.
    Params: 
    data - список Фибонначи для положительных элементов
    '''
    if len(data) % 2 != 0:
        negativ_data = [- data[len(data)-1], data[len(data)-2]]
    else:
        negativ_data = [data[len(data)-1], - data[len(data)-2]]
    for i in range(2, 2*(len(data)-1)+1):
        negativ_data.append(negativ_data[i-1] + negativ_data[i-2] )
    return negativ_data
print(negativ_fib(fib(N)))


