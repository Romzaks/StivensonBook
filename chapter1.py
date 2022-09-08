import math


def ex1():
    print('Roman')
    print('Saint-Petersburg, Russia')


def ex2():
    name = input('Input your name: ')
    print('Good afternoon,', name)


def ex3():
    len = float(input('Input length: '))
    wid = float(input('Input width: '))
    s = len * wid
    print(f'{s:.2f}')


def ex4():
    len = float(input('Input length: '))
    wid = float(input('Input width: '))
    s = len * wid
    s_in_arc = s / 43560
    print(f'{s_in_arc:.2f}')


PRICE_1, PRICE_2 = 0.10, 0.25


def ex5():
    count1 = int(input('Input count 1 liter bottles '))
    count2 = int(input('Input count > 1 liter bottles '))
    sum = count1 * PRICE_1 + count2 * PRICE_2
    print(f'{sum:.2f}$')


def ex6():
    tax = 0.20  # налог
    fee = 0.18  # чаевые

    sum = float(input('Input sum: '))
    sum_tax = sum * tax
    sum_fee = sum * fee
    all_sum = sum + sum_tax + sum_fee
    print(f'{sum_tax:.2f}$, {sum_fee:.2f}$, {all_sum:.2f}$')


def ex7():
    n = int(input('Input number: '))
    s = (1 + n) * n // 2
    print(s)


def ex8():
    weight1, weight2 = 75, 112
    count1 = int(input('Input first thing: '))
    count2 = int(input('Input second thing: '))
    sum_weight = count1 * weight1 + count2 * weight2
    print(sum_weight)


def ex9():
    p = 0.04
    k = 1 + p
    init_sum = float(input('Input your sum: '))
    print(f'1 - {(init_sum * k):.2f}')
    print(f'1 - {(init_sum * k**2):.2f}')
    print(f'1 - {(init_sum * k**3):.2f}')


def ex10():
    a, b = int(input()), int(input())
    print(a + b, abs(a - b), a * b, a // b, a % b, math.log10(a), a**b, sep='\n')


def ex11():
    liter = 0.22
    km = 0.62
    coef = 235
    usa = float(input('Input in USA: '))
    canada = usa * coef
    print('Canada, ', canada)


def ex12():
    r = 6371.01
    t1, g1 = math.radians(float(input())), math.radians(float(input()))
    t2, g2 = math.radians(float(input())), math.radians(float(input()))
    distance = r * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
    print(distance)



