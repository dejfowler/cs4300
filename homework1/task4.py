
def calculate_discount(price, discount):
    if discount >= 1:
        discount = discount/100
    return round(price * (1-discount), 2)

