import math


def countSquare(*args):
    if len(args) == 1:
        # Если передан один аргумент, считаем что это круг
        return _countCircle(args[0])
    elif len(args) == 3:
        # Если передано три аргумента, считаем что это треугольник
        return _countTriangle(*args)
    else:
        # Иначе вызываем ошибку
        raise ValueError("Нет фигуры с заданным количеством параметров")



def _countTriangle(a, b, c):
    """
    Вычисление по формуле Герона через полупериметр
    """

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует.")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


def _countCircle(r):
    """
    Вычисление по стандартной формуле
    """
    area = math.pi * r ** 2

    return area