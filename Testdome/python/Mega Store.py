from enum import Enum, auto


class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()


def get_discounted_price(cart_weight, total_price, discount_type):
    if discount_type == DiscountType.WEIGHT:
        discount = 0.18 if cart_weight > 10 else 0.06
    elif discount_type == DiscountType.SEASONAL:
        discount = 0.12
    else:
        discount = 0.06

    return total_price * (1 - discount)


print(get_discounted_price(12, 100, DiscountType.WEIGHT))
