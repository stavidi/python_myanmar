# Однопроходные алгоритмы

lesson = 418185

## Самый тяжелый арбуз

Продаются арбузы разного веса. Студент хочет взять самый тяжелый арбуз.

Дано: вес каждого арбуза через пробел.

Найти: вес самого тяжелого арбуза.

Решение: студент смотрит арбузы по одному и берет новый арбуз, если он тяжелее.

* `a` - список арбузов (килограммы), мы их будем перебирать в цикле;
* `xstud` - вес арбуза, который выбрал студент
* `x` - вес очередного арбуза (в цикле)

Алгоритм:

* Сначала у студента нет арбуза.
* Студент берет первый арбуз `xstud = a[0]`
* у каждого арбуза `x`
    * студент проверяет, что тяжелее - его арбуз `xstud` или новый арбуз `x`
    * если новый арбуз тяжелее, то студент берет новый арбуз `xstud = x`
    * идем к следующему арбузу
* студент выбрал арбуз `xstud`

Напишем это на python.

```python
def bigest(a):
    # из всех арбузов в а возвращает самый большой арбуз
    xstud = a[0]
    print(f'самый большой арбуз {xstud}, других арбузов пока нет')
    for x in a[1:]:     # для всех остальных арбузов
        if x > xstud:   # если новый арбуз тяжелее
            xstud = x   # взять новый арбуз
        print(f'смотрю x={x},  самый большой арбуз {xstud}')
    # закончили перебирать все арбузы
    return xstud

a = list(map(float, input().split()))   # килограммы не целые, float
xmax = bigest(a)
print(xmax)        
```
Input:
```cpp
2.5 1.3 5.7 7.2 3.14 4.5
```
Output:
```cpp
самый большой арбуз 2.5, других арбузов пока нет
смотрю 2.5, самый большой арбуз 2.5
смотрю 1.3, самый большой арбуз 2.5
смотрю 5.7, самый большой арбуз 5.7
смотрю 7.2, самый большой арбуз 7.2
смотрю 3.14, самый большой арбуз 7.2
смотрю 4.5, самый большой арбуз 7.2
7.2
```

## QUIZ Выбор арбуза

Студент решил выбирать арбуз так:

```python
def choose(a):
    xstud = a[0]
    for x in a[1:]:
        xstud = x
    return xstud

a = list(map(float, input().split()))
my = choose(a)
print(my)        
```

Какой арбуз у него в my?

A. Самый большой

B. Самый маленький

C. Первый

D. Последний

E. Не знаю

ANSWER: D

## NUMBER Слишком рано

Студент решил выбирать арбуз так:

```python
def choose(a):
    xstud = a[0]
    for x in a[1:]:
        if x > xstud:
            xstud = x
        return xstud

a = [2.5, 1.3, 5.7, 7.2, 3.14, 4.5]
my = choose(a)
print(my)        
```

Какой арбуз у него в my?

ANSWER: 1.3

## NUMBER Поспешил

Студент решил выбирать арбуз так:

```python
def choose(a):
    xstud = a[0]
    for x in a[1:]:
        if x > xstud:
            xstud = x
            return xstud

a = [2.5, 1.3, 5.7, 7.2, 3.14, 4.5]
my = choose(a)
print(my)        
```

Какой арбуз у него в my?

ANSWER: 5.7

## NUMBER Начнем с 0

Студент записывал температуру на улице. Какая самая низкая температура?

Студент искал самую низкую температуру так:

```python
def choose(a):
    cold = 0            # начнем с 0
    for t in a:
        if t < cold:
            cold = t
    return cold

a = list(map(int, input().split()))
brrrr = choose(a)
print(brrrr)        
```
Сначала он измерил температуру зимой:
```cpp
-5 -7 -16 -23 -10 -3
```
и `brrrr` стало -10.

Потом он измерил температуру летом:

```cpp
23 25 20 23 17 15 10 19
```

Какая температура в `brrrr` летом?

ANSWER: 0

## TASKINLINE Очень холодно

Дано несколько измерений температуры. Найдите самую холодную температуру.

TEST
23 25 20 23 17 15 10 19
----
10
====
-5 -7 -16 -23 -10 -3
----
-23
====
1023 1025 1020 1023 1017 1015 1010 1019
----
1010
====
10 20 -5
----
-5
====

## Два арбуза

Студент и девушка покупают арбузы. 1 арбуз несет студент, 1 арбуз несет девушка.
Студент несет арбуз тяжелый. Девушка несет арбуз легкий.

Напишем функцию `sort2`. Она возвращает арбуз для студента и девушки.

```python
def sort2(x, y):
    if x > y:
        return x, y
    else:
        return y, x
        
# проверяем, как работает функция
stud, girl = sort2(3, 5)
print(stud, girl)           # 5 3

stud, girl = sort2(13, 5)
print(stud, girl)           # 13 5

stud, girl = sort2(6, 6)
print(stud, girl)           # 6 6
```

## TASKINLINE Еще один арбуз

Напишите функцию sort3, которая берет 3 арбуза и 
возвращает арбуз студента (самый тяжелый) и арбуз девушки (второй по тяжести).
Самый легкий арбуз можно не возвращать.

TEST
2 17 1
---
17 2
====
1 12 5
---
12 5
====
3 10 12
---
12 10
====
10 3 17
---
17 10
====
10 7 0 
---
10 7
====
10 3 5
---
10 5
====
3 1 3
---
3 3
====
3 3 1
---
3 3
====
1 3 3
---
3 3
====
1 3 1
---
3 1
====
3 1 1
---
3 1
====
1 1 3
---
3 1
====
2 2 2
---
2 2
====

## TASKINLINE Два больших арбуза

Студент и девушка покупают арбузы. Они хотят взять 2 самых больших арбуза.
Студент берет самый большой. Девушка самый большой из оставшихся.

Даны арбузы. Найти арбуз студента и арбуз девушки.

* Если арбузов только 2, как поделят арбузы студент и девушка
* Принесли еще 1 арбуз, что с ним делать?
    * дать студенту?
    * дать девушке?
    * оставить, у студента и девушки арбузы больше.

TEST
3 5 2 7 6 4 1
----
7 6
====
1 2 3 4 5 6 7 8
----
8 7
====
8 7 6 5 4 3 2 1
----
8 7
====
5 8
----
8 5
====
5 3
----
5 3
====