def describe_city(city):
    country = "Iceland"  # default country
    if city == "Reykjavik" or city == "New York City":
        country = "Iceland"
    else:
        country = "Other"
    print(f"{city} is in {country}.")

# Call the function for three different cities, at least one of which is not in the default country
print("Description of Reykjavik")
describe_city("Reykjavik")
print("Description of New York City")
describe_city("New York City")
print("Description of Paris")
describe_city("Paris")

"""  
The `describe_city()` function takes a single argument, the name of a city.
The function then uses the `country` variable to determine which country the city is in. The default 
value for `country` is "Iceland". The function then uses `if` statements to check if the city is equal 
to "Reykjavik" or "New York City". If it is, the country remains the default "Iceland". If it's not, the 
country is set to the appropriate value based if the city is "Other" (i.e., any other city besides 
"Reykjavik" or "New York City").Finally, the function prints a sentence that includes the city name, and 
the country it's in (which will be either "Iceland" or "Other").The function is called three times with 
different cities as input. The output for the first 2 calls will be "__ is in Iceland" because 
"Reykjavik" and "New York City" are used as inputs, and the default value for country is "Iceland". 
The output for the 3rd call will be "Paris is in Other" because it is the one city of the three that is 
not "Reykjavik" or "New York City".

"""