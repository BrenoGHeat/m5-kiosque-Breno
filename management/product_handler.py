from menu import products


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
    for product in products:
        if product.get("_id") == id:
            return product

    return {}


def get_products_by_type(string):
    if not isinstance(string, string):
        raise TypeError("product type must be a str")
    products_filter = []
    for product in products:
        if product.get("type") == string:
            products_filter.append(product)

    return products_filter


def add_product(menu: list, **kwargs):
    max_id = 0
    if len(menu):
        max_product = max(menu, key=lambda product: product["_id"])
        max_id = max_product["_id"]

    new_id = max_id + 1

    new_product = {"_id": new_id, **kwargs}

    menu.append(new_product)
    return new_product
