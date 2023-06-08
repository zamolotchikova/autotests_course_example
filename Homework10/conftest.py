import pytest
import datetime


@pytest.fixture(scope="session", autouse=True)
def test_session_start_end(request):
    start_time = datetime.datetime.now()
    print(f"\nТесты запущены: {start_time}")

    def session_end():
        end_time = datetime.datetime.now()
        print(f"\nТесты завершены: {end_time}")
        duration = end_time - start_time
        print(f"Время прохождения всех тестов: {duration}")

    request.addfinalizer(session_end)


@pytest.fixture(scope="function")
def test_time(request):
    start_time = datetime.datetime.now()
    print(f"\nТест начал выполняться: {start_time}")

    def test_end():
        end_time = datetime.datetime.now()
        print(f"\nТест закончил выполнение: {end_time}")
        duration = end_time - start_time
        print(f"Время прохождения теста: {duration}")

    request.addfinalizer(test_end)
