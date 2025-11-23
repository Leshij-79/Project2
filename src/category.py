from src.product import Product


class Category:
    """
    Класс категорий продуктов
    """

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Инициализация класса Category
        :param name: Имя категории в формате строки
        :param description: Описание категории в формате строки
        :param products: Список продуктов категории в формате списка класса Product
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products_in_str(self) -> str:
        """
        Формирование строки для печати списка продуктов/товаров в текущей категории
        :return: Возвращает строку для печати списка  продуктов/товаров
        """
        return_str = ""
        item_int = 1
        for item in self.__products:
            if item_int < len(self.__products):
                return_str += f"{item.name}, {item.price} руб.Остаток: {item.quantity} шт.\n"
            else:
                return_str += f"{item.name}, {item.price} руб.Остаток: {item.quantity} шт."
            item_int += 1
        return return_str

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт/товар в категорию продуктов/товаров
        :param product: Объект класса Product
        """
        Category.product_count += 1
        self.__products.append(product)
