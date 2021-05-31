print("Привет")
print('2 + 3 =', 2 + 3)
print('1', '2', '3', sep=' + ', end=' ')
print('=', 1 + 2 + 3)
print(11 + 6)
print(11 - 6)
print(11 * 6)
print(11**6)
print(11 % 6)
print((23 + 8) % 24)
print((7 - 8) % 24)
speed1 = 108
speed2 = 108
time = 12
dist = time * (speed1 + speed2)
print(dist)

phrase = 'Hasts la vista'
who = '"baby"'
print(phrase, who, sep=',')

ans = 2 + 3
expr = ' 2 + 3 = '
print(expr + str(ans))
# Сумма чисел
n = int(input())
a1 = n // 100 % 100
a2 = n // 10 % 10
a3 = n % 10
print(a1 + a2 + a3)
# Электронные часы
n = int(input())
a1 = n // 60 % 24
a2 = n % 60
print(a1, a2)
# Убираем к число цифр к конца
n = int(input())
k = int(input())
print(n // 10 ** k)
# Задача про пирожки
a = int(input())
b = int(input())
n = int(input())
abcoin = a * 100 + b
npir = (abcoin * n) // 100
dpir = (abcoin * n) % 100
print(npir, dpir)
# Задача про номера
n = int(input())
b = n + 1
c = n - 1
print('The next number for the number', n, 'is', b, end='')
print('.')
print('The previous number for the number', n, 'is', c, end='.')
# Задание про пингвины
n = int(input())
a = '   _~_    '
b = '  (o o)   '
c = ' /  V  \\  '
d = '/(  _  )\\ '
f = '  ^^ ^^   '
q = a * n
w = b * n
e = c * n
r = d * n
t = f * n
print(q)
print(w)
print(e)
print(r)
print(t)
# Четность числа
n = int(input())
b = n % 2 == 0
print(b)
# Какое число больше?
a = int(input())
b = int(input())
if a > b:
    print(1)
elif b > a:
    print(2)
elif a == b:
    print(0)
# Больше из трех
a = int(input())
b = int(input())
c = int(input())
if a > b > c:
    print(a)
elif a > c > b:
    print(a)
elif b > a > c:
    print(b)
elif b > c > a:
    print(b)
elif c > a > b:
    print(c)
elif c > b > a:
    print(c)
# Больше из трех, второй вариант
a = int(input())
b = int(input())
c = int(input())
if b > a:
    a = b
if c > a:
    a = c
print(a)
# Цикл
x = int(input())
while x > 0:
    y = x
    while y > 0:
        print(y)
        y -= 1
    x -= 1
print('Stop')

import turtle
turtle.shape('turtle')
for i in range(360):
    turtle.left(1)
    turtle.forward(2)