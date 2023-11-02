age = 30

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
elif age >= 65:
    print("The person is an elder.")
else:
    print("Invalid age.")

""" 
an if-elif-else chain is used to determine the person's stage of life based on their age.
If the person is less than 2 years old, the program prints a message that the person is a baby.
If the person is at least 2 years old but less than 4, the program prints a message that the person is
a toddler. If the person is at least 4 years old but less than 13, the program prints a message that
the person is a kid. If the person is at least 13 years old but less than 20, the program prints a 
message that the person is a teenager. If the person is at least 20 years old but less than 65,
the program prints a message that the person is an adult. If the person is age 65 or older, the program 
prints a message that the person is an elder. If the age is invalid, the program prints an appropriate 
message.

 """