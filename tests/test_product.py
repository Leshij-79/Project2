import pytest

from src.product import Product


def test_product_init(fixture_product: Product) -> None:
    """
    Тест инициализации класса товаров
    :param fixture_product: Фикстура товаров
    :return: Результат тестов
    """
    assert fixture_product.name == '55" QLED 4K'
    assert fixture_product.price == 12000
    assert fixture_product.quantity == 7
    assert fixture_product.description == "Фоновая подсветка"


def test_product_price_setter(fixture_product: Product) -> None:
    """
    Тест сеттера изменения цены товара
    :param fixture_product: Фикстура товара
    :return: Результат теста
    """
    fixture_product.price = 13000.0
    assert fixture_product.price == 13000


def test_product_price_setter_zero_price(capsys, fixture_product: Product) -> None:
    """
    Тест сеттера изменения цены товара на 0
    :param fixture_product: Фикстура товара
    :return: Результат теста
    """
    fixture_product.price = 0.0
    message = capsys.readouterr()[0]
    assert message == "Цена не должна быть нулевая или отрицательная\n"


@pytest.mark.parametrize("data_dict", [({'name': '55" QLED 4K', 'description': "Фоновая подсветка",
                                         'price': 12000, 'quantity': 7})])
def test_product_new_product(data_dict: dict) -> None:
    """
    Тест на добавление товара
    Использование параметризации
    :return: Результат теста
    """
    assert Product.new_product(data_dict).name == data_dict['name']


@pytest.mark.parametrize("data_dict", [({'name': '55" QLED 4K', 'description': "Фоновая подсветка",
                                         'price': 0, 'quantity': 7})])
def test_product_new_product_zero_price(capsys, data_dict: dict) -> None:
    """
    Тест на добавление товара с нулевой ценой
    Использование параметризации
    :return: Результат теста
    """
    Product.new_product(data_dict)
    message = capsys.readouterr()[0]
    assert message == "Цена не должна быть нулевая или отрицательная\n"


@pytest.mark.parametrize("data_dict", [({'name': '55" QLED 4K', 'description': "Фоновая подсветка",
                                         'price': 120000, 'quantity': 7})])
def test_product_new_product_double_product(data_dict: dict) -> None:
    """
    Тест на добавление товара с дублированием наименования
    Использование параметризации
    :return: Результат теста
    """
    list_product = [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)]
    Product.new_product(data_dict, list_product)
    assert list_product[0].price == 123000.0
    assert list_product[0].quantity == 14


@pytest.mark.parametrize("data_dict", [({'name': '55" QLED 4K', 'description': "Фоновая подсветка",
                                         'price': 125000, 'quantity': 7})])
def test_product_new_product_double_product_second(data_dict: dict) -> None:
    """
    Тест на добавление товара с дублированием наименования
    Использование параметризации
    :return: Результат теста
    """
    list_product = [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)]
    Product.new_product(data_dict, list_product)
    assert list_product[0].price == 125000.0
    assert list_product[0].quantity == 14


@pytest.mark.parametrize("data_dict", [({'name': '55" QLED 4K-1', 'description': "Фоновая подсветка",
                                         'price': 125000, 'quantity': 7})])
def test_product_new_product_double_product_third(data_dict) -> None:
    """
    Тест на добавление товара
    Использование параметризации
    :return: Результат теста
    """
    list_product = [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)]
    Product.new_product(data_dict, list_product)
    assert list_product[1].name == '55" QLED 4K-1'
    assert list_product[1].price == 125000.0
    assert list_product[1].quantity == 7
