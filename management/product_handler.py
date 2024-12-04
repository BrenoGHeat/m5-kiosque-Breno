from menu import products
from collections import Counter


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
    for product in products:
        if product.get("_id") == id:
            return product

    return {}


def get_products_by_type(string):
    if not isinstance(string, str):
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


def menu_report():
    product_count = len(products)
    prices = []
    types = []
    for product in products:
        prices.append(product["price"])
        types.append(product["type"])

    average_price = sum(prices) / product_count
    average_price = round(average_price, 2)

    counter_types = Counter(types)
    print(counter_types)
    most_commom_type = counter_types.most_common(1)[0][0]

    return (f'Products Count: {product_count} - ' +
            f'Average Price: ${average_price} - ' +
            f'Most Common Type: {most_commom_type}')
