#Create a function named large_power() that takes two parameters named base and exponent.

#If base raised to the exponent is greater than 5000, return True, otherwise return False


def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

test = input("Enter the base and exponent separated by a comma: ")
base, exponent = test.split(",")
base = int(base)
exponent = int(exponent)
print(large_power(base, exponent)) 