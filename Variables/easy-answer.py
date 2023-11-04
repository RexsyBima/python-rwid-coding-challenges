#Challenge 1 : Variable Swap
# Variable Swap without using a third variable
a = 5
b = 10

# Swap the variables
a, b = b, a

print(f"a: {a}, b: {b}")  # Output should be "a: 10, b: 5"

#Challenge 2 : Type conversion
# Converts a space-separated string of numbers into a list of integers
numbers_string = "3 4 5 6 7"  # Example input
numbers_list = [int(num) for num in numbers_string.split()]

print(numbers_list)  # Output should be [3, 4, 5, 6, 7]

#Challenge 3 : Unit Conversion
# Convert kilometers to miles
kilometers = 10  # Example input
miles = kilometers * 0.621371

print(f"{kilometers} kilometers is equal to {miles} miles.")
#Challenge 4 : Simple Interest Calculator
# Simple interest formula is I = PRT / 100
P = 1000  # Principal amount
R = 5     # Rate of interest per year
T = 2     # Time in years

# Calculate simple interest
I = (P * R * T) / 100

print(f"The simple interest is: {I}")

#Challenge 5 : Age in Seconds
# Calculate age in seconds
age_in_years = 25  # Example age
age_in_seconds = age_in_years * 365 * 24 * 60 * 60

print(f"Your age in seconds is: {age_in_seconds}")
