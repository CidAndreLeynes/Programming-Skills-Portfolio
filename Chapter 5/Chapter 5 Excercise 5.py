pets = [
    {'kind': 'dog', 'owner': 'Cid'},
    {'kind': 'cat', 'owner': 'Yuan'},
    {'kind': 'rabbit', 'owner': 'Rohan'},
]

for pet in pets:
    print('The kind of animal is:', pet['kind'])
    print('The owner of the animal is:', pet['owner'])
    print()

""" 
The code above defines a new list called `pets` with three dictionaries in it. 
Each dictionary represents a type of pet (eg. dog, cat, rabbit) and the owner's name.
The `for` loop iterates through the list of dictionaries and prints a sentence for each pet using the 
information stored in the dictionary. The sentence includes the type of pet and its owner's name. 
The `print` statements are separated by a new line character (i.e., `\n`) to get a clean output.

"""