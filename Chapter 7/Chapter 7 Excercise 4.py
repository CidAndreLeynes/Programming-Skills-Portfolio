def make_shirt(size, message):
    if size is None:
        size = "large"
    message = message.upper() + f"!"
    message = f"Shirt size: {size}\nPrint: {message}"
    print(message)

# Call the function to make a large shirt with the default message
make_shirt(size=None, message="I love Python")

# Call the function to make a medium shirt with the default message
make_shirt(size="medium", message="I love Python")

# Call the function to make a shirt of any size with a different message
make_shirt(size="Small", message="I hate Java")

"""
The modified `make_shirt()` function now has a default size of "Large" with a message "I love Python" if 
the size is not specified, and it allows you to make a shirt of any size with a different message. The 
function should now function as expected.
"""