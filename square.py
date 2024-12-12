def square_area(side):
    """Вычисление площади квадрата."""
    if side < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной.")
    return side ** 2

def square_perimeter(side):
    """Вычисление периметра квадрата."""
    if side < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной.")
    return 4 * side