river = {
    'nile': 'egypt',
    'tigris': 'iraq, iran',
    'euphrates': 'turkey, syria, iraq'
}

for key, value in river.items():
    print(key, 'runs through', value)

for key in river.keys():
    print(key)

for key in river.keys():
    print(river[key])


""" 
In this code, we create a dictionary called 'river' that maps river names to country names. 
Then, we use a loop to print a sentence about each river (i.e., The 'nile' runs through 'egypt').
Next, we use 2 loops to print the names of each river and the names of each country included in the 
dictionary.
"""