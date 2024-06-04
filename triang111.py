import math

class Triangle:
    """Класс Triangle представляет треугольник с углами и сторонами.

    Поля:
    a, b, c - стороны треугольника
    alpha, beta, gamma - углы треугольника в градусах

    Методы:
    area() - вычисляет площадь треугольника
    perimeter() - вычисляет периметр треугольника
    heights() - вычисляет высоты треугольника
    triangle_type() - определяет тип треугольника
    """
    __counter = 0

    def __init__(self, a, b, c, alpha, beta, gamma):
        """Инициализация нового экземпляра класса Triangle."""
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        Triangle.__counter += 1

    def __del__(self):
        """Деструктор класса Triangle."""
        Triangle.__counter -= 1

    @classmethod
    def get_counter(cls):
        """Возвращает количество созданных объектов класса Triangle."""
        return cls.__counter

    @property
    def a(self):
        """Возвращает значение стороны a."""
        print("Доступ к стороне a")
        return self._a

    @a.setter
    def a(self, value):
        """Устанавливает значение стороны a."""
        self._a = value

    # Аналогично реализовать для сторон b и c, а также для углов alpha, beta, gamma

    def area(self):
        """Вычисляет площадь треугольника по формуле Герона."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        """Вычисляет периметр треугольника."""
        return self.a + self.b + self.c

    def heights(self):
        """Вычисляет высоты треугольника."""
        area = self.area()
        return {'ha': 2 * area / self.a, 'hb': 2 * area / self.b, 'hc': 2 * area / self.c}

    def triangle_type(self):
        """Определяет тип треугольника."""
        if self.a == self.b == self.c:
            return "Равносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Равнобедренный"
        elif self.alpha == 90 or self.beta == 90 or self.gamma == 90:
            return "Прямоугольный"
        else:
            return "Разносторонний"

    def __str__(self):
        """Строковое представление объекта класса Triangle."""
        return f"Triangle(a={self.a}, b={self.b}, c={self.c}, alpha={self.alpha}, beta={self.beta}, gamma={self.gamma})"

    def __repr__(self):
        """Строковое представление объекта класса Triangle для разработчиков."""
        return f"Triangle({self.a}, {self.b}, {self.c}, {self.alpha}, {self.beta}, {self.gamma})"
