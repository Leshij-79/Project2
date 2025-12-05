import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def fixture_product() -> Product:
    return Product('55" QLED 4K', "Фоновая подсветка", 12000, 7)


@pytest.fixture
def fixture_smartphone() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def fixture_smartphone_second() -> Smartphone:
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")


@pytest.fixture
def fixture_lawngrass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def fixture_lawngrass_second() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def fixture_category() -> Category:
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[Product(name='55" QLED 4K', description="Фоновая подсветка", price=12000, quantity=7)],
    )


@pytest.fixture
def fixture_category_second() -> Category:
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[
            Product(name='55" QLED 4K', description="Фоновая подсветка", price=12000, quantity=7),
            Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
        ],
    )
