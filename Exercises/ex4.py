# Assign value to cars
cars = 100
# Assign value to space_in_a_car
space_in_a_car = 4.0
# Assign value to drivers
drivers = 30
# Assign value to passengers
passengers = 90
# Calculate cars not driven
cars_not_driven = cars - drivers
# Assign value of drivers to cars_driven
cars_driven = drivers
# Calculate carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# Calculate average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


# Print a string with a variable
print("There are",cars,"cars available.")
# Print a string with a variable
print("There are only",drivers,"drivers available.")
# Print a string with a variable
print("There will be",cars_not_driven,"empty cars today.")
# Print a string with a variable
print("We can transport ", carpool_capacity, " people today.")
# Print a string with a variable
print("We have ", passengers, " to carpool today.")
# Print a string with a variable
print("We need to put about ", average_passengers_per_car, " in each car.")
