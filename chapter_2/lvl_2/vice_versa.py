

def vice_versa(number):
    while len(str(number)) != 2:
            number = int(input('Please, enter a two-digit number: '))

    l_number = list(str(number))
    number_l = list(reversed(l_number))
    gegenuber = int(''.join(number_l))
    return number, gegenuber

