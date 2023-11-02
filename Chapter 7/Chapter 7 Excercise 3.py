def make_shirt(size, phrase):
    message = "Shirt size: {size}\nPrint: {phrase}".format(size=size, phrase=phrase)
    print(message)

# Use the function using positional arguments
make_shirt("Large", "I love Python")

# Use the function using keyword arguments
make_shirt(size="Large", phrase="I love Python")


# Use the function using positional arguments
make_shirt("Large", "I love Python")

# Use the function using keyword arguments
make_shirt(size="Large", phrase="I love Python")

"""  
According to some research I found,
there is no difference between keyword and positional arguments in Python. 
They both achieve the same result. The only difference is in the syntax used when calling the function.

"""
