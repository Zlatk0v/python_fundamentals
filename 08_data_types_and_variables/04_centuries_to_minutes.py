# input
centuries = int(input())

# logic
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

# output
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
