smallPizza = 15
mediumPizza = 20
largePizza = 25
pepCostS = 2
pepCostML = 3

pizzaSize = input('What size pizza would you like to order? S, M, L?\n').upper()
addPepperoni = input('Would you like to add pepperoni? Y or N\n').upper()

def getPizzaCost(pizzaSize, addPepperoni):
    if addPepperoni == 'Y':
        if pizzaSize == 'S':
            return smallPizza + pepCostS
        elif pizzaSize == 'M':
            return mediumPizza + pepCostML
        elif pizzaSize == 'L':
            return largePizza + pepCostML
    else:
        if pizzaSize == 'S':
            return smallPizza 
        elif pizzaSize == 'M':
            return mediumPizza 
        elif pizzaSize == 'L':
            return largePizza 

print(f'Your total is ${getPizzaCost(pizzaSize, addPepperoni)}.')