# main.py

# Функция для вычисления площади треугольника
def triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive values.")
    return 0.5 * base * height

# Функция для вычисления периметра треугольника
def triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive values.")
    return a + b + c

# Функция для вычисления площади квадрата
def square_area(side):
    if side <= 0:
        raise ValueError("Side must be a positive value.")
    return side * side

# Функция для вычисления периметра квадрата
def square_perimeter(side):
    if side <= 0:
        raise ValueError("Side must be a positive value.")
    return 4 * side

# Функция для вычисления площади прямоугольника
def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")
    return length * width

# Функция для вычисления периметра прямоугольника
def rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")
    return 2 * (length + width)

# Функция для вычисления площади круга
import math
def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius * radius

# Функция для вычисления периметра круга
def circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return 2 * math.pi * radius
