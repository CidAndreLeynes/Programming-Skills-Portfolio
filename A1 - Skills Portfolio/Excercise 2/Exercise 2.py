import random  # Import the random module to randomly select jokes

# Function to load jokes from a file
def load_jokes(filename):
    # Open the file and read each line
    with open(filename, "r") as file:
        # Split each line by "?" and store as a list of [setup, punchline] pairs
        jokes = [line.strip().split('?') for line in file if '?' in line]
    return jokes  # Return the list of jokes

# Function to handle the main joke-telling interaction
def tell_jokes(jokes):
    # Display instructions for the user
    print("Type 'Alexa tell me a joke' to hear a joke, or 'quit' to exit.")
    while True:  # Start an infinite loop to continue until user quits
        user_input = input("Your command: ").strip().lower()  # Get and normalize user input
        if user_input == "quit":  # Check if the user wants to quit
            print("Goodbye!")  # Print farewell message
            break  # Exit the loop if user typed "quit"
        elif user_input == "alexa tell me a joke":  # Check if user requested a joke
            setup, punchline = random.choice(jokes)  # Randomly select a joke
            print("Setup:", setup + "?")  # Display the setup part of the joke
            input("Press Enter for the punchline...")  # Wait for user to press Enter
            print("Punchline:", punchline)  # Display the punchline
        else:  # If the command is neither "quit" nor "Alexa tell me a joke"
            print("Invalid command. Please type 'Alexa tell me a joke' or 'quit'.")  # Show error

# Load jokes from file and start the program
jokes = load_jokes("randomJokes.txt")  # Call function to load jokes from "randomJokes.txt"
tell_jokes(jokes)  # Start the joke interaction with the loaded jokes
