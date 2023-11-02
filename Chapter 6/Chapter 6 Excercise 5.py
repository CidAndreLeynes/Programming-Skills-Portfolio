sandwich_orders = ['BLT', 'Tuna', 'Lobster Roll', 'Pastrami']
finished_sandwiches = []

while 'Pastrami' in sandwich_orders:
    print("We are out of Pastrami!")
    for s in sandwich_orders:
        if s == 'Pastrami':
            sandwich_orders.remove(s)
    else:
        print('Pastrami sold out')

for s in sandwich_orders:
    finished_sandwiches.append(s)

finished_sandwiches.sort()

print("You have made the following sandwiches:\n")
for s in finished_sandwiches:
    print(s)

"""  
In this code, we first check if 'Pastrami' appears in the sandwich_orders list. If it does, we remove it 
from the list and print a message saying that the deli is out of pastrami. If 'Pastrami' does not appear 
in the list, we print a message saying that Pastrami is sold out.
Next, we use a for loop to iterate through the list of sandwiches and add them to the finished_sandwiches 
list. This list is then sorted and printed at the end of the program.
"""