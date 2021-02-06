# Переменные

lesson = 479596

## Видео

 Видео  https://www.youtube.com/watch?v=T0C52MCd8os 
от 27:40 до 33:00

## Переменная

**Переменная** (variable) - это память, куда можно записать прочитать 1 значение. Значение может быть любое, например, число.

Функция `middle(size)`. Рисует отрезок. Ставит точку посередине отрезка.

![точка посередине отрезка](https://stepik.org/media/attachments/lesson/479596/01_middle.png)

* Придумаем имя переменной. Назовем переменную middle. 
* Вычислим длину половины отрезка.
* Сохраним результат (число) в переменную middle.
* В `t.bk(middle)` прочитаем это число из переменной middle.

```python
import turtle

def middleLine(size):
    t.color('blue')
    t.fd(size)
    
    # middle - переменная (variable). 
    # В переменную можно записать (write) число 
    # и потом прочитать (read) 
    middle = size / 2   # запишем в переменную middle число size/2
    t.bk(middle)        # прочитаем число из переменной middle
    
    t.color('red')
    t.dot(5)
    
t = turtle.Turtle()
t.width(3)

middleLine(200)

turtle.done() 
```

## TASKTEXT Задача: 1/3 отрезка

* Напишите функцию **parts(size)**. Она рисует 
    * 1 синюю линию длины size и 
    * 1 красную линию посередине длины size/3.
    
![треть отрезка](https://stepik.org/media/attachments/lesson/479596/01_3.png)

## Видео

Видео  https://www.youtube.com/watch?v=T0C52MCd8os  
 от 33:00 до 42:44
 
## Вычисления с переменными

Переменные можно писать в вычислениях.

Нарисуем квадрат размера size с центром (x0, y0). Нарисуем диагональ квадрата.

Функция **sqd(x0, y0, size)** рисует квадрат с центром в (x0,y0) и рисует диагональ.
* встать в точку (х0,у0)
* вычислить как идти в вершину, записать число в переменную half
* встать в вершину квадрата
* нарисовать квадрат
* вычислить длину диагонали, записать число в переменную d
* нарисовать диагональ

![квадрат](https://stepik.org/media/attachments/lesson/479596/sq_middle.png)

```python
def square(x, y, size):
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(5)
    
    # вычислить размер до вершины
    # результат записать в переменную half
    half = size / 2
    
    # перейти в вершину
    t.pu()
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.pd()

    # нарисовать квадрат
    t.color('blue')
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)

    # вычислить длину диагонали
    # результат записать в переменную d
    d = math.sqrt(2) * size
    
    # нарисовать диагональ
    t.lt(45)
    t.fd(d)         # читаем число из переменной d
```

## TASKTEXT Задача: квадрат с диагоналями

Изменить функцию **square**. Она должна рисовать

![квадрат](https://stepik.org/media/attachments/lesson/479596/sq_middle2.png)

```python
def square(x, y, size):
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(5)
    
    # вычислить размер до вершины
    # результат записать в переменную half
    half = size / 2
    
    # перейти в вершину
    t.pu()
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.pd()

    # нарисовать квадрат
    t.color('blue')
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)

    # вычислить длину диагонали
    # результат записать в переменную d
    d = math.sqrt(2) * size
    
    # нарисовать диагональ
    t.lt(45)
    t.fd(d)         # читаем число из переменной d
```

## Где я?

Черепаха рисует в системе координат с осями Х и У. Можно узнать, где сейчас черепаха.

```python
x = t.xcor()   # записать х координату черепахи в переменную х
y = t.ycor()   # записать y координату черепахи в переменную y
p = t.pos()    # записать (x,y) координаты точки в переменную p
```

Можно двигать (move) черепаху по указанным координатам. 
Черепаха не поворачивается.
```python
t.goto(p)      # двигать в точку p
t.setpos(p)    # двигать в точку p
```
или с координатами x и y
```python
t.setpos(x, y) # двигать в точку с координатами (x,y)
t.goto(x, y)   # двигать в точку с координатами (x,y)

t.setx(x)      # изменить х, не изменить у
t.sety(y)      # изменить у, не изменить х
```
Функция `t.write(текст)` рисует текст черепахой. Можно написать координаты черепахи
```python
p = t.pos()         # записали точку в переменную p
t.write(p)          # написали координаты точки p
```

То же самое:
```python
t.write(t.pos())    # написали координаты
```
или 
```python
t.write( (x,y) )    # x и y надо писать в ( )
```

## TASKTEXT Задача: середина отрезка

Напишите функцию middleLine(x1, x2). Она рисует линию от (x1,0) до (x2,0) и пишет координаты концов и середины.

middleLine(-200, 100)

![середина](https://stepik.org/media/attachments/lesson/479596/02_middle_cor.png)

* Используйте только функции goto, setpos, setx. 
* Функции **fd, bk, lt, rt нельзя использовать**

## Пример: диагональ - запоминаем точки

Нарисовать можно по-другому.

![середина](https://stepik.org/media/attachments/lesson/479596/sq_middlep.png)

* перейдем в центр квадрата
* вычислим half
* перейдем в вершину
* нарисуем 2 стороны квадрата
* **запомним точку в переменную p**
* нарисуем 2 стороны квадрата
* **перейдем в точку p - нарисуем диагональ**

```python
def square(x, y, size):
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(10)
    
    # вычислить размер до вершины
    # результат записать в переменную half
    half = size / 2
    
    # перейти в вершину
    t.pu()
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.pd()

    # нарисовать квадрат
    t.color('blue')
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    p = t.pos()      # запишем точку в переменную p
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)

    # нарисовать диагональ
    t.goto(p)        # прочитаем точку из переменной p 
```

## TASKTEXT Задача: квадрат с диагоналями - запомнить точки

Запомните все точки вершин в переменные p1, p2, p3, p4.

Нарисуйте 

![диагонали](https://stepik.org/media/attachments/lesson/479596/sq_middle2p.png)

Исправьте функцию `square`.

```python
import turtle
import math

def square(x, y, size):
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(5)
    
    # вычислить размер до вершины
    # результат записать в переменную half
    half = size / 2
    
    # перейти в вершину
    t.pu()
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.pd()

    # нарисовать квадрат
    t.color('blue')
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    p = t.pos()      # запишем точку в переменную p
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)

    # нарисовать диагональ
    t.goto(p)        # прочитаем точку из переменной p    
    
t = turtle.Turtle()
t.width(3)
t.color('red')

square(-100, -50, 100)

turtle.done()    
```

## TASKTEXT Задача: флаг

Черепаха стоит в центре прямоугольника.
Напишите функцию **rect4(width, height)**. Она рисует прямоугольник шириной width и высотой height так:

![флаг](https://stepik.org/media/attachments/lesson/479596/trk.png)

Выберите, какой вариант вы будете делать.

### Вариант 1. Сохраняем точки

* Напишите функцию trifill(p1, p2, p3, col). Она рисует треугольник с вершинами p1, p2, p3 цветом col.
* Напишите функцию rect4(width, height)
    * Черепаха стоит в центре прямоугольника. Запомните эту точку в переменную p0.
    * Нарисуйте прямоугольник из его центра. Запомните вершины в переменные p1, p2, p3, p4. <br/>
    Можно придумать свои имена переменных, например, rt, lt, lb, rb (right top, left top, left bottom, right bottom).
    * Нарисуйте 4 треугольника. Функция trifill(p0, p1, p2, 'green') нарисует зеленый треугольник.
    
### Вариант 2. Считаем координаты

* написать функцию trifill(x1, y1, x2, y2, x3, y3, col). Она по трем точкам (x1,y1), (x2,y2), (x3,y3) рисует треугольник цветом col. 
* Напишите функцию rect4(w, h)
    * Черепаха стоит в центре прямоугольника. Запомните его координаты в переменные x0 и y0.
    * Нарисуйте 4 треугольника. Функция   trifill(x0, y0, x0-w/2, y0+h/2, x0+w/2, y0+h/2, 'green')  нарисует верхний зеленый треугольник.    


## Большая задача

Нужно нарисовать узор. Это большая задача. Она состоит из маленьких задач. Будем сначала решать маленькие задачи.

![узор](https://stepik.org/media/attachments/lesson/479596/uzor_rect.png)

## TASKTEXT Задача: часть узора

Напишите функцию part(w, h). Она рисует шириной w и высотой h.

![узор](https://stepik.org/media/attachments/lesson/479596/uzor_v1en.png)

### Вариант 1. Запоминаем точки

* Напишите функцию line(p1, p2) - рисовать отрезок от точки p1 до точки p2
* Напишите функцию part(w, h). В функции:
    * вычислите ширину черточки step,
    * Для рисования узора нарисовать нижние _ _ _ и запомнить все точки, где начинаются и кончаются черточки в переменные b0, b1, b2, b3, b4, b5.
    * передвинуться для рисования верхних линий
    * нарисовать верхние линии и запомнить все точки, где начинаются и кончаются черточки в переменные t0, t1, t2, t3, t4, t5
    * нарисовать остальные линии
    
### Вариант 2. Вычисляем координаты

* Напишите функцию line(x1, y1, x2, y2) - рисовать отрезок
* Напишите функцию part(w, h). В функции:
    * вычислите ширину черточки step,
    * Для рисования узора вычислить все места, где начинаются и кончаются черточки.
    * Х координаты точек: x1, x2, x3, x4, x5, x6.
    * Y координаты точек: y и y+h.

## TASKTEXT Задача: ковер (carpet)

Используйте функцию part(w, h) из предыдущей задачи.

* Черепаха стоит в центре.
* Напишите функцию uzor(w, h, dh)
* Нарисуйте

![узор](https://stepik.org/media/attachments/lesson/479596/uzor_rect.png)

## Видео

Видео  https://www.youtube.com/watch?v=T0C52MCd8os 
с 50:45 до конца

## Пример: треугольник

Нарисовать треугольник со стороной **size** из его центра с координатами **(x,y)**.
Написать функцию **triFromCenter(x, y, size)**.

```python
triFromCenter(-50, 80, 150)
```
Нарисует

![узор](https://stepik.org/media/attachments/lesson/479596/08_tri.png)

* перейдем в точку (x,y). Сохраним точку в переменную center
* вычислим радиус описанной окружности size*2/3. Сохраним число в переменную path
* перейдем в точки вершин и сохраним их в переменных p1, p2, p3
* нарисуем треугольник по точкам p1, p2, p3

```python
def triFromCenter(x, y, size):
    # перейдем в центр треугольника
    t.pu()
    t.goto(x, y)
    t.pd()
    # запишем эту точку в переменную center
    сenter = t.pos()
    # поставим в центре точку
    t.color('green')
    t.dot(10)
    
    # радиус описанной окружности запишем в path
    path = size * 2 / 3
    
    # перейдем в вершину
    t.fd(path)
    # запишем точку вершины в переменную p1
    p1 = t.pos()
    t.bk(path)
    t.lt(120)
    
    # перейдем в вершину
    t.fd(path)
    # запишем точку вершины в переменную p2
    p2 = t.pos()
    t.bk(path)
    t.lt(120)

    # перейдем в вершину
    t.fd(path)
    # запишем точку вершины в переменную p3
    p3 = t.pos()
  
    # рисуем треугольник по вершинам
    t.color('red')
    t.goto(p1)
    t.goto(p2)
    t.goto(p3)
    

t = turtle.Turtle()
t.width(3)
t.color('red')

triFromCenter(-50, 80, 150)

turtle.done()  
```

## Вводим числа с клавиатуры

Можно в программе написать - нельзя нарисовать другой треугольник.

Чтобы нарисовать любой треугольник человек должен ввести числа.
Числа в repl.it вводятся на вкладке console (консоль).
Прочитать 1 строку с консоли можно input(). Это функция python.
input() возвращает текст. Нужно число. 
int(text) из текста делает число.
Прочитать строку, сделать из нее число, записать число в переменную х:

```python
x = int(input())
```

Прочитать 3 числа. 1 число на 1 строке

```python
-50
80
150
```

Нужно написать код:
```python
x = int(input())
y = int(input())
size = int(input())
```

## Пример: вводим числа с клавиатуры

* Нажмите кнопку run - запустите код
* Нажмите вкладку console и введите 3 числа. По 1 числу на 1 строке. 
* Нажмите вкладку result. Черепаха должна нарисовать треугольник

Ничего посылать не нужно. **Нужно научиться запускать код и вводить числа с клавиатуры.**

## TASKTEXT Задача: звезда

Напишите функцию **star(x, y, size)**, где 

* (x, y) - координаты одной вершины, 
* size - **на ваш выбор**:
    * или расстояние между двумя вершинами 
    * или длина отрезка звезды
    * или радиус описанной окружности

Напишите координаты каждой вершины t.write(t.pos())

Прочитайте size из консоли.

Пример. Введем числа. **Каждое число на новой строке**
```cpp
0
100
300
```
Получим 

![star](https://stepik.org/media/attachments/lesson/479596/func_t16.png)