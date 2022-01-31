# Author: SCT (AMDG) 1/27/22

groceries = [['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt',]]
costs = [1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]
groceries_mod = groceries

def food_costs(groceries,costs): 
    for item in groceries_mod:
        for i,v in enumerate(item):
            new_value = v + ": $" + str(costs[0])
            print(new_value)
            del costs[0]
           

print(food_costs([['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt',]],  [1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49] ))



