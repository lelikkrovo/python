# a = int(input())
# b = int(input())
# print(f'{a} + {b} = {a+b}')

# x, y = int(input()), int(input())
# y = y % x
# print(x - y)

# x = int(input())
# s = 100000 * (1 + 10) ** x
# print(round(s))

# x = int(input())
# s = 100000 * (1 + 0.1/12) ** (x * 12)
# print(round(s))

# greet = input()
# print(f'Hello, my name is {greet} ')

# s = 'foo-bar-baz'
# '-'.join(s.split('-'))

# x = input()
# print(x[:len(x)//2])


# x = input()
# x1 = x[::-1]
# if x == x1:
#    print('YES')
# else:
#    print('NO')


# x = input()
# list(x)
# print(list(x))


# s = int(input()) деление с округление вверх
# p = 4
# print((s + p -1) // p)


# x = int(input())
# 1 = x // 60
# y = x % 60
# print(f'{x} мин - это {x1} час {y} минут.')

# num = 17 Получить любую из цифр в числе
# a = num % 10
# b = num // 10
# print(a, b)

# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
# print(a, b, c)

# Последняя цифра: (num % 101) // 100;
# Предпоследняя цифра: (num % 102) // 101;
# Предпредпоследняя цифра: (num % 103) // 102;
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.


# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Сумма цифр =', last_digit + first_digit)
# Число, образованное при перестановке цифр двузначного числа.
# print('Искомое число =', last_digit * 10 + first_digit)

# Выводит на экран цифры (через запятую).
# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(digit1, digit2, digit3, sep=',')

# Рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# num = int(input())
# digit1 = num % 10
# digit2 = (num // 10) % 10
# digit3 = num // 100
# print(f'Сумма цифр = {digit3 + digit2 + digit1}')
# print(f'Произведение цифр = {digit3 * digit2 * digit1}')

# num = int(input())
# digit1 = num % 10
# digit2 = (num // 10) % 10
# digit3 = (num // 100) % 10
# digit4 = num // 1000
# print(f'Цифра в позиции тысяч равна {digit4}')
# print(f'Цифра в позиции сотен равна {digit3}')
# print(f'Цифра в позиции десятков равна {digit2}')
# print(f'Цифра в позиции единиц равна {digit1}')

# Сумма квадрата и квадрат суммы
# a = int(input())
# b = int(input())
# s = (a + b) ** 2
# s1 = a ** 2 + b ** 2
# print(f'Квадрат суммы {a} и {b} равен {s}')
# print(f'Сумма квадратов {a} и {b} равна {s1}')


# Подсчет четных чисел
# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0 #переменная счетчик
# if num1 % 2 == 0:
#    counter = counter + 1 #увеличиваем счетчик на 1
# if num2 % 2 == 0:
#    counter = counter + 1 #увеличиваем счетчик на 1
# if num3 % 2 == 0:
#    counter = counter + 1 #увеличиваем счетчик на 1
# print(counter)

# четное нечетное
# number = int(input())
# if number % 2 == 0:
#    print('Четное')
# else:
#    print('Нечетное')

# Сумма первой и последней цифр равна разности второй и третьей цифр.
# number = int(input())
# number1 = number % 10
# number2 = (number // 10) % 10
# number3 = (number // 100) % 10
# number4 = number // 1000
# if number4 + number1 == number3 - number2:
#     print('ДА')
# else:
#     print('НЕТ')


# num = int(input())
# if num < 18:
#     print('Доступ запрещен')
# else:
#     print('Доступ разрешен')

# Определяет арифметическую последовательность
# num1, num2, num3 = int(input()), int(input()), int(input())
# if num2 - num1 == num3 - num2:
#     print('YES')
# else:
#     print('NO')

# наименьшее число
# num1, num2 = int(input()), int(input())
# if num1 > num2:
#     print(num2)
# else:
#     print(num1)

# Определяет наименьшее из четырёх чисел.
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a < b:
#     x = a
# else:
#     x = b
# if c < d:
#     y = c
# else:
#     y = d
# if x < y:
#     print(x)
# else:
#     print(y)

# Определяем возростную группу
# e = int(input())
# if e <= 13:
#     print('детство')
# if 14 <= e <= 24:
#     print('молодость')
# if 25 <= e <= 59:
#     print('зрелость')
# if 60 <= e:
#     print('старость')

