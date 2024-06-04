import math

class Triangle:
    """
    Класс для представления треугольника.

    Поля:
    - a, b, c - стороны треугольника
    - alpha, beta, gamma - углы треугольника (в градусах)

    Методы:
    - get_sides, set_sides - получение и изменение сторон
    - get_angles, set_angles - получение и изменение углов
    - area - вычисление площади
    - perimeter - вычисление периметра
    - heights - вычисление высот
    - kind - определение вида треугольника
    """

    __counter = 0

    def __init__(self, a, b, c, alpha, beta, gamma):
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        Triangle.__counter += 1

    def __del__(self):
        Triangle.__counter -= 1

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @property
    def a(self):
        print("Доступ к полю a")
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    # То же самое для остальных полей

    def area(self):
        # Вычисление площади по формуле Герона
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def heights(self):
        # Вычисление высот треугольника
        area = self.area()
        return (2 * area / self.a, 2 * area / self.b, 2 * area / self.c)

    def kind(self):
        # Определение вида треугольника
        if self.a == self.b == self.c:
            return "Равносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Равнобедренный"
        elif self.alpha == 90 or self.beta == 90 or self.gamma == 90:
            return "Прямоугольный"
        else:
            return "Разносторонний"

    def __str__(self):
        return f"Треугольник со сторонами {self.a}, {self.b}, {self.c} и углами {self.alpha}, {self.beta}, {self.gamma}"

    def __repr__(self):
        return f"Triangle({self.a}, {self.b}, {self.c}, {self.alpha}, {self.beta}, {self.gamma})"