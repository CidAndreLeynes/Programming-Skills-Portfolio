import random  # Import the random module to generate random numbers and operations

def displayMenu():
    # Display the difficulty level menu
    print("DIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")

def randomInt(difficulty_level):
    # Generate a random integer based on difficulty level
    if difficulty_level == 1:  # Easy level: single-digit numbers
        return random.randint(1, 9)
    elif difficulty_level == 2:  # Moderate level: double-digit numbers
        return random.randint(10, 99)
    elif difficulty_level == 3:  # Advanced level: 4-digit numbers
        return random.randint(1000, 9999)
    else:  # Invalid difficulty level should raise an error
        raise ValueError("Invalid difficulty level.")

def decideOperation():
    # Randomly decide whether to use addition or subtraction
    return random.choice(['+', '-'])

def displayProblem(number1, number2, operation):
    # Display the problem for the user to solve
    print(f"{number1} {operation} {number2} = ", end="")

def isCorrect(user_answer, correct_answer):
    # Check if the user's answer is correct
    if user_answer == correct_answer:  # If answer is correct
        print("Correct!")
        return True  # Return True to indicate a correct answer
    else:  # If answer is incorrect
        print("Incorrect.")
        return False  # Return False to indicate an incorrect answer

def calculateScore(attempt):
    # Calculate score based on the attempt number
    return 10 if attempt == 1 else 5  # 10 points for first attempt, 5 for second

def displayResults(score):
    # Display the user's final score and grade
    print(f"\nYour final score is: {score} out of 100")
    if score > 90:  # Score 91-100
        print("Grade: A+")
    elif score > 80:  # Score 81-90
        print("Grade: A")
    elif score > 70:  # Score 71-80
        print("Grade: B")
    elif score > 60:  # Score 61-70
        print("Grade: C")
    elif score > 50:  # Score 51-60
        print("Grade: D")
    else:  # Score 50 or below
        print("Grade: F")

def getDifficultyLevel():
    # Prompt the user to select a difficulty level and validate the input
    while True:
        try:
            choice = int(input("Choose a difficulty level (1, 2, or 3): "))
            if choice in [1, 2, 3]:  # Check if choice is valid
                return choice  # Return valid choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:  # Handle non-integer input
            print("Invalid input. Please enter a number.")

def generateQuestion(difficulty_level):
    # Generate a question based on the chosen difficulty level
    number1 = randomInt(difficulty_level)  # Generate first number
    number2 = randomInt(difficulty_level)  # Generate second number
    operation = decideOperation()  # Randomly choose an operation
    # Calculate the correct answer based on the chosen operation
    correct_answer = number1 + number2 if operation == '+' else number1 - number2
    return number1, number2, operation, correct_answer  # Return all components of the question

def playQuiz():
    # Play a 10-question quiz based on the selected difficulty level
    difficulty_level = getDifficultyLevel()  # Get user-selected difficulty
    score = 0  # Initialize score counter
    for _ in range(10):  # Loop to ask 10 questions
        # Generate a new question
        number1, number2, operation, correct_answer = generateQuestion(difficulty_level)
        attempts = 0  # Track the number of attempts for the current question
        while attempts < 2:  # Allow up to 2 attempts per question
            displayProblem(number1, number2, operation)  # Display the problem
            try:
                user_answer = int(input())  # Get user input as an integer
                if isCorrect(user_answer, correct_answer):  # Check answer
                    score += calculateScore(attempts + 1)  # Update score
                    break  # Exit loop if answer is correct
            except ValueError:  # Handle non-integer input
                print("Please enter a valid integer.")
            attempts += 1  # Increment attempt counter after each attempt
    displayResults(score)  # Display the final score and grade

def main():
    # Main program loop to allow replaying the quiz
    while True:
        displayMenu()  # Show the difficulty level menu
        playQuiz()  # Start the quiz
        # Ask if the user wants to play again
        play_again = input("Would you like to play again? (yes or no): ").strip().lower()
        if play_again != 'yes':  # Exit loop if user doesn't enter "yes"
            print("Thank you for playing!")  # Thank user for playing
            break  # Exit the game

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
