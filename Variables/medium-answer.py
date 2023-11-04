#Challenges 1 : FizzBuzz with a Twist
# Only two variables used
i, output = 1, ""
while i <= 100:  # Adjust range as needed
    output += "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i)
    print(output)
    i += 1
    output = ""  # Reset output for next iteration



#Challenges 2 : String Reversal
def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

input_string = "Hello, World!"
print(reverse_string(input_string))



#Challenges 3 : Prime Number Checker
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 29  # Change this value to test other numbers
print(f"{number} is a prime number: {is_prime(number)}")



#Challenges 4 : Fibonacci Sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Variable n will be the number of Fibonacci numbers to generate
n = 10
print(list(fibonacci(n)))



#Challenges 5 : Sorting Algorithm (Bubble Sort Example)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap

array_to_sort = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array_to_sort)
print("Sorted array is:", array_to_sort)