# Cчитывает три числа и подсчитывает сумму только положительных чисел.
# a, b, c = int(input()), int(input()), int(input())
# if a > 0:
#     x = a
# else:
#     x = 0
# if b > 0:
#     y = b
# else:
#     y = 0
# if c > 0:
#     z = c
# else:
#     z = 0
# print(x + y + z)

# Из отрицательного делает положительное / без условия else
# x = int(input())
# if x < 0:
#     x = -x
# print(x)

# високосный год
# n = int(input())
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# Второй вариан решения для високосного года
# n = int(input())
# if n % 100 == 0:
#     if n % 400 == 0:
#         print('YES')
#     else:
#         print('NO')
#
# else:
#     if n % 4 == 0:
#         print('YES')
#     else:
#         print('NO')

# Третий вариант решения задачи
# n = int(input())
# if n % 400 == 0:
#     print('YES')
# elif n % 100 == 0:
#     print('NO')
# elif n % 4 == 0:
#     print('YES')
# else:
#     print('NO')


# Задача с арбузами (сравнить и выбрать большее)
# a, b, c = int(input()), int(input()), int(input())
# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a > b:
#     m = a
# else:
#     m = b
# if c > m:
#     m = c
# if d > m:
#     m = d

# Задача шахматы / 2 варианта ладья
# 1 вариант
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')
# 2 вариант ладья
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')

# Деление с остатком 0 <= r <= d в конце остоток будет меньше b
# a = b * q + r
#
# a - исходное количисто яблок
# b - количество школьников
# q - сколько досталось каждому
# r - статок
#
# n = int(input())
# r = 1
# k = 50
# s = (100 * r + k) * n
# print(f'Рублей - {s // 100}, копеек - {s % 100}')

# n = int(input())
# r = 1
# k = 50
# s = (60 * r + k) * n
# print(f'Рублей - {s // 100}, копеек - {s % 100}')

# k = int(input()) #количество уроков
# t = 45 * k + 10 * (k - 1) #время урока в минутах, 45 - урок, 10 - перемена
# h = t // 60 #часы
# m = t % 60 #минуты
# print(h + 9, m) #урок начинается с 9:00

# дни, часы, минуты, секунды
# t = s + m * 60 + h * 60 * 60 + d * 24 * 60 * 60
# #обратная задача #n % 2 = 0 - четное число
# t =
# d = t // (24 * 60 * 60)
# t %= (24 * 60 * 60) #Количество секунд после того как отбросили дни
# h = t % (60 * 60)
# t %= 60 * 60
# m = t // 60
# s = t % 60

# Задача бро байкера s // 109, s % 109,
# Если отрицательное число, S = q * l +r и 0 <= r < l,
# -1  = -1 * 109 + 108, 0 <= r <= 109
# s = 100 * r + c  s - общая сумма в рублях о копейках.

# (s + p - 1) //s

# v, t = int(input()), int(input())
# s = v * t
# print(s % 109)

# задача со сломаными часами
# x1, y1, a1, b1, x2, y2 = int(input()), int(input()), int(input()),int(input()), int(input()), int(input())
# t = (x2 * 60 + y2 - (x1 * 60 + y1)) % (24 * 60)
# start = a1 * 60 + b1
# end = start + 2 * t
# print(end // 60 % 24, end % 60)


# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and b == c:
#     print(3)
# elif a == b or a == c or b ==c:
#     print(2)
# else:
#     print(0)

# Словарь
# MLB_team = dict ([
#     ('Colorado', 'Rockies'),
#     ('Boston', 'Red Sox'),
#     ('Minnesota', 'Twins')
# ])
# print(MLB_team['Colorado'])


# x = int(input())
# if x < 0:
#     print(-1)
# elif x > 0:
#     print(1)
# else:
#     print(0)

"""Программа, которая будет получать на вход количество,
а выводить это число и правильное склонение слова
("student", "studenta", "studentov")."""
# x = int(input())
# if x % 10 in (0, 5, 6, 7, 8, 9) or x % 100 in (11, 12, 13, 14):
#     print(f'{x} studentov')
# elif x % 10 in (2, 3, 4):
#     print(f'{x} studenta')
# elif x % 10 in (1,):
#     print(f'{x} student')

# a, b, c = int(input()), int(input()), int(input())
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)


# y, x = int(input()), int(input())
# column = y
# line = x
# if 8 > column > 1 and 8 > line > 1:
#     print(8)
# elif column < 2 and line < 2:
#     print(3)
# elif column > 7 and line > 7:
#     print(3)
# else:
#     print(5)


