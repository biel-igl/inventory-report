from inventory_report.product import Product


def test_product_report() -> None:
    produto = Product(
        "001",
        "paçoquinha",
        "Brasil",
        "26/06/2023",
        "26/08/2023",
        "123456789",
        "Frágio",
    )

    assert (
        f"{produto}"
        == "The product 001"
        " - paçoquinha with serial number 123456789 manufactured on"
        " 26/06/2023 by the company Brasil valid until 26/08/2023 "
        "must be stored according to the following instructions: Frágio."
    )
