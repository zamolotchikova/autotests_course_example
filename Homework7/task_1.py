# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

# Здесь пишем код
class Segment:
    def __init__(self, pointA, pointB):
        self.x1 = pointA[0]
        self.y1 = pointA[1]
        self.x2 = pointB[0]
        self.y2 = pointB[1]

    def length(self):
        """
        Метод возвращает длину отрезка, с округлением до 2 знаков
        :return: float
        """
        return round(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5, 2)

    def x_axis_intersection(self):
        """
        Метод возвращает True, если отрезок пересекает ось абцисс, иначе False
        :return: bool
        """
        if self.y1 < 0 < self.y2 or self.y2 < 0 < self.y1:
            return True
        else:
            return False
 #       return self.y2 >= 0

    def y_axis_intersection(self):
        """
        Метод возвращает True, если отрезок пересекает ось ординат, иначе False
        :return: bool
        """
        if self.x1 < 0 < self.x2 or self.x2 < 0 < self.x1:
            return True
        else:
            return False
 #       return self.x1 <= 0



# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
