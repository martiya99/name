#На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
#Ваша задача написать условную конструкцию (из if, elif, else), 
#которая выводит кол-во одинаковых чисел среди 3-х введённых.
first = int(input('Введите число №1: '))
second = int(input('Введите число №2: '))
third = int(input('Введите число №3: '))
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')