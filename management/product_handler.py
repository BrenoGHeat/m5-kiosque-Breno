from menu import products


def get_product_by_id(id: int):
    for product in products:
        if product.get("_id") == id:
            return product
    else:
        return {}


def get_products_by_type(string):
    products_filter = []
    for product in products:
        if product.get("type") == string:
            products_filter.append(product)
    if len(products_filter):
        return products_filter
    else:
        return products_filter