"""Напишите программу, которая считывает координаты точки и
радиус окружности и определяет попадает ли точка внутрь 
окружности с заданным радиусом, центр которой находится в
центре координат."""
# x, y , r = float(input()), float(input()), float(input())
# if x ** 2 + y ** 2 <= r ** 2:
#     print('YES')
# else:
#     print('NO')

# вывести квадрат каждого члена числа в обратном порядке
# x = int(input())
# while x > 0:
#     digit = x % 10
#     print(digit ** 2)
#     x //= 10

# неизвестное число, в конце строки написано 'end'
# line = input()
# while line != 'end':
#     #обработка
#     num = int(line)
#     print(num ** 2)
#     #переход к следующей итерации
#     line = input()
# print('33')

# найти число цифр 1 в его двойной записи
# x = int(input())
# s = 0
# while x > 0:
#     bindigit = x % 2
#     s += bindigit # if bindigit == 1:
#     x //= 2            #s += 1
# print(s)

# l = [1, 2, 3, 4, 5]
# for x in l:
#     print(x ** 2)

# генератор, range - генерирует арифметические прогрессии
# 1) range(N) 0, 1, 2, 3...,N-1
# 2) range(a, b) a, a + 1, a + 2..., b - 1
# 3) range(a, b, d) a, a + d, a + 2d, a + 3d, (a + n * d) #< b
# for x in range():
#     print(x ** 2)

# от 1 до 100
# range(1, 101)
# #от 100 до 1
# range(100, 0, -1)
# #четные числа от 1 до 100
# range(2, 101, 2)


# квадрат суммы
# n = int(input())
# s = 0
# for x in range(1, n + 1):
#     s += x ** 2
# print(s)

# поиск факториала
# N = int(input())
# factorial = 1
# for x in range(1, N + 1):
#     factorial *= x
# print(factorial)

# арифметическая прогрессия
# s = 0
# d = 1
# a = float(input())
# n = int(input())
# for i in  range(0, n + 1):
#     s += d
#     d *= a
# print(s)

# принадлежат ли точки к одной координатной четверти
# y, x, y1, x1 = float(input()), float(input()), float(input()), float(input())
# if y > 0 and x > 0 and y1 > 0 and x1 > 0:
#     print('YES')
# elif y > 0 and x < 0 and y1 > 0 and x1 < 0:
#     print('YES')
# elif y < 0 and x < 0 and y1 < 0 and x1 < 0:
#     print('YES')
# elif y < 0 and x > 0 and y1 < 0 and x1 > 0:
#     print('YES')
# else:
#     print('NO')


# принадлежат ли точки к одной координатной четверти
# a, b = float(input()), float(input())
# if a > 0 and b > 0:
#     print('1')
# elif a < 0 and b < 0:
#     print('3')
# elif a > 0 and b < 0:
#     print('4')
# elif a < 0 and b > 0:
#     print('2')

# Классическая задача "Fizz Buzz".
# i = int(input())
# if i % 3 == 0 and i % 5 == 0:
#     print('Fizz Buzz')
# elif i % 3 == 0:
#     print('Fizz')
# elif i % 5 == 0:
#     print('Buzz')
# else:
#     print(i)

# a, b, c = int(input()), int(input()), int(input())
# max_digit = max(a, b, c)
# min_digit = min(a, b, c)
# middle_digit = max_digit - min_digit
# print(min_digit)
# print(middle_digit)
# print(max_digit)


# list_strings = []
# base_number = None
#
# while True:
#     current_str = input()
#     if current_str != '.':
#         list_strings.append(current_str)
#         continue
#
#     base_number = float(input())
#     break
#
# for s_i in list_strings:
#     op, n_i.split()[0], float(s_i.split()[1])
#     if op == '+':
#         base_number += n_i
#     elif op == '-':
#         base_number -= n_i
#     elif op == '*':
#         base_number *= n_i
#     else:
#         base_number /= n_1
#
# print(base_number)


# list_strings = []
# base_number = None
#
# while True:
#     current_str = input()
#     if current_str != '.':
#         list_strings.append(current_str)
#         continue
#
#     base_number = float(input())
#     break
#
# for s_i in list_strings:
#     op, n_i.split()[0], float(s_i.split()[1])
#     if op == '+':
#         base_number += n_i
#     elif op == '-':
#         base_number -= n_i
#     elif op == '*':
#         base_number *= n_i
#     else:
#         base_number /= n_1
#
# print(base_number)

# шахматы. узнать к черной или белой относится координата
# x, y = int(input()), int(input())
# if (x + y) % 2 == 0:
#     print('BLACK')
# else:
#     print('WHITE')

