#Create a function called divisible_by_ten() that has one parameter named num.

#The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num):
    result = num % 10
    if result == 0:
        return True
    else:
        return False

test = input("Enter a number you wish to test:")
num = float(test)
print(divisible_by_ten(num))
