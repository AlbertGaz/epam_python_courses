"""Homework 11.2."""

from typing import Callable


class Order:
    """Order class. Contain price and discount."""

    def __init__(self, price: int, discount: Callable) -> None:
        self.price = price
        self.discount_fun = discount

    def discount_calc(self) -> float:
        """Calculate discount."""
        self.discount = self.discount_fun(self)
        if 0 <= self.discount <= self.price:
            return self.discount
        return 0

    def final_price(self) -> float:
        """Calculate final price."""
        return self.price - self.discount_calc()
