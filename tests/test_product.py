def test_product_init(fixture_product) -> None:
    """
    Тест инициализации класса товаров
    :param fixture_product: Фикстура товаров
    :return: Результат тестов
    """
    assert fixture_product.name == '55" QLED 4K'
    assert fixture_product.price == 12000
    assert fixture_product.quantity == 7
    assert fixture_product.description == "Фоновая подсветка"
