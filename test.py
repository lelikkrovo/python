#a = int(input())
#b = int(input())
#print(f'{a} + {b} = {a+b}')

#x, y = int(input()), int(input())
#y = y % x
#print(x - y)

#x = int(input())
#s = 100000 * (1 + 10) ** x
#print(round(s))

#x = int(input())
#s = 100000 * (1 + 0.1/12) ** (x * 12)
#print(round(s))

#greet = input()
#print(f'Hello, my name is {greet} ')

#s = 'foo-bar-baz'
#'-'.join(s.split('-'))

#x = input()
#print(x[:len(x)//2])



#x = input()
#x1 = x[::-1]
#if x == x1:
#    print('YES')
#else:
#    print('NO')


#x = input()
#list(x)
#print(list(x))



#s = int(input()) округление вверх
#p = 4
#print((s + p -1) // p)



#x = int(input())
#1 = x // 60
#y = x % 60
#print(f'{x} мин - это {x1} час {y} минут.')

#num = 17 Получить любую из цифр в числе
#a = num % 10
#b = num // 10
#print(a, b)

#num = 754
#a = num % 10
#b = (num % 100) // 10
#c = num // 100
#print(a, b, c)

#Последняя цифра: (num % 101) // 100;
#Предпоследняя цифра: (num % 102) // 101;
#Предпредпоследняя цифра: (num % 103) // 102;
#Вторая цифра: (num % 10n-1) // 10n-2;
#Первая цифра: (num % 10n) // 10n-1.


#num = int(input())
#last_digit = num % 10
#first_digit = num // 10
#print('Сумма цифр =', last_digit + first_digit)
#Число, образованное при перестановке цифр двузначного числа.
#print('Искомое число =', last_digit * 10 + first_digit)

#Выводит на экран цифры (через запятую).
#num = int(input())
#digit3 = num % 10
#digit2 = (num // 10) % 10
#digit1 = num // 100
#print(digit1, digit2, digit3, sep=',')

#Рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# num = int(input())
# digit1 = num % 10
# digit2 = (num // 10) % 10
# digit3 = num // 100
# print(f'Сумма цифр = {digit3 + digit2 + digit1}')
# print(f'Произведение цифр = {digit3 * digit2 * digit1}')

#num = int(input())
#digit1 = num % 10
#digit2 = (num // 10) % 10
#digit3 = (num // 100) % 10
#digit4 = num // 1000
#print(f'Цифра в позиции тысяч равна {digit4}')
#print(f'Цифра в позиции сотен равна {digit3}')
#print(f'Цифра в позиции десятков равна {digit2}')
#print(f'Цифра в позиции единиц равна {digit1}')

# Сумма квадрата и квадрат суммы
#a = int(input())
#b = int(input())
#s = (a + b) ** 2
#s1 = a ** 2 + b ** 2
#print(f'Квадрат суммы {a} и {b} равен {s}')
#print(f'Сумма квадратов {a} и {b} равна {s1}')

a = int(input())
b = int(input())
c = int(input())
if a != b != c:
    print('числа не равны')
else:
    print('числа равны')

#x = int(input())
#s = 100000 * (1 + 10) ** x
##print(round(s))



