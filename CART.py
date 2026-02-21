foods = []
prices = []
total_price = 0

while True:
    food = input("enter a food to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter a price to buy a {food}: $"))
        foods.append(food)
        prices.append(price)
print("-----YOUR CART-----")
for food in foods:
    print(food ,end=" ")
for price in prices:
    total_price += price
print(f"your total is: ${total_price}")

