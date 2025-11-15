import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """
    Функция чтения данных товарам из json-файла
    :param path: Путь к json-файлу с данными товаров
    :return: Список словарей по товарам
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    return json_data


def create_object_class_from_json(data: list[dict]) -> list[object]:
    """
    Функция создания объектов классов из данных, полученных из json-файла
    :param data: Список словарей данных, прочитанных из json-файла
    :return: Список объектов классов категорий товаров и самих товаров
    """
    list_category = []
    for data_category in data:
        list_product = []
        for data_product in data_category['products']:
            list_product.append(Product(**data_product))

        data_category['products'] = list_product
        list_category.append(Category(**data_category))

    return list_category


if __name__ == "__main__":
    path = "../data/products.json"

    data_list = create_object_class_from_json(read_json(path))
    for item in data_list:
        print(f'Категория - {item.name}')
        print(f'Описание - {item.description}')
        for item_product in item.products:
            print(f'Товар - {item_product.name}')
            print(f'Описание - {item_product.description}')
            print(f'Цена - {item_product.price}')
            print(f'Количество - {item_product.quantity}')
            print(f'Сумма - {item_product.price * item_product.quantity}')
            print('-' * 50)
        print('=' * 50)


