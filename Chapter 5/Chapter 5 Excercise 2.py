programming_terms = {
    'function': 'A grouping of code that performs a specific task and can be called multiple times in your program',
    'variable': 'A piece of data stored in your program that you can name and change the value of',
    'loop': 'A block of code that repeats a set of instructions a specific number of times or until a certain condition is met',
    'exception': 'An error that causes your program to stop executing or to behave unexpectedly',
    'data structure': 'A way to organize and manipulate data in your program, such as lists, dictionaries, and arrays'
}

for word, description in programming_terms.items():
    print(word, ':', "\n")
    print(description, ':')
    print()

"""  
Sure! In this code, we are using a Python dictionary to store five programming words along with their meanings. A dictionary in Python is a data type that allows us to associate keys with values, much like storing information in a folder with labeled tabs.

In this case, the keys in the dictionary represent the five programming words ('function', 'variable', 'loop', 'exception', and 'data structure') and the values in the dictionary represent their respective meanings.

When we loop through the dictionary using the "for word, description in programming_terms.items():" statement, we access each key-value pair in the dictionary. We then print each key followed by ":" and then the value, for example "function: A grouping of code that performs a specific task and can be called multiple times in your program".
"""