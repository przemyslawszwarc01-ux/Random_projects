#shopping cart script
#learning lists and adding to them

products = []
prices = []
total_price = 0

while True:
    product = input("Enter product name: ")
    if product == "quit":
        break
    try:
        price = float(input("Enter price: "))
        prices.append(price)
    except ValueError:
        print("only numbers are allowed")
        break
    products.append(product)

print("_____Your Shopping Cart_____")
print(*products, sep="\n")
total_price = sum(prices)
total_price = round(total_price, 2)
print(f"Total price: ${total_price}")

