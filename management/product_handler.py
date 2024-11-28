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
            return products_filter.append(product)
    else:
        return products_filter
