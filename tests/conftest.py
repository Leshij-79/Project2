import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def fixture_product() -> Product:
    return Product('55" QLED 4K', "Фоновая подсветка", 12000, 7)


@pytest.fixture
def fixture_category() -> Category:
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[Product(name='55" QLED 4K', description="Фоновая подсветка", price=12000, quantity=7)],
    )
