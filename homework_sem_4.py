# Задайте натуральное число N. Напишите программу, которая составит список простых
#  множителей числа N.
N = int(input("Введите число: "))
list = []
def is_prime(x):
    '''
    Функция проверяет простое число или нет
    params: x - число, которое необходимо проверить
    '''
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return x
for i in range(2, (N // 2) + 1):
    if N % i == 0:
        if is_prime(i) != False:
            list.append(is_prime(i))
print(list)



# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# list = [1,1,1,1,2,2,2,3,3,3,4]
# def f(list):
#     '''
#     Функция выводит список из неповторяющихся элементов, заданного списка
#     params:
#     list - заданный список
#     '''
#     new_list = list[:1]
#     for i in range(1,len(list)):
#         if list[i] != list[i-1]:
#             new_list.append(list[i])
#     return new_list
# print(f(list))



# В файле, содержащем фамилии студентов и их оценки, изменить на прописные 
# буквы фамилии тех студентов, которые имеют средний балл более «4».

# with open('file.txt', 'r', encoding ='utf-8') as data:
#     str = ''
#     for line in data:
#         if "5" in line:
#             str += line.upper()
#         else:
#             str += line   
# with open('file.txt', 'w', encoding ='utf-8') as data:
#     for i in str:
#         data.write(i)



# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
# которая спрашивает ключ, считывает текст и дешифровывает его.

# from encodings import utf_8

# text = str(input("Введите текст: "))
# key = int(input("Введите ключ в диапазоне от 0 до 150: "))
# while key > 150 or key <= 0:
#     key = int(input("Введите ключ в диапазоне от 0 до 150: "))


# def cryption(text, key):
#     alpha = ' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя\
#     ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!"№;%:?*()_+=-\.,<>/[]'
#     cryption_text = ''
#     for i in text:
#         cryption_text += alpha[(alpha.index(i)+key)-len(alpha)]
#         with open('file.txt', 'w', encoding='utf-8') as data:
#             data.write(cryption_text)


# def decryption(key):
#     alpha = ' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя\
#     ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!"№;%:?*()_+=-\.,<>/[]'
#     with open('file.txt', 'r', encoding='utf-8') as data: 
#         for line in data:   
#             cryption_text = str(line)
#     decryption_text = ''
#     for i in cryption_text:
#         decryption_text += alpha[alpha.index(i)-key]
#     return decryption_text

# cryption(text,key)   
# key = int(input("Введите ключ: "))
# print(decryption(key))


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# # AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool

# from asyncore import write

# def rle(file):
#     '''
#     Функция принимает на вход текст из файла и сжимает его.
#     params: 
#     file - файл с исходным текстом
#     '''
#     with open(file, 'r') as file:
#         for line in file:
#             text = line
#     result = ''
#     current = text[0]
#     count = 1
#     for i in text[1:]:
#         if i == current:
#             count += 1
#         else:
#             result = result + str(count) + current
#             current = i
#             count = 1
#     result += str(count) + current
#     with open('file2.txt', 'w') as file:
#         file.write(result)
#     print(f'Исходный текст: {text}')
#     print(f'Сжатый текст: {result}')
  
# def de_rle(file):

#     '''
#     Функция принимает на вход файл со сжатым текст и выдает востановленный.
#     params: 
#     file -файл со сжатым текстом
#     '''
#     with open(file, 'r') as file:
#             for line in file:
#                 text = line    
#     n = ''
#     count = ''
#     for i in text:
#         if i.isdigit():
#             count += str(i) 
#         else:    
#             n += str(int(count)*i)
#             count = ''
#     return n

# rle('file1.txt')
# print(f'Востановленный текст: ' + de_rle('file2.txt'))

