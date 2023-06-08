# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("a, b, result",
                         [
                             pytest.param(1, 5, 0.2, marks=pytest.mark.smoke("smoke test")),
                             pytest.param(1, 0, 0, marks=pytest.mark.skip("skip_test")),
                             (10, 0.2, 50), (1000000, 5, 200000), (-10, 5, -2)
                         ])
def test_test(a, b, result):
    assert all_division(a, b) == result
