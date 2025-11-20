def test_category_init(fixture_category) -> None:
    """
    Тест класса категорий товаров
    :param fixture_category: Фикстура категории товаров
    :return: Результаты тестов
    """
    assert fixture_category.name == "Телевизоры"
    assert fixture_category.description == "Современный телевизор"
    assert fixture_category.category_count == 1
    assert fixture_category.product_count == 1
