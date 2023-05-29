class Segment:
    def __init__(self, tup1, tup2):
        self.x1 = tup1[0]
        self.x2 = tup2[0]
        self.y1 = tup1[1]
        self.y2 = tup2[1]

    def length(self):
        """Возвращает длину отрезка, с округлением до 2 знаков после запятой
        :return: float
        """
        return round(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5, 2)

    def x_axis_intersection(self):
        """Возвращает True, если отрезок пересекает ось абцисс
        :return: bool
        """
        return self.y2 >= 0

    def y_axis_intersection(self):
        """Возвращает True, если отрезок пересекает ось ординат
        :return: bool
        """
        return self.x1 <= 0

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

