import pytest


def test_category_iterator(fixture_category_iterator) -> None:
    """
    Тестирование класса итерации по категории товаров
    :param fixture_category_iterator: Фикстура итератора категории
    :return: Результаты тестов
    """
    iter(fixture_category_iterator)
    assert fixture_category_iterator.index == 0
    assert next(fixture_category_iterator).name == '55" QLED 4K'
    assert next(fixture_category_iterator).name == "Iphone 15"
    with pytest.raises(StopIteration):
        next(fixture_category_iterator)
