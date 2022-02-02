# Author: SCT (AMDG) 1/31/22

def fibon(number): # def function
    # Conditonals used to set base values for each input
    if number == 1: # 1 will always be 0
        return [0]
    if number == 2: # 2 will alays equal 0,1
        return [0,1]
    fib = [0,1]
    while number > len(fib): # if input is > than 2, continue with series of sum values
        fib.append(fib[-1] + fib[-2])
    return fib

# test cases
print(fibon(5))
print(fibon(10))