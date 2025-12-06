import pytest

from src.category import Category
from src.product import Product


def test_category_init(fixture_category: Category) -> None:
    """
    Тест класса категорий товаров
    :param fixture_category: Фикстура категории товаров
    :return: Результаты тестов
    """
    assert fixture_category.name == "Телевизоры"
    assert fixture_category.description == "Современный телевизор"
    assert fixture_category.category_count == 1
    assert fixture_category.product_count == 1


def test_products(fixture_category_second: Category) -> None:
    """
    Тест печати товаров категории
    :param fixture_category_second: Фикстура двух товаров в категории
    :return: Результаты тестов
    """
    assert fixture_category_second.products_in_str == (
        '55" QLED 4K, 12000 руб.Остаток: 7 шт.\n' "Iphone 15, 210000.0 руб.Остаток: 8 шт."
    )


def test_add_product(fixture_category_second: Category) -> None:
    """
    Тест на увеличение счетчика количества товаров в категории
    :param fixture_category_second: Фикстура двух товаров
    :return: Результаты теста
    """
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    fixture_category_second.add_product(product2)
    assert fixture_category_second.category_count == 3


def test_add_product_error(fixture_category_second: Category) -> None:
    """
    Тест на ошибочный класс при добавлении товара или продукта в категорию
    :return: Результат теста
    """
    with pytest.raises(TypeError):
        fixture_category_second.add_product(1)


def test_number_of_products(fixture_category_second) -> None:
    """
    Тест формирования f-строки по общему количеству товаров/продуктов в категории
    :param fixture_category_second: Фикстура двух товаров
    :return: Результаты теста
    """
    assert str(fixture_category_second) == "Телевизоры, количество продуктов: 15 шт."
