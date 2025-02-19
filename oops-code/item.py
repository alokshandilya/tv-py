from __future__ import annotations

import csv
from typing import Any, Dict


class Item:
    pay_rate: float = 0.8  # 20% discount
    all: list[Item] = []

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        """initialize item

        Args:
            name (str): name of item
            price (float): price of item
            quantity (int, optional): quantity of item. Defaults to 0.
        """

        # validations
        assert price > 0.0, f"Price {price} should be greater than 0!"
        assert (
            quantity >= 0
        ), f"Quantity {quantity} should be greater than or equal to 0!"

        # assign to self object
        self.__name: str = name
        self.price: float = price
        self.quantity: int = quantity

        # add to all items
        Item.all.append(self)

    @property
    # Property decorator = read-only attribute
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            raise Exception("Name too long!")
        if len(value) == 0:
            raise Exception("Name cannot be blank!")
        else:
            self.__name = value

    def calulate_total_price(self) -> float:
        """total price of item

        quantity * price

        Returns:
            int: total price of item
        """
        total_price: float = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """apply discount to price

        Returns:
            float: discounted price
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader: csv.DictReader = csv.DictReader(f)
            items: list[Dict[str, str]] = list(reader)

        for item in items:
            Item(
                name=item.get("name", ""),
                price=float(item.get("price", 0)),
                quantity=int(item.get("quantity", 0)),
            )

    @staticmethod
    def is_integer(num: int | float | Any) -> bool:
        """check if number is integer

        counts float as integer if decimal is 0
        e.g. 5.0 is integer

        Args:
        num (int | float): number to check

        Returns:
        bool: True if number is integer, False otherwise
        """
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"
