#Challenges 1 : Type printer
user_input = input("Enter anything: ")
print(f"The type of the input is {type(user_input)}")



#Challenges 2 : Int to float conversion
integer_value = int(input("Enter an integer: "))
print(f"Before conversion: {integer_value} is of type {type(integer_value)}")

float_value = float(integer_value)
print(f"After conversion: {float_value} is of type {type(float_value)}")




#Challenges 3 : String to list
input_string = input("Enter a comma-separated list of numbers: ")
list_of_integers = [int(i) for i in input_string.split(",")]
print(list_of_integers)



#Challenges 4 : Boolean casting
user_input = input("Enter a value: ")
boolean_value = bool(user_input)
print(f"Original: {user_input} (type: {type(user_input)})")
print(f"Converted to boolean: {boolean_value} (type: {type(boolean_value)})")




#Challenges 5 : sum of strings
str1 = input("Enter the first number: ")
str2 = input("Enter the second number: ")

# Assuming the user inputs valid numbers as strings
sum_of_numbers = int(str1) + int(str2)

print(f"The sum is: {str(sum_of_numbers)}")
 