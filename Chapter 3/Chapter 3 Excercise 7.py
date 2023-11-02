locations = ['Tokyo', 'Paris', 'New York', 'Cairo', 'Bangkok']

# Print the original list
print(locations)

# Print the list in alphabetical order using sorted()
print(sorted(locations))

# Show that the original list hasn't changed
print(locations)

# Print the list in reverse alphabetical order using sorted()
print(sorted(locations, reverse=True))

# Show that the original list hasn't changed
print(locations)

# Use reverse() to change the order of the list and print it
locations.reverse()
print(locations)

# Use reverse() to change the order of the list and print it again
locations.reverse()
print(locations)

# Use sort() to store the list in alphabetical order and print it
locations.sort()
print(locations)

# Use sort() to store the list in reverse alphabetical order and print it
locations.sort(reverse=True)
print(locations)
