import json
from unittest.mock import mock_open, patch

from src.utils import create_object_class_from_json, read_json_file


@patch("builtins.open", new_callable=mock_open)
def test_read_json(mock_json_file) -> None:
    """Тестирование чтения json-файла"""
    data_mock_for_test = [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]

    mock_file = mock_json_file.return_value
    mock_file.read.return_value = json.dumps(data_mock_for_test)

    assert read_json_file("") == data_mock_for_test


def test_create_object_class_from_json() -> None:
    data = [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]
    result = create_object_class_from_json(data)
    assert result[0].name == "Телевизоры"
    assert result[0].description == "Современный телевизор"
    assert result[0].products[0].name == '55" QLED 4K'
    assert result[0].products[0].description == "Фоновая подсветка"
    assert result[0].products[0].price == 123000.0
    assert result[0].products[0].quantity == 7
    assert result[0].category_count == 2
    assert result[0].product_count == 2
