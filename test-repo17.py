# Python function multiplying numbers
# Python using for loop inside def function
# to calculate the numbers inside tuples
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number     # using augmented assignment operator
    return total


print(multiply(2,3,4,5))