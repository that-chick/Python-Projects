toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell" + str(num_pizzas), "different kinds of pizza")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"],[2, "olives"],[7,"anchovies"],[2, "mushrooms"]]

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices [1]
priciest_pizza = pizza_and_prices [-1]
pizza_and_prices.pop(-1)
pizza_and_prices.insert(2,[2.5, "peppers"])

three_cheapest = pizza_and_prices [0:2], pizza_and_prices [3:4]
print(pizza_and_prices)
print(three_cheapest)

#pizza's good. Duh.
