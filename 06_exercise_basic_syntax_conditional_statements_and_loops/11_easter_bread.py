# input
budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
cost_per_loaf = price_flour + price_eggs + (price_milk * 0.25)

# variables
number_of_loaves = 0
colored_eggs = 0

# logic
while budget >= cost_per_loaf:
    budget -= cost_per_loaf
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0 and number_of_loaves > 2:
        colored_eggs -= (number_of_loaves - 2)

# output
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
