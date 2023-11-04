#Challenge 1 : Multiplication Table
# Take input from the user
num = int(input("Enter a number to see its multiplication table: "))

# Print the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Challenge 2 : Formatted Receipt
items = {
    'Bread': 1.99,
    'Milk': 0.99,
    'Eggs': 2.99,
    'Butter': 3.49
}

# Calculate the total price
total_price = sum(items.values())

# Print the receipt
print("Item     Price")
print("----     -----")
for item, price in items.items():
    print(f"{item:<9}${price:>5.2f}")
print("----     -----")
print(f"Total    ${total_price:.2f}")

#Challenge 3 : Pyramid Patterns
# Get the height of the pyramid from the user
height = int(input("Enter the height of the pyramid: "))

# Print the pyramid pattern
for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))

#Challenge 4 : Box Border
# Get the height and width from the user
width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))

# Print the top border
print('*' * width)

# Print the sides
for _ in range(height - 2):
    print('*' + ' ' * (width - 2) + '*')

# Print the bottom border
print('*' * width)

#Challenge 5 : Email Extractor
# Given string with emails
emails = "user1@example.com user2@domain.com user3@test.org"

# Split the string into a list of emails
email_list = emails.split()

# Print each email on a separate line
for email in email_list:
    print(email)


