def calculate_total_price(all_product, total_quantity):
    prices = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
    total_price = prices[product] * quantity
    return total_price


product = input().lower()
quantity = int(input())
print(f"{calculate_total_price(product, quantity):.2f}")
