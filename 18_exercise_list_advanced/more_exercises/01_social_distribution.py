# input
population = list(map(int, input().split(", ")))
min_wealth = int(input())

# logic and output
total_wealth = sum(population)
needed_wealth = min_wealth * len(population)
if total_wealth < needed_wealth:
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            needed = min_wealth - population[i]
            max_index = population.index(max(population))
            population[max_index] -= needed
            population[i] += needed
    print(population)
