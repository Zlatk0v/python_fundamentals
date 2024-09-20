# input
year = int(input())


# logic
while True:
    year += 1
    year_str = str(year)

    if len(set(year_str)) == len(year_str):
        break
# output
print(year)
