class Money:
    """Класс для работы с денежными суммами"""
    __counter = 0

    def __init__(self, money=None):
        """Поля класса: денежная сумма """        
        self.money = money
        
        Money.__counter += 1

    @classmethod
    def get_instance_count(cls):
        """Число созданных объектов класса"""
        return f"Число созданных объектов класса: {cls.__counter}"
    
    def __str__(self):
        """Отображение в виде строки"""
        res = 0
        for i in self.money:
            res += i * self.money[i]
        return f"{self.money}"
    
    def __repr__(self):
        """Репрезентация данных"""
        return f"Money = {self.money})"
    
    def __del__(self):
        """Удаление объекта"""
        Money.__counter -= 1
    
    @property
    def money(self):
        """Доступ к полю money"""
        print("Задействован аргумент money")
        return self._money
    
    @money.setter
    def money(self, value):
        """Устанавливаем значение money"""
        print("Изменение значения money")
        self._money = value

    def __add__(self, other):
        """Сложение сумм"""
        res = res1 = 0
        for i in self.money:
            res += i * self.money[i]
        for i in other.money:
            res1 += i * other.money[i]
        return f"Складываем первое число со вторым: {res} + {res1} = {res+res1}"
    
    def __sub__(self, other):
        """Вычитание сумм"""
        res = res1 = 0
        for i in self.money:
            res += i * self.money[i]
        for i in other.money:
            res1 += i * other.money[i]
        if res1 > res:
            return f"Отнимаем второе число от первого: {res1} - {res} = {res1-res}"
        else:
            return f"Отнимаем первое число от второго: {res} - {res1} = {res-res1}"

    
    def __mul__(self, other):
        """Умножение сумм"""
        res = res1 = 0
        for i in self.money:
            res += i * self.money[i]
        for i in other.money:
            res1 += i * other.money[i]
        return f"Перемножаем денежные суммы: {res} * {res1} = {res*res1}"
    
    def __truediv__(self, other):
        """Деление сумм"""
        res = res1 = 0
        for i in self.money:
            res += i * self.money[i]
        for i in other.money:
            res1 += i * other.money[i]
        if res > res1:
            return f"Делим денежные суммы {res} / {res1} = {round(res / res1, 2)}"
        else:
            return f"Делим денежные суммы {res1} / {res} = {round(res1 / res, 2)}"
        
    def __eq__(self, other):
        """Равность денежных сумм (True/False)"""
        return f"Равны ли денежные суммы: {self.money == other.money}"

    def umnozh_on_number(self, number):
        """Умножение на дробное число"""
        res = 0
        for i in self.money:
            res += i * self.money[i]
        
        return f"Умножаем денежную сумму на число {res} * {number} = {res * number}"
    
    def div_on_number(self, number):
        """Умножение на дробное число"""
        res = 0
        for i in self.money:
            res += i * self.money[i]
        
        return f"Делим денежную сумму на число {res} / {number} = {round(res / number, 2)}"