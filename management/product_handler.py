def get_product_by_id(id: int):
    for product in products:
        if product.get("_id") == id:
            return product
    else:
        return {}
