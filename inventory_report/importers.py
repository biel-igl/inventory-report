from abc import ABC, abstractmethod
import json
from typing import Dict, List, Type

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        produtos = []
        with open(self.path) as file:
            products = json.load(file)
            produtos = [
                Product(
                    product["id"],
                    product["product_name"],
                    product["company_name"],
                    product["manufacturing_date"],
                    product["expiration_date"],
                    product["serial_number"],
                    product["storage_instructions"],
                )
                for product in products
            ]
        return produtos


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