# шахматы. как ходит король с учетом топтания на месте
# x, y, x1, y1 = int(input()), int(input()), int(input()), int(input())
# if 1 <= (x - x1) ** 2 + (y - y1) ** 2 <= 2:
#     print('YES')
# else:
#     print('NO')


# x = int(input())
# if x > -30 and x <= -2 or x > 7 and x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# четырехзначным и делится нацело на 7 или на 17
# x = int(input())
# if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
# if a * c <= a * b + b * c:
#     print('YES')
# else:
#     print('NO')

# x = int(input())
# if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# принцип работы for, результат - 1 3 6 10 15 21
# total = 0
# for i in range(1, 7):
#     total += i
#     print(total, end=' ')

# n = int(input())
# total = 0
# for i in range(1, n):
#     if (i * i % 10) in [2, 5, 8]:
#         total += i
# print(total)

# на вход число месяца, на выход количество дней в месяце
# x = int(input())
# if x == 2:
#     print(28)
# elif x == 4 or x == 6 or x == 9 or x == 11:
#     print(30)
# else:
#     print(31)

# узнать к какой весовой котегории относится боксер
# x = int(input())
# if x < 60:
#     print('Легкий вес')
# elif 64 > x >= 60:
#     print('Первый полусредний вес')
# elif 64 <= x < 69:
#     print('Полусредний вес')

"""Программа должна вывести результат применения операции к
введенным числам или соответствующий текст, 
если операция неверная либо если происходит деление на ноль."""
# a, b = int(input()), int(input())
# s = input()
# if s == '+':
#     print(a + b)
# elif s == '-':
#     print(a - b)
# elif s == '*':
#     print(a * b)
# elif s == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)
# else:
#     print('Неверная операция')


# a = input()
# b = input()
# if a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or b == 'желтый' and a == 'красный':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or b == 'желтый' and a == 'синий':
#     print('зеленый')
#
# elif a == 'красный' and b == 'красный':
#     print('красный')
# elif a == 'желтый' and b == 'желтый':
#     print('желтый')
# elif a == 'синий' and b == 'синий':
#     print('синий')
#
# else:
#     print('ошибка цвета')

# смешиваем краску, красный, синий, желтый
# a = input()
# b = input()
# if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
#     print('зеленый')
#
# elif a == 'красный' and b == 'красный':
#     print('красный')
# elif a == 'желтый' and b == 'желтый':
#     print('желтый')
# elif a == 'синий' and b == 'синий':
#     print('синий')
#
# else:
#     print('ошибка цвета')

# put your python code here

# рулетка, программа должна вывести цвет кармана либо
# сообщение «ошибка ввода», если введённое число лежит
# вне диапазона от 0 до 36.
# x = int(input())
# 36 >= x >= 0
# if x == 0:
#     print('зеленый')
# elif 28 >= x >= 19 or 10 >= x >= 1:
#     if x % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 18 >= x >= 11 or 36 >= x >= 29:
#     if x % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# else:
#     print('ошибка ввода')


# for i in range(10):
#     print('Hello')

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')



'''Программа должна вывести на экран границы отрезка, 
являющегося пересечением, либо общую точку, либо 
текст «пустое множество».'''
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# a1 < b1 and a2 < b2
# if a1 == a2 and b1 == b2:
#     print(a1, b2)
# elif a1 < a2 and b1 > b2:
#     print(a2, b2)
# elif a2 < a1 and b2 > b1:
#     print(a1, b1)
#
# elif a1 < a2 and b1 == b2:
#     print(a2, b2) #or b1
# elif a1 == a2 and b1 > b2:
#     print(a2, b2) #or a1
# elif a2 < a1 and b1 == b2:
#     print(a1, b1) #or b2
# elif a2 == a1 and b2 > b1:
#     print(a1, b1) #or a2
# elif a1 < a2 and b1 == a2 and b1 < b2:
#     print(b1) #or a2
# elif a2 < a1 and b2 == a1 and b2 < b1:
#     print(b2) #or a1
# elif a1 < a2 and b1 < b2 and a2 < b1:
#     print(a2, b1)
# elif a2 < a1 and b2 < b1 and a1 < b2:
#     print(a1, b2)
# else:
#     print('пуcтое множество')

# покрашены ли в один цвет шахматные клетки
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# от 10-15 девочки
# x = int(input())
# y = input()
# if 15 >= x >= 10 and y == 'f':
#     print('YES')
# else:
#     print('NO')

# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».
# x = int(input())
# if x % 2 != 0:
#     print('YES')
# elif 5 >= x >= 2 % 2 == 0:
#     print('NO')
# elif 20 >= x >= 6 % 2 == 0:
#     print('YES')
# elif x > 20 % 2 == 0:
#     print('NO')

# if
# шахматы, ход слона
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x1 - x2 == y1 - y2 or x1 + y1 == x2 + y2:
#     print('YES')
# else:
#     print('NO')

# вариант 2
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# dx = x2 - x1
# dy = y2 - y1
# if dx == dy or dx == -dy:
#     print('YES')
# else:
#     print('NO')

# шахматы
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# dx = abs(x2 - x1)
# dy = abs(y2 - y1)
# if dx == 2 and dy == 1 or dx == 1 and dy == 2:
#     print('YES')
# else:
#     print('NO')

# d = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
# }
# print(d.keys())
# d.setdefault(7, 'test')
# print(d)
# print(d.get(4, 'No such key'))
# print(d.items())
# for values in d.values():
#     print(values)
# for key, value in d.items():
#     print(key, value)

# множество
# s = {5, 7, 2, 1} #множество
# # for elem in sorted(list(s)): #сортировка "набора" множества
# if 5 in s: #True / if 5 not in s False
#     #s.add(8) #добавляем элемент в множество
# c = A и B
# c = A | B
#     A.union(B) #объединение A и B
#
#     A |= B #результат сразу же записывается в A
#     A.update(B)
#
#     A & B A &= B #пересечение
#     A.intersection #A.intersection_update(B)
#
#     A - B A -= B A.difference(B) / A.difference_update(B)
#
#     A ^ B A ^= B A.symmetric_difference(B)
#                  A.symmetric_difference_update(B)
#
#     A <= B #операция проверяющая что множество А входит в B
#     A < B #А в подмножестве B но !=

# Словарь
# Months = {
#     'January' : 1,
#     'February' : 2,
# }
# Date = input() #January, 1
# pos = Date.find(',')
# m = Date[:pos]
# m = Months[m]
# d = int(Date[pos +2:]))


# проверить сколько раз слово word встречается в словаре
# if word in A:
#     A[word] = A[word] + 1
# else:
#     A[word] = 1
#
# A[word] = A.get(word, 0) + 1 #2 вариант

# столицы, стран
# Capitals = {
#     'Russia': 'Moscow',
#     'Ukraine': 'Kyiv',
#     'Belarus': 'Minsk',
# }
# for country in Capitals:
#     print('Столица', country, '- город', Capitals[country])

# дан список, определить сколько в нем встречается различных чисел
# print(len(set(input().split())))
# print(len(set(input().split())))

# дано 2 списка, сколько чисел содержится в 1 и 2 одновременно
# print(len(set(input().split()) & set(input().split())))

#на вход строка, если число ранее встречалось 'YES' иначе 'NO'
# s = set()
# for word in input().split():
#     if word in s:
#         print('YES')
#     else:
#         print('NO')
#         s.add(word)

# вывести слово которое в тексте встречается чаще всего
#import sys
# Count = dict()
# for word in input().split(): #for word in sys.stdin.read().split():
#     if word in Count:
#         Count[word] += 1
#     else:
#         Count[word] = 1
# max_word = ''
# max_count = 0
# for word in Count:
#     if Count[word] > max_count or Count[word] == max_count and word < max_word:
#         max_count = Count[word]
#         max_word = word
# print(max_word)

#города
# n = int(input())
# Cities = dict()
# for i in range(n):
#     s = input().split()
#     for word in s[1:]:
#         Cities[city] = s[0]
# print(Cities)
# m = int(input())
# for i in range(m):
#     print(Cities[input()])


# Дано положительное действительное число. Выведите его дробную часть.
# print(float('0.' + input().split('.')[1][::]))

# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# max_digit = max(a, b, c, d, e)
# min_digit = min(a, b, c, d, e)
# print(f'Наименьшее число = {min_digit}')
# print(f'Наибольшее число = {max_digit}')

# from math import sin, cos, tan, radians
# x = radians(float(input()))
# print(sin(x) + cos(x) + tan(x) ** 2)

# from math import sqrt
# a, b, c = float(input()), float(input()), float(input())
# a != 0
# D = b ** 2 - 4 * a * c
# if D < 0:
#     print('Нет корней')
# else:
#     x1 = (-b + sqrt(D)) / (2 ** a)
#     x2 = (-b - sqrt(D)) / (2 ** a)
#
# print(min(x1, x2))
# print(max(x1, x2))


