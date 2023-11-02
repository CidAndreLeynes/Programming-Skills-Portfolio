toppings = []
while True:
    topping = input('Enter a pizza topping: ')
    if topping == 'quit':
        break
    toppings.append(topping)

for topping in toppings:
    print(topping, end='\n')

""" 

Of course! In the above code, we first ask the user to enter a series of pizza toppings, and as they 
enter each topping, we store it in a list called `toppings`. We continue to ask the user to enter
pizza toppings until they enter the word 'quit', at which point we stop adding to the list.
We then loop through the `toppings` list and print each topping on a new line using the `end='\n'` 
parameter in the `print()` function. The `end='\n'` parameter causes the printing of each item to start 
on a new line.This allows us to print all the pizza toppings in a clear and readable format, with each 
topping on its own line.

"""