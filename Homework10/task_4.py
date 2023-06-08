# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class Test_test:

    def test_zero(self, test_time):
        with pytest.raises(ZeroDivisionError):
            all_division(1, 0)

    def test_five(self):
        assert (all_division(1, 5)) == 0.2

    def test_number_negative(self):
        assert (all_division(-10, 5)) == -2

    def test_point(self):
        assert (all_division(10, 0.2)) == 50

    def test_number_big(self, test_time):
        assert (all_division(1000000, 5)) == 200000
