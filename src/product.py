class Product:
    """
    Класс товаров и их цены и количества
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, value):
        if value > 0:
            if self.__price <= value:
                self.__price = value
            else:
                answer_user = input('Введена цена ниже текущей. Установить введенную цену? (Y/n) ')
                if answer_user == 'Y' or answer_user == 'y' or answer_user == '':
                    self.__price = value
        else:
            print('Цена не должна быть нулевая или отрицательная')


    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int, list_product: list = []):
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        if len(list_product) > 0:
            add_for_list = 1
            for product in list_product:
                if product.name == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    add_for_list = 0
                    return
            if add_for_list:
                list_product.append(cls(name, description, price, quantity))
        return cls(name, description, price, quantity)
