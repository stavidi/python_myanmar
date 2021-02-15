## Читать числа 

### Числа в 1 строку через пробел читаем так:
```python
a = list(map(int, input().split()))     # 5 -1 23
```
### Дано n. Дальше n чисел, по 1 числу на 1 строке. 

Input:
```cpp
3   # сколько чисел
5
-1
23
```
Читаем сначала n, потом читаем в цикле числа:
```python
n = int(input())        # прочитали 3
a = []                  # сначала a - пустой список
for i in range(n):      # повторить n раз
    x = int(input())    # читаем 1 число на 1 строке
    a.append(x)         # добавляем это число в список
    print(*a)           # печатаем в цикле список
    
print('После цикла', *a)
```
Output:
```cpp
5
5 -1
5 -1 23
После цикла 5 -1 23
```

### Даны числа, по 1 числу на 1 строке

Input:
```cpp
5
-1
23
```
Сколько чисел - не знаем. Можем перебрать все строки, которые ввели с клавиатуры. Это **sys.stdin**. Еще нужен `import sys`

```python
import sys                  # чтобы написать sys.stdin
a = []                      # сначала a - пустой список
for line in sys.stdin:      # для каждой строки, введенной с клавиатуры
    x = int(line)           # из строки делаем число
    a.append(x)             # добавляем это число в список
    print(*a)               # печатаем в цикле список
    
print('После цикла', *a)
```
В конце всех данных нужно нажать *Ctrl+Z* в Windows или *Ctrl+D* в других операционных системах (Мас, Linux).

Output:
```cpp
5
5 -1
5 -1 23
После цикла 5 -1 23
```

Можно числа записать в файл, например, `data.txt`, а программу в файл `myprint.py`. В командной строке читать символы не из клавиатуры, а из файла:

```cpp
python myprint.py < data.txt
```
Тогда заканчивать поток символов с помощью  *Ctrl+Z* или *Ctrl+D* не нужно, закончится файл, закончатся все символы.