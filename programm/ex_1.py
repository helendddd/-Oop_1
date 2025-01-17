# Парой называется класс с двумя полями, которые имеют имена first и second.
# Требуется реализовать тип данных с помощью такого класса.
# Во всех заданиях обязательно должны присутствовать:
#   метод инициализации __init__;
#   метод должен контролировать значения аргументов на корректность;
#   ввод с клавиатуры read;
#   вывод на экран display.
# Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой
# структуры. Функция должна получать в качестве аргументов значения для полей
# структуры и возвращать структуру требуемого типа. При передаче ошибочных
# параметров следует выводить сообщение и заканчивать работу.
#
# Элемент геометрической прогрессии вычисляется по формуле:
# aj = a0* r^j, j = 0, 1, 2,...
# Поле first — дробное число, первый элемент прогрессии а ;
# поле second — постоянное отношение.
# Определить метод для вычисления заданного элемента прогрессии.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


class GeometricProgression:
    def __init__(self, first=1.0, second=1.0):
        """
        Конструктор для инициализации 1-го элемента прогрессии
        и постоянного отношения.
        Проверяет корректность введённых значений.
        """
        if not isinstance(first, (int, float)):
            raise ValueError("Первый элемент прогрессии должен быть числом.")
        if not isinstance(second, (int, float)):
            raise ValueError("Постоянное отношение должно быть числом.")

        self.first = float(first)  # Первый элемент прогрессии a0
        self.second = float(second)  # Постоянное отношение r

    def read(self):
        """
        Ввод данных с клавиатуры для первого элемента и постоянного отношения.
        """
        self.first = float(input("Введите первый элемент прогрессии (a0): "))
        self.second = float(input("Введите постоянное отношение (r): "))

    def display(self):
        """
        Вывод данных на экран, включая j-й элемент прогрессии.
        """
        print(f"Первый элемент прогрессии (a0): {self.first}")
        print(f"Постоянное отношение (r): {self.second}")
        j = int(input("Введите номер элемента прогрессии, для вычисления: "))
        result = self.elementj(j)
        print(f"{j}-й элемент прогрессии: {result}")

    def elementj(self, j):
        """
        Метод для вычисления j-го элемента прогрессии.
        """
        if not isinstance(j, int) or j < 0:
            raise ValueError(
                "Индекс элемента должен быть неотрицательным целым числом."
            )
        return self.first * (self.second ** j)


def make_geometric_progression(first, second):
    """
    Внешняя функция для создания объекта GeometricProgression.
    """
    try:
        return GeometricProgression(first, second)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)


if __name__ == '__main__':
    # Создаём первый объект прогрессии через функцию
    gp1 = make_geometric_progression(2, 3)
    gp1.display()

    # Ввод значений для второго объекта с клавиатуры
    print("Создаём вторую прогрессию:")
    first = float(input("Введите первый элемент прогрессии (a0): "))
    second = float(input("Введите постоянное отношение (r): "))
    gp2 = make_geometric_progression(first, second)
    gp2.display()
