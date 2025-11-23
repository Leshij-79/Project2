from typing import Any


class Product:
    """
    Класс товаров и их цены и количества
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация класса Product
        :param name: Наименование продукта/товара в формате строки
        :param description: Описание продукта/товара в формате строки
        :param price: Цена продукта/товара в формате числа с плавающей точкой
        :param quantity: Количество на складе в формате целого числа
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> Any:
        """
        Геттер приватного атрибута цена
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> Any:
        """
        Сеттер приватного атрибута price с проверкой цены на 0 и отрицательность, а также на понижение цены
        :param value: Новая цена продукта/товара в формате числа с плавающей точкой
        """
        if value > 0:
            if self.__price <= value:
                self.__price = value
            else:
                answer_user = input("Введена цена ниже текущей. Установить введенную цену? (Y/n) ")
                if answer_user == "Y" or answer_user == "y" or answer_user == "":
                    self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, data_dict: dict, list_product: list = []):
        """
        Классовый метод для добавления нового продукта/товара с проверкой на повторение (опционально) с суммированием
        количества продукта/товара на складе и установления большей цены из повторяющихся, в тч с проверкой цены на
        0 или отрицательность
        :param data_dict: Данные по товару в формате словаря
        :param list_product: Список объектов класса Product
        :return: Ссылка на объект класса Product
        """
        if data_dict['price'] <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if len(list_product) > 0:
            add_for_list = 1
            for product in list_product:
                if product.name == data_dict['name']:
                    product.quantity += data_dict['quantity']
                    if product.price < data_dict['price']:
                        product.price = data_dict['price']
                    add_for_list = 0
                    return
            if add_for_list:
                list_product.append(cls(data_dict['name'], data_dict['description'],
                data_dict['price'], data_dict['quantity']))
        return cls(data_dict['name'], data_dict['description'], data_dict['price'], data_dict['quantity'])
