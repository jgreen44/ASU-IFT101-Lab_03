#   Filename:           Lab 3
#   Created by:         jasongreen
#   Date:               Monday, January 21, 2019
#   Time of Creation:   11:48
#   ---

# find the average of three numbers

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))
number3 = int(input("Please enter your last number: "))

number_avg = (number1 + number2 + number3) / 3
print("The average of {}, {} and {} is {}!".format(number1, number2, number3, number_avg))

avg = 0

for i in range(0, 7):
    number = int(input("Please enter a number: "))
    avg = avg + number

avg = avg / 7
print("The average is: ", avg)



# Ask user to enter a number. Then, depending on whether
# the number is even or odd, print out an appropriate message
# to the user.

while True:
    number = int(input("Please enter a number: "))
    number_modulo = number % 2

    if number_modulo == 0:
        print("You entered: {}. \nDid you know that {} is an even number?".format(number, number))
        try_again = input("Would you like to try another number?(y/n): ")
        if try_again == 'n':
            break
    elif number_modulo != 0:
        print("You entered: {}. \nDid you know that {} is an odd number?".format(number, number))
        try_again = input("Would you like to try another number?(y/n): ")
        if try_again == 'n':
            break