#рисовать ничего не будем, черепаха не нужна

# функция принимает градусы Цельсия и возвращает градусы Фаренгейта
def farh(c):
    res = c * 9 / 5 + 32   # считаем результат
    return res             # возвращаем результат

# Напечатаем таблицу для перевода из градусов Цельсия в Фаренгейты от -50 до 50 с шагом 10 градусов Цельсия

cel = -50            # сначала -50 градусов Цельсия
while cel <= 50:     # пока градусы Цельсия не больше 50
    f = farh(cel)    # функция farh возвращает число, записываем его в переменную f
    print(cel, f)
    cel += 10        # увеличить градусы Цельсия
