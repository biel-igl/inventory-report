from typing import List, Optional

from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None) -> None:
        self._data = data or []

    def add_data(self, data: List[Product]) -> None:
        self._data += data

    @property
    def data(self) -> List[Product]:
        return self._data
