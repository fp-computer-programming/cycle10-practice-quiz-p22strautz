# Author: SCT (AMDG) 1/31/22

def factorial(number):
    result = 1 # base value to add to
    num = 1 # counter for loop
    if number == 0:
        result = 0 # sets cenario for 0
    else:
        while num <= number: # factorial sum cant go past itself
            result = num * result # sets total = to the total * counter
            num += 1 # counter
    return result

# test case
print(factorial(3))