# Напишите программу, которая находит вещественные корни квадратного уравнения
# from math import sqrt
# a, b, c = float(input()), float(input()), float(input())
# D = (b ** 2) - (4 * a * c)
# if D < 0:
#     print('Нет корней')
# elif D == 0:
#     print(-b / (2 * a))
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))

# Напишите программу, которая находит площадь указанного правильного многоугольника.
# from math import tan, pi
# n, a = float(input()), float(input())
# print((n * a ** 2) / (4 * tan(pi / n)))

# на вход названия городов узнак мин и мак длин городов
# str1, str2, str3 = input(), input(), input()
# print(min(str1, str2, str3, key=len))
# print(max(str1, str2, str3, key=len))
#
#
# Напишите программу, которая выясняет можно ли из
# длин этих строк построить возрастающую арифметическую прогрессию.
# a, b, c = input(), input(), input()
# max_digit = max(a, b, c, key=len)
# min_digit = min(a, b, c, key=len)
# avarege = len(a) + len(b) + len(c) - (len(max_digit) + len(min_digit) )
# if (len(max_digit) + len(min_digit)) / 2 == avarege:
#     print('YES')
# else:
#     print('NO')
#2 вариант по формуле прогрессии
# a, b, c = len(input()), len(input()), len(input())
# print('YES' if (b * 2 - c - a) * (c * 2 - b - a) * (a * 2 - b - c) == 0 else 'NO')

# s = input()
# if len(s) == 1 and s in 'aeiou':
#     print('YES')
# else:
#     print('NO')

#поиск "синий" в строке
# s = input()
# if 'синий' in s:
#     print('YES')
# else:
#     print('NO')

# вариант 2
# s = input()
# print('YES' if 'синий' in s else 'NO')



# s = input()
# if 'суббота' in s:
#     print('YES')
# elif 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')


# s = input()
# if 'суббота' in s or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')

# Напишите программу проверяющую корректность email адреса.
# s = input()
# if '@' in s:
#     if '.' in s:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# 2 вариант
# s = input()
# if '@' in s and '.' in s:
#     print('YES')
# else:
#     print('NO')

# цикл for с input()
# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# a, b = input(), int(input())
# for i in range(b):
#     print(a)

# n = int(input())
# for i in range(n):
#     print('*' * 19)

# Напишите программу, которая выводит
# звездный треугольник в соответствии с примером.
# n = int(input())
# for i in range(n):
#     n -= 1
#     print('*' * (n + 1))
# второй вариант
# n = int(input())
# for i in range(n):
#     print('*' * (n - i))

'''На вход программе подается три 
натуральных числа m, \, p, \, nm,p,n:

m:m: стартовое количество организмов;
p:p: среднесуточное увеличение в %;
n:n: количество дней для размножения.
Напишите программу, которая предсказывает 
размер популяции организмов. Программа должна 
выводить размер популяции в каждый день, начиная 
с 11 и заканчивая nn-м днем.'''
# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print(i + 1, float(m))
#     m += m * p / 100

# второй вариант
# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print(m * (p / 100 + 1) ** i)


# range с 3 параметрами
# for i in range (56, 171, 2):
#     print(i)
# 2 вариант
# for i in range(56, 171):
#     if i % 2 == 0:
#         print(i)

# for i in range(5, 0, -1):
#     print(i, end=' ')
# print('Взлетаем!!!')


# Даны два целых числа mm и nn. Напишите программу, которая
# выводит все числа от mm до nn включительно в порядке
# возрастания, если m < nm<n, или в порядке убывания в противном случае.
# m, n = int(input()), int(input())
# if m < n:
#     n, m = m, n
#     for i in range(n, m + 1):
#         print(i)
# elif m > n:
#     n, m = m, n
#     for i in range(n, m - 1, -1):
#         print(i)
# elif m == n:
#     print(m or n)

# Даны два целых числа mm и nn (m > nm>n). Напишите
# программу, которая выводит все нечетные числа от
# mm до nn включительно в порядке убывания.
# m, n = int(input()), int(input())
# for i in range(m, n - 1, -1):
#     if i % 2 == 1:
#         print(i)

# вариант 2
# m, n = int(input()), int(input())
# m = m % 2 - 1 + m #как из четного сделать не четное
# for i in range(m, n, -2):
#     print(i)

# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0: #можно попробовать i % 15 == 0
#         print(i)

