pokemon_distances = list(map(int, input().split()))

removed_sum = 0

while len(pokemon_distances) > 0:
    index = int(input())

    if index < 0:
        removed_element = pokemon_distances[0]
        pokemon_distances[0] = pokemon_distances[-1]
    elif index >= len(pokemon_distances):
        removed_element = pokemon_distances[-1]
        pokemon_distances[-1] = pokemon_distances[0]
    else:
        removed_element = pokemon_distances.pop(index)

    removed_sum += removed_element

    for i in range(len(pokemon_distances)):
        if pokemon_distances[i] <= removed_element:
            pokemon_distances[i] += removed_element
        else:
            pokemon_distances[i] -= removed_element

print(removed_sum)
