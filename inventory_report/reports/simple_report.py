import datetime
from typing import List, Optional, Dict

from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self.storages: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.storages.append(inventory)

    def generate(self) -> str:
        oldest_manuf_date = (
            self._find_oldest_manufacturing_date() or datetime.datetime.now()
        )
        closest_exp_date = (
            self._find_closest_expiration_date() or datetime.datetime.now()
        )
        largest_inventory_company = self._find_largest_inventory_company()

        result = (
            f"Oldest manufacturing date:"
            f" {oldest_manuf_date.strftime('%Y-%m-%d')}\n"
            f"Closest expiration date:"
            f" {closest_exp_date.strftime('%Y-%m-%d')}\n"
            f"Company with the largest inventory: {largest_inventory_company}"
        )

        return result

    def _find_oldest_manufacturing_date(self) -> Optional[datetime.datetime]:
        oldest_manuf_date: Optional[datetime.datetime] = None

        for inventory in self.storages:
            for product in inventory.data:
                manufacturing_date = datetime.datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                )
                if (
                    oldest_manuf_date is None
                    or manufacturing_date < oldest_manuf_date
                ):
                    oldest_manuf_date = manufacturing_date

        return oldest_manuf_date

    def _find_closest_expiration_date(self) -> Optional[datetime.datetime]:
        closest_exp_date: Optional[datetime.datetime] = None
        current_date = datetime.datetime.now()

        for inventory in self.storages:
            for product in inventory.data:
                expiration_date = datetime.datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                )
                if expiration_date >= current_date and (
                    closest_exp_date is None
                    or expiration_date < closest_exp_date
                ):
                    closest_exp_date = expiration_date

        return closest_exp_date

    def _find_largest_inventory_company(self) -> str:
        company_inventory_counts: Dict[str, int] = {}

        for inventory in self.storages:
            for product in inventory.data:
                company_name = product.company_name
                company_inventory_counts[company_name] = (
                    company_inventory_counts.get(company_name, 0) + 1
                )

        largest_inventory_company = max(
            company_inventory_counts, key=lambda k: company_inventory_counts[k]
        )

        return largest_inventory_company
