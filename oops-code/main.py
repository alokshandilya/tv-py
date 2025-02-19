from item import Item
from phone import Phone

Item.instantiate_from_csv()

print(Item.all, end="\n\n")

phone = Phone("Nokia 5.1 Plus", 10000, 10, 3)

phone.name = "iphone"

print(Phone.all)
