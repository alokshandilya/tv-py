from item import Item


class Phone(Item):
    def __init__(
        self,
        name: str,
        price: float,
        quantity: int = 0,
        broken_phones: int = 0,
    ) -> None:
        # call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phones {broken_phones} should be >= 0!"  # noqa: E501

        self.broken_phones: int = broken_phones

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"  # noqa: E501
        )
