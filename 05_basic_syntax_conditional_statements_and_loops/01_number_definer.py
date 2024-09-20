# input
number = float(input())

# logic positive
if number == 0:
    print('zero')

elif number > 0:
    if number < 1:
        print('small positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('positive')

# logic negative
else:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')
