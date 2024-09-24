# Создать класс Angle для работы с углами на плоскости, задаваемыми
# величиной в градусах и минутах. Обязательно должны быть реализованы:
# - перевод в радианы,
# - приведение к диапазону 0-360,
# - увеличение и уменьшение угла на заданную величину,
# - получение синуса,
# - сравнение углов.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


class Angle:
    def __init__(self, degrees=0.0, minutes=0.0):
        """
        Конструктор для инициализации угла в градусах и минутах.
        """
        if not isinstance(degrees, (int, float)):
            raise ValueError("Значение градусов должно быть числом.")
        if not isinstance(minutes, (int, float)):
            raise ValueError("Значение минут должно быть числом.")

        self.degrees = degrees
        self.minutes = minutes
        self.normalize360()

    def read(self):
        """
        Ввод данных с клавиатуры для работы с углами на плоскости.
        """
        self.degrees = float(input("Введите градусы: "))
        self.minutes = float(input("Введите минуты: "))
        self.normalize360()

    def display(self):
        """
        Вывод данных на экран.
        """
        print(f"Угол: {self.degrees} градусов, {self.minutes} минут")

    def to_decimal_degrees(self):
        """
        Преобразование угла в десятичные градусы.
        """
        return self.degrees + self.minutes / 60.0

    def radians(self):
        """
        Перевод в радианы.
        """
        return math.radians(self.to_decimal_degrees())

    def normalize360(self):
        """
        Приведение угла к диапазону от 0 до 360 градусов.
        """
        total_degrees = self.to_decimal_degrees()
        normalized_degrees = total_degrees % 360
        self.degrees = int(normalized_degrees)
        self.minutes = (normalized_degrees - self.degrees) * 60

    def add_angle(self, degrees=0.0, minutes=0.0):
        """
        Увеличение угла на заданную величину в градусах и минутах.
        """
        total_minutes = (self.degrees + degrees) * 60 + self.minutes + minutes
        self.degrees = total_minutes // 60
        self.minutes = total_minutes % 60
        self.normalize360()

    def subtract_angle(self, degrees=0.0, minutes=0.0):
        """
        Уменьшение угла на заданную величину в градусах и минутах.
        """
        total_minutes = (
            (self.degrees * 60 + self.minutes) -
            (degrees * 60 + minutes)
        )
        self.degrees = total_minutes // 60
        self.minutes = total_minutes % 60
        self.normalize360()

    def sinangle(self):
        """
        Получение синуса угла.
        """
        return math.sin(self.radians())

    # Сравнение углов
    def equals(self, other):
        """
        Проверка на равенство двух углов.
        """
        if isinstance(other, Angle):
            return math.isclose(
                self.to_decimal_degrees(),
                other.to_decimal_degrees()
            )
        return False

    def greater(self, other):
        """
        Проверка, больше ли текущий угол, чем другой угол.
        """
        if isinstance(other, Angle):
            return self.to_decimal_degrees() > other.to_decimal_degrees()
        return False

    def less(self, other):
        """
        Проверка, меньше ли текущий угол, чем другой угол.
        """
        if isinstance(other, Angle):
            return self.to_decimal_degrees() < other.to_decimal_degrees()
        else:
            return False


if __name__ == '__main__':
    angle1 = Angle(30, 20)  # Угол 30 градусов 20 минут
    angle2 = Angle(45, 50)  # Угол 45 градусов 50 минут
    angle1.display()
    angle2.display()

    print("Угол 1 в радианах:", angle1.radians())
    print("Синус угла 1:", angle1.sinangle())

    print("Угол 1 == Угол 2:", angle1.equals(angle2))
    print("Угол 1 > Угол 2:", angle1.greater(angle2))
    print("Угол 1 < Угол 2:", angle1.less(angle2))

    # Увеличение угол 1 на 10 градусов и 30 минут
    angle1.add_angle(10, 30)
    angle1.display()

    # Уменьшение угол 2 на 5 градусов и 40 минут
    angle2.subtract_angle(5, 40)
    angle2.display()
