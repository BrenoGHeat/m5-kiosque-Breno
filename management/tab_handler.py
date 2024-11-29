from menu import products


def calculate_tab(consumption: list):
    total = 0
    for order in consumption:
        for product in products:
            if order["_id"] == product["_id"]:
                total += product["price"] * order["amount"]
    return {'subtotal': f'${round(total, 2)}'}
