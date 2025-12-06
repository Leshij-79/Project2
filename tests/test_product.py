import pytest

from src.product import LawnGrass, Product, Smartphone


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
    message = capsys.readouterr()
    fixture_product.price = 0.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


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


@pytest.mark.parametrize(
    "data_dict", [{"name": '55" QLED 4K-1', "description": "Фоновая подсветка", "price": 125000, "quantity": 7}]
)
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


def test_product_smartphone_init(fixture_smartphone: Smartphone) -> None:
    assert fixture_smartphone.name == "Iphone 15"
    assert fixture_smartphone.description == "512GB, Gray space"
    assert fixture_smartphone.price == 210000.0
    assert fixture_smartphone.quantity == 8
    assert fixture_smartphone.efficiency == 98.2
    assert fixture_smartphone.model == "15"
    assert fixture_smartphone.memory == 512
    assert fixture_smartphone.color == "Gray space"


def test_product_lawngrass_init(fixture_lawngrass: LawnGrass) -> None:
    assert fixture_lawngrass.name == "Газонная трава"
    assert fixture_lawngrass.description == "Элитная трава для газона"
    assert fixture_lawngrass.price == 500.0
    assert fixture_lawngrass.quantity == 20
    assert fixture_lawngrass.country == "Россия"
    assert fixture_lawngrass.germination_period == "7 дней"
    assert fixture_lawngrass.color == "Зеленый"


def test_product_smartphone_add(fixture_smartphone: Smartphone, fixture_smartphone_second: Smartphone) -> None:
    assert fixture_smartphone + fixture_smartphone_second == 2580000.0


def test_product_lawngrass_add(fixture_lawngrass: LawnGrass, fixture_lawngrass_second: LawnGrass) -> None:
    assert fixture_lawngrass + fixture_lawngrass_second == 16750.0


def test_product_smartphone_add_error(fixture_smartphone: Smartphone) -> None:
    with pytest.raises(TypeError):
        fixture_smartphone + 1


def test_product_lawngrass_add_error(fixture_lawngrass: LawnGrass) -> None:
    with pytest.raises(TypeError):
        fixture_lawngrass + 1


def test_print_product(fixture_product) -> None:
    """
    Тест магического метода __str__ для формирования f-строки по товару/продукту для печати
    :param fixture_product: Фикстура товара
    :return: Результат теста
    """
    assert str(fixture_product) == '55" QLED 4K, 12000 руб. Остаток: 7'


def test_add_products() -> None:
    """
    Тест магического метода __add__ для расчета общей суммы по двум товарам
    :return: Результат теста
    """
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert (product1 + product2) == 2580000.0
