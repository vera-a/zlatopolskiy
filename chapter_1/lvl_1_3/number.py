# Create a programme that prins out the number, that user has input. There should also be a message "You have input" before a numv#er

# user input number
# variable = user_input

# take number in function
# result = function(variable)

# print function returned value
# print result
input_value = input('Insert your number: ')
def return_num(val):
    print('in function: ' + str(val))
    return val
print('Your number is: ' + str(return_num(input_value)))
