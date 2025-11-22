from src.category import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства " "жизни",
        [product1, product2, product3],
    )

    print(category1.products_in_str)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    list_product = [product1, product2, product3, product4]

    print(category1.products_in_str)
    print(category1.product_count)

    new_product = Product.new_product(
        "Samsung Galaxy S23 Ultra-1", "256GB, Серый цвет, 200MP камера", 180000.0, 5, list_product
    )

    if new_product is not None:
        new_product.price = 800
        print(new_product.price)

        new_product.price = -100
        print(new_product.price)
        new_product.price = 0
        print(new_product.price)
