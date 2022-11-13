
# Project Euler Problem 8
# Largest product in a series

def greatest_product_in_string(num):
    """
    Reads from a text file and looks for the greatest product of adjacent digits in a number.
    'num' paramater is size of the adjacent digits to be searched for.
    Needs a .txt file called 'number' that contains the number in the same format as Project Euler problem.
    :param num:
    :return: tuple
    """

    # Reads the text file that contains the number and stores it as string
    with open('number.txt') as file_object:
        numbers = file_object.readlines()

    number_string = ''
    for number in numbers:
        number_string += number.strip()

    flag_number = len(number_string) - num
    list_of_products = []
    numberDict = {}

    """
    Algorithm:
    1. Stores desired size of adjacent numbers in order in a temporary list.
    2. Removes the number that is first in string.
    3. Calculate product and stores in a temp. If product is zero goto Step 1.
    4. Store factors and product in a dictonary with factors:product format
    5. Check each value from keys in dictonary, and stops comparing when value is equal -
     - to the greatest product.
    6. Return tuple as (joined string factors as integer, greatest product as integer).
    """

    while len(number_string) >= num:

        temp_list = []

        for x in range(num):
            temp_list.append(number_string[x])

        number_string = number_string[1:]

        product_of_numbers = 1

        for y in temp_list:
            product_of_numbers *= int(y)

        if product_of_numbers == 0:  # Process restarts if product is zero
            continue
        else:
            pass

        temp_number = ''.join(temp_list)
        list_of_products.append(product_of_numbers)

        numberDict.update({int(temp_number):int(product_of_numbers)})

    for key in numberDict.keys():  # Checks for key that results in largest product
        if numberDict[key] == max(list_of_products):
            greatest_product = key
            break
        else:
            pass

    print('*'.join(list(str(greatest_product))) + " = " + str(max(list_of_products)))

    return (greatest_product, max(list_of_products))
