inventory = {}

item_count = int(input("How many items do you have in your inventory? "))
for x in range(item_count):
    item_name = input("What is the item? ")
    item_price = input("What is the price? ")
    inventory[item_name] = float(item_price)
    print("--------")

for item, price in inventory.items():
    print("The price of " + item + "is $" + str(price))

    if (price < 5):
        print("this item is on sale!")


print("--------")
