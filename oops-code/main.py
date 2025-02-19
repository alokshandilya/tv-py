from item import Item
from phone import Phone

Item.instantiate_from_csv()

print(Item.all, end="\n\n")

phone = Phone("Nokia 5.1 Plus", 10000, 10, 3)

phone.name = "iphone"

item = Item("fokat", 100, 10)
print(item.price)

item.apply_increment(0.2)
print(item.price)

item.send_email()
