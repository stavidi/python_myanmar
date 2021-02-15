# unmutable и mutable

lesson = 427315

## Задача

$n$ детей. Им дали конфеты $a_0, a_1, .. a_n$ штук. Дети хотят, чтобы у каждого было одинаковое количество конфет. Дети маленькие. Они не умеют складывать и делить на $n$.

Дети умеют делить поровну на 2 человека. Они делят поровну. Если есть лишняя конфета, ее откладывают.

Хитрый школьник решил помочь детям.

* Школьник поставил детей в круг и делил так:
    * Поделил для ребенка 0 и ребенка 1, если есть лишняя конфета взял себе.
    * Поделил для ребенка 1 и ребенка 2, если есть лишняя конфета взял себе.
    * ...
    * Поделил для ребенка $n-1$ и ребенка $n$, если есть лишняя конфета взял себе.
    * **Поделил для ребенка $0$ и ребенка $n$**, если есть лишняя конфета взял себе.
* потом дети проверили - у всех одинаковое количество конфет или нет. Если не одинаковое, они повторяют еще раз для всех детей.

Дано: $a_0, a_1, .. a_n$ - конфет у каждого ребенка

Найти: Сколько конфет у каждого ребенка в конце и сколько конфет у хитрого школьника.

Будем печатать номера двух детей и сколько конфет у каждого ребенка. Пусть детям дали 1 5 3 4 2 конфет.

```cpp
      1 5 3 4 2   # дали детям
0 1 : 3 3 3 4 2   # поделили у ребенка 0 и 1, сложили 1+5=6, по 3 конфеты, лишних нет  
1 2 : 3 3 3 4 2   # поделили у ребенка 1 и 2, сложили 3+3=6, по 3 конфеты, лишних нет  
2 3 : 3 3 3 3 2 + # поделили у ребенка 2 и 3, сложили 3+4=7, по 3 конфеты, +1 лишняя
3 4 : 3 3 3 2 2 + # поделили у ребенка 3 и 4, сложили 3+2=5, по 2 конфеты, +1 лишняя
0 4 : 2 3 3 2 2 + # поделили у ребенка 0 и 4, сложили 3+2=5, по 2 конфеты, +1 лишняя
check NO          # проверили, что у всех детей одинаково - НЕТ
0 1 : 2 2 3 2 2 + # поделили у ребенка 0 и 1, сложили 3+2=5, по 2 конфеты, +1 лишняя
1 2 : 2 2 2 2 2 + # поделили у ребенка 1 и 2, сложили 3+2=5, по 2 конфеты, +1 лишняя
2 3 : 2 2 2 2 2   # поделили у ребенка 2 и 3, сложили 2+2=2, по 2 конфеты, лишних нет
3 4 : 2 2 2 2 2   # поделили у ребенка 3 и 4, сложили 2+2=2, по 2 конфеты, лишних нет
0 4 : 2 2 2 2 2   # поделили у ребенка 0 и 4, сложили 2+2=2, по 2 конфеты, лишних нет
check YES         # проверили, что у всех детей одинаково - ДА
2 5               # ответ: у детей по 2 конфеты, у школьника 5 конфет
```

Что делать:
* написать функцию, которая делит конфеты у **двух** детей и дает конфету (1 или 0) школьнику
* написать функцию проверки, что у все одинаково (делали раньше)
* написать функцию, которая делит конфеты у **всех** детей и дает конфеты школьнику

Дальше мы будем разбирать, как писать эту программу.

## TASKINLINE Напишем функцию, которая делит конфеты для двух детей

Напишем часть задачи. Только функцию, которая делит конфеты для детей с номером $i$ и $j$. И дает 1 или 0 конфет школьнику (переменная `schoolboy`)

Дано: 

* $a_0, a_1, .. a_n$ - конфет у каждого ребенка
* $i$ - на следующих строках номера двух детей, которые делят конфеты
* $j$ - на следующих строках номера двух детей, которые делят конфеты

```python
def delim(a, i, j):
    """ Функция делит конфеты детей a[i] и a[j].
    Отдает школьнику (return) лишние конфеты."""
    # тут нужно написать код
    
a = list(map(int, input().split()))     # все конфеты у детей
i = int(input())
j = int(input())

schoolboy = delim(a, i, j)              # делим кофеты для детей i и j
print(i, j, schoolboy, a)               # печатаем так
```
TEST
1 2 3 4 5
0
3
----
0 3 1 [2, 2, 3, 2, 5]
====
9 3 6 2 7
0
1
----
0 1 0 [6, 6, 6, 2, 7]
====
9 3 6 2 7
1
2
----
1 2 1 [9, 4, 4, 2, 7]
====
9 3 6 2 7
1
3
----
1 3 1 [9, 2, 6, 2, 7]
====
9 3 6 2 7
4
2
----
4 2 1 [9, 3, 6, 2, 6]
====
9 3 6 2 7
0
-1
----
0 -1 0 [8, 3, 6, 2, 8]
====

## TASKINLINE Вся задача про конфеты

Дано: 

* $a_0, a_1, .. a_n$ - конфет у каждого ребенка

Печатать ответ нужно только 2 числа: сколько конфет у каждого ребенка и сколько конфет у школьника.

```python
def delim(a, i, j):
    """ Функция делит конфеты детей a[i] и a[j].
    Отдает школьнику (return) лишние конфеты."""
    # тут нужно написать код
    
def all_equal(a):
    """ Проверяет, все ли числа в списке a одинаковые.
    Возвращает True (все одинаковые) или False (не все)"""
    # вы писали раньше такую задачу
    
def make_all_happy(a):
    """ Дети делят конфеты, лишние конфеты возвращают"""
    # тут нужно написать код

a = list(map(int, input().split()))     # все конфеты у детей
schoolboy = make_all_happy(a)           # долго делим конфеты у всех детей
print(a[0], schoolboy)                  # печатаем так
```
TEST
1 5 3 4 2
----
2 5
====
9 3 6 2 7
----
4 7
====
1 13 4 9 6 17 8 14 3
----
6 21
====
2 2 2 2
----
2 0
====
3 4
----
3 1
====
5 5
----
5 0
====