# Дано натуральное число n. Напишите программу,
# которая выводит таблицу умножения на n.
# n = int(input())
# for i in range(1, 11):
#     print(f'{n} x {i} = {i * n}')

# counter1 = 0
# counter2 = 0
# for i in range(5):
#     num = int(input())
#     if num > 10:
#         counter1 += 1
#     if num == 0:
#         counter2 += 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.')

# Рассмотрим еще один пример: подсчитать количество чисел
# из диапазона [1;100], квадрат которых оканчивается на 4.
# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter += 1
# print(counter)

# total = 0
# for i in range(5):
#     num = int(input())
#     if num > 10:
#         total += num
# print('Сумма чисел больших 10 равна', total)

# Напишем программу, которая считает
# сумму натуральных чисел от 1 до 100:
# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)

# напишем программу, которая запрашивает 10
# целых чисел и находит их среднее значение:
# total = 0
# for i in range(5):
#     num = int(input())
#     total += num
# average = total / 5
# print('Среднее значение равно', average)



# Напишем программу, определяющую,
# что натуральное число является простым:
# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#
# if num != 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число состовное')


# Напишем программу, которая считывает
# 5 положительных чисел и находит среди них наибольшее число.
# largest = -1
# for i in range(5):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# Напишем программу, которая считывает 5
# чисел (необязательно положительных) и находит среди них наибольшее:
# largest = int(input())
# for i in range(4):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)


# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='') #ответ 1361015

# Напишите программу, которая подсчитывает
# количество чисел в диапазоне от aa до bb
# включительно, куб которых оканчивается на 44 или 99.
# total = 0
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4:
#         total += 1
#     if i ** 3 % 10 == 9:
#         total += 1
# print(total)

# Напишите программу, которая
# подсчитывает сумму введенных чисел.
# n = int(input())
# total = 0
# for i in range(n):
#     n = int(input())
#     total += n
# print(total)



# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет значение выражения
# from math import log
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     i = 1 / i
#     total += i
# print(total - log(n))

# Напишите программу, которая подсчитывает
# сумму тех чисел от 11 до nn (включительно)
# квадрат которых оканчивается на 2, \, 52,5 или 88.
# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2:
#         counter += i
#     if i ** 2 % 10 == 5:
#         counter += i
#     if i ** 2 % 10 == 8:
#         counter += i
# print(counter)

# На вход программе подается натуральное
# число n. Напишите программу, которая вычисляет n!
# n = int(input())
# counter = 1
# for i in range(2, n + 1):
#     counter *= i
# print(counter)

# 2 вариант
# from math import factorial
# n = int(input())
# print(factorial(n))

# Напишите программу, которая считывает
# 10 чисел и выводит произведение отличных от нуля чисел.
# counter = 1
# for i in range(10):
#     n = int(input())
#     if n > 0:
#         counter *= n
# print(counter)

# Напишите программу, которая
# вычисляет сумму всех его делителей.
# counter = 0
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += i
# print(counter)

# Напишите программу вычисления знакочередующей суммы
# n = int(input())
# counter = 0
# for i in range(1, n +1):
#     if i % 2 == 0:
#         counter -= i
#     if i % 2 == 1:
#         counter += i
# print(counter)

# 2 вариант
# n = int(input())
# total = 0
# for i in range(n):
#     total += (i + 1) * (- 1) ** i
# print(total)


# На вход программе подается натуральное число nn, а затем nn
# различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе
# наибольшее число последовательности.
# n = int(input())
# largest = 0
# prelargest = 0
# for i in range(1, n + 1):
#     a = int(input())
#     if a < prelargest and a < largest:
#         largest = largest
#         prelargest = prelargest
#     if prelargest < a < largest:
#         prelargest = a
#     if a > prelargest and a > largest:
#         prelargest = largest
#         largest = a
# print(largest)
# print(prelargest)

# Напишите программу, которая считывает последовательность
# из 10 целых чисел и определяет является ли каждое из них
# четным или нет.
# counter = 0
# for i in range(10):
#     n = int(input())
#     if n % 2 == 0:
#         counter += 1
# if counter == 10:
#     print('YES')
# else:
#     print('NO')

# 2 вариант
# flag = True
# for i in range(3):
#     n = int(input())
#     if n % 2 == 1:
#         flag = False
# if flag: #flag == True
#     print('YES')
# else:
#     print('NO')
#
# 3 вариант с флагом
#
# flag = 'YES'
# for _ in range(10):
#     n = int(input())
#     if a % 2 != 0:
#         flag = 'NO'
# print(flag)

