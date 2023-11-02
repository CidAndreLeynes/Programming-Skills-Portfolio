ticket_prices = {'under 3': 0, '3 to 12': 10, 'over 12': 15}

while True:
    age = input("What's your age? ")
    age = int(age)
    break

if age < 3:
    print("Your ticket is free!")
elif age < 12:
    print("Your ticket is $10!")
else:
    print("Your ticket is $15!")


"""  
In the first line, we define a dictionary called `ticket_prices` that maps age ranges to ticket prices.

In the second line, we enter a loop that prompts the user to enter their age.

In the third line, we use the `input()` function to ask the user their age. We store the user's input in a string variable called `age`.

The fourth line uses the `int()` function to convert the user's age to an integer. We assign the converted age to the same `age` variable.

The fifth line is a break statement that exits the loop if the user inputs a valid age (an integer).

Outside of the loop, we print the ticket price based on the user's age. If the user enters an age less 
than 3, we print that their ticket is free. If the user enters an age between 3 and 12, we print that 
their ticket is $10. Otherwise, if the user enters an age over 12, we print that their ticket is $15.
"""