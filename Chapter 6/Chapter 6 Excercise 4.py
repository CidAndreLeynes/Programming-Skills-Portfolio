sandwich_orders = ['BLT', 'Tuna', 'Lobster Roll']
finished_sandwiches = []

for sandwich in sandwich_orders:
    message = f"I made your {sandwich} sandwich."
    finished_sandwiches.append(sandwich)
    print(message)

message = f"\nYou have made the following sandwiches:\n"
for sandwich in finished_sandwiches:
    message +=", " + sandwich
    print(message)


"""  
In this code, we first create a list of sandwich orders, which we could replace with a list of the 
ingredients in the sandwiches if needed. Then we create an empty list called finished_sandwiches which 
will contain all the finished sandwiches after the loop is completed.We then enter a loop that iterates 
through the list of sandwich orders, printing a message with the type of sandwich made for each order. 
We then append the sandwich order to the list of finished sandwiches and move on to the next order.
After all the sandwiches have been made, we print a new message that lists all the finished sandwiches.
"""