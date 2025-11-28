class CategoryIterator:
    """
    Класс итерации по категории товаров
    """

    def __init__(self, category):
        """
        Инициализация класса итерации по категории товаров
        :param category: Объект класса Category
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """
        Магический метод по возвращению итератора для объекта
        :return: Итератор объекта
        """
        self.index = 0
        return self

    def __next__(self):
        """
        Магический метод по возвращению следующего элемента в итерации
        :return: Следующий метод в итерации
        """
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
