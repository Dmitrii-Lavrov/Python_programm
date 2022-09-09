# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# N = input("Введите число: ")
# sum = sum(int(i) for i in N if i.isdigit())
# print(sum)



# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# data = []
# n = input("Введите число: ")
# while n.isdigit() == False:
#     print("Вы ввели не число!")
#     n = input("Введите число: ")
# N = int(n)
# x = 1
# fact = 1
# for i in range(1,N+1):
#     while x <= i:
#         fact *= x
#         x += 1
#         data.append(fact)
# print(f"{N} -> {data}")



# Напишите такую программу, которая найдет палиндром введенного пользователем числа.
# a = input("Введите число: ")
# b = ''
# print(a, end= " -> ")
# while a != b:
#     for i in range(len(a)):
#         b += a[-1-i]
#     if a!=b:
#         a = str(int(b) + int(a))     
#         b = ''
# print(a)


# Реализуйте выдачу случайного числа
import datetime
N_min = int(input("Введите минимальное значение: "))
N_max = int(input("Введите максимальное значение: "))
Number = int(datetime.datetime.now().microsecond)
while Number > N_max:
    Number = Number/10 + N_min
print(int(Number))
