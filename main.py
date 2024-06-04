from Money import *

# создание объекта класса "Money"
money1 = Money({100: 2, 500:1})
money2 = Money({500: 2})
# help(Money)
print(repr(money1))
print(str(money1))
print('-----')
print(money1.__add__(money2))
print(money1.__sub__(money2))
print(money1.__mul__(money2))
print(money1.__truediv__(money2))
print(money1.__eq__(money2))
print(money1.div_on_number(3))
print(money1.umnozh_on_number(3.5))
print(Money.get_instance_count())
del money2
print(Money.get_instance_count())