import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json_file(path: str) -> Any:
    """
    Функция чтения данных товарам из json-файла
    :param path: Путь к json-файлу с данными товаров
    :return: Список словарей по товарам
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    return json_data


def create_object_class_from_json(data: list[dict]) -> list[Category]:
    """
    Функция создания объектов классов из данных, полученных из json-файла
    :param data: Список словарей данных, прочитанных из json-файла
    :return: Список объектов классов категорий товаров и самих товаров
    """
    list_category = []
    for data_category in data:
        list_product = []
        for data_product in data_category["products"]:
            list_product.append(Product(**data_product))

        data_category["products"] = list_product
        list_category.append(Category(**data_category))

    return list_category
