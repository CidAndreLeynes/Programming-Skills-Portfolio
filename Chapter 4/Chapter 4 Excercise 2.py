alien_color = 'green'

if alien_color == 'green':
    print("Player earned 5 points by shooting the green alien!")
else:
    print("Player earned 10 points by shooting the alien!")

if alien_color == 'blue':
    print("Player earned -5 points by shooting the blue alien!")
else:
    print("Player earned 20 points by shooting the alien!")

#In the first if-else chain, if the alien's color is green, 5 points are awarded, and if it's not green,
#  10 points are awarded (assuming that the alien's color is not blue). The program is then repeated with
#  a different color and point value for the alien, to illustrate its flexibility.