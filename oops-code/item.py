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
        self.__price: float = price
        self.quantity: int = quantity

        # add to all items
        Item.all.append(self)

    @property
    # Property decorator = read-only attribute
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @name.setter
    def name(self, value: str) -> None:
        # length b/w 1 and 10
        if 1 <= len(value) <= 10:
            self.__name = value
        else:
            raise Exception("Name should be 1-10 characters!")

    def apply_increment(self, increment: float) -> None:
        """apply increment to price

        price = price + price * increment

        Args:
        increment (float): increment value
        range: 0.0 to 1.0

        Returns:
        None
        """
        if 0.0 < increment < 1:
            self.__price = self.__price + self.__price * increment
        else:
            raise Exception("Increment should be between 0 and 1")

    # encapsulation
    def calulate_total_price(self) -> float:
        """total price of item

        quantity * price

        Returns:
            int: total price of item
        """
        total_price: float = self.__price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """apply discount to price

        Returns:
            float: discounted price
        """
        self.__price = self.__price * self.pay_rate

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

    # abstraction
    def __connect(self, smtp_server: str) -> None:
        print(f"connected to {smtp_server}")
        pass

    def __prepare_body(self) -> str:
        return f"""
        Hello

        We have {self.quantity} {self.name} in stock.

        Regards,
        Alok Shandilya
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("smtp.gmail.com")
        self.__prepare_body()
        self.__send()
        print("email sent successfully")

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"