# Напишите программу, которая считывает натуральное число n
# и выводит первые nn чисел последовательности Фибоначчи.
# n = int(input())
# previous = 0 # previous = real = 0
# real = 0
# for i in range(1, n + 1):
#     if i <= 2:
#         n = 1
#         previous = 1
#         real = 1
#     if i > 2:
#         n = previous + real
#         previous = real
#         real = n
#     print(n, end=' ')

# 2 решение
# n = int(input())
# a, b = 1, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())

# Напишем программу, которая считывает числа и находит их
# сумму, до тех пор пока пользователь не введет слово stop
# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)

# Напишите программу, которая выводит члены последовательности.
# a = input()
# while a != 'КОНЕЦ' and a != 'конец':
#     print(a)
#     a = input()


# Напишите программу, которая выводит общее количество
# членов данной последовательности.
# total = 0
# a = input()
# while a != 'стоп' and a != 'хватит' and a != 'достаточно':
#     total += 1
#     a = input()
# print(total)
#
# 2 вариант
# a, total = input(), 0
# while a not in ('стоп', 'хватит', 'достаточно'):
#     total += 1
#     a = input()
# print(total)

# Концом последовательности является любое число не делящееся
# на 7. Напишите программу, которая выводит члены
# данной последовательности.
# a = input()
# while int(a) % 7 == 0:
#     print(a)
#     a = input()


# На вход программе подается последовательность целых чисел,
# каждое число на отдельной строке. Концом последовательности
# является любое отрицательное число. Напишите программу, которая
# выводит сумму всех членов данной последовательности.
# total = 0
# a = input()
# while int(a) >= 0:
#     total += int(a)
#     a = input()
# print(total)


# На вход программе подается последовательность целых чисел от 1 до 5,
# характеризующее оценку ученика, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число, либо число
# большее 5. Напишите программу, которая выводит количество пятерок.
# a, total = input(), 0
# while 0 < int(a) < 6:
#     # b = int(a) % 5 == 0
#     total += int(a) % 5 == 0
#     a = input()
# print(total)

# a = input()
# while a != 'end':
#     a = int(a) ** 2
#     print(a)
#     a = input()
#
# дано число x вывести квадрат его цифр в обратном порядке
# x = int(input())
# while x:
#     digit = x % 10
#     print(digit ** 2)
#     x //= 10

# найти количество цифр 1 в его двоичной записи
# s = 0
# x = int(input())
# while x > 0:
#     binDigit = x % 2
#     s += binDigit
#     x //= 2
# print(s)

# получить сумму квадратов
# n = int(input())
# s = 0
# for x in range(1, n + 1):
#     s += x ** 2
# print(s)

# факториал
# N = int(input())
# factorial = 1
# for x in range(1, N+1):
#     factorial *= x
# print(factorial)

# поиск возможных делителей
# x = int(input())
# for delitel in range(1, x + 1):
#     if x % delitel == 0:
#         print(delitel, end=' ')

# выводит число в обратном порядке
# n = int(input())
# while n > 0:
#     digit = n%10
#     print(digit, end='')
#     n //= 10
# print()


# вывести максимум и минимум числа #179 1 9
# n = int(input())
# minDigit = 10
# maxDigit = -1
# while n > 0:
#     digit = n % 10
#     minDigit = min(minDigit, digit)
#     maxDigit = max(maxDigit, digit)
#     n //= 10
# print(minDigit, maxDigit)

# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break
#     print(n)
# print('hello')

# a = ['foo', 'bar', 'baz', 'qux']
# while True:
#     if not a:
#         break
#     print(a.pop(-1))

# ответ 3foo3bar1foo1bar
# s = ''
#
# n = 5
# while n > 0:
#     n -= 1
#     if (n % 2) == 0:
#         continue
#
#     a = ['foo', 'bar', 'baz']
#     while a:
#         s += str(n) + a.pop(0)
#         if len(a) < 2:
#             break
# print(s)


# a = ['test', 'test1']
# a.clear()
# print(a)

# a = ['foo', 'bar', 'baz']
# for i in a:
#     print(i)


# captains = ['Janeway', 'Picard', 'Sisko']
#
# for i in range(len(captains)):
#     print(captains[i])

# NumPy - это сторонняя библиотека Python.
# import numpy as np
# for i in np.arange(0.3, 1.6, 0.3):
#     print(i)

# import numpy as np
# print(np.linspace(1, 10, 10))







