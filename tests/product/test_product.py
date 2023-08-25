from inventory_report.product import Product


def test_create_product() -> None:
    produto = Product(
        "001",
        "paçoquinha",
        "Brasil",
        "26/06/2023",
        "26/08/2023",
        "123456789",
        "Frágio",
    )
    assert produto.company_name == "Brasil"
    assert produto.expiration_date == "26/08/2023"
    assert produto.id == "001"
    assert produto.manufacturing_date == "26/06/2023"
    assert produto.product_name == "paçoquinha"
    assert produto.serial_number == "123456789"
    assert produto.storage_instructions == "Frágio"
