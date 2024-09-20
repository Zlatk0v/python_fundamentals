# input
number_for_message = int(input())

# logic and output
for message in range(number_for_message):
    current_number = int(input())
    if current_number == 88:
        print('Hello')
    elif current_number == 86:
        print('How are you?')
    elif current_number < 88:
        print('GREAT!')
    else:
        print('Bye.')
