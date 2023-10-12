# Exercise 3.1.5[Lab Task]

# Write a python program to find the sum of odd and even numbers from a set of numbers
print("*** Sum of ODD/EVEN numbers ***\n")


def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum


input_numbers = input("Enter a set of numbers : ")

numbers = [int(x) for x in input_numbers.split()]

even_sum, odd_sum = sum_even_odd(numbers)

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

# Write a python program to find the smallest number from a set of numbers
print("\n***Find the smallest number***")


def find_smallest(numbers):
    if not numbers:
        return None

    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


input_numbers = input("Enter a set of numbers : ")

numbers = [int(x) for x in input_numbers.split()]

smallest_number = find_smallest(numbers)

if smallest_number is not None:
    print(f"Smallest number: {smallest_number}")
else:
    print("No numbers entered.")

# Write a python program to find the sum of all numbers between 50 and 100, which are divisible by 3 and not divisible by 5
print("\n***Sum of 50-100 which is divisible by 3 but not divisible by 5***")
sum = 0
for i in range(50, 101):
    if (i % 3 == 0 and i % 5 != 0):
        sum += i
print(f"Sum is: {sum} ")

# Write a python program to find the second-highest number from a set of numbers
print("\n***Find the second-highest number***")

numbers = input("Enter a set of numbers : ").split()
numbers = [int(num) for num in numbers]

if len(numbers) < 2:
    print("There are not enough numbers to find the second highest.")
else:
    second_highest = sorted(set(numbers), reverse=True)[1]
    print(f"The second highest number is: {second_highest}")

# Write a python program to find the factorial of a number using for loop
print("\n***Find the factorial of a number***")
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i;
print(f"The factorial of {num} is: {factorial}")

# Write a python program to generate Fibonacci series
print("\n***Generate Fibonacci Series***")
n = int(input("Enter the number: "))
a, b = 0, 1
print("Fibonacci series:")
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

# Exercise 4.2[Lab Task ]
# Write a python program to find the largest number between two numbers using function
print("\n***Find the largest number between two numbers using function***")


def maximum(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    elif x == y:
        return 0
    else:
        return 1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = maximum(num1, num2)

if result == num1:
    print(f"{num1} is largest number")
elif result == num2:
    print(f"{num2} is largest number")
elif result == 0:
    print(f"{num1} & {num2} both equal")
elif result == 1:
    print("Result invalid")
else:
    print("Enter valid number")

# Write a python program to find the sum of the numbers passed as parameters
print("***\nSum of the numbers passed as parameters***")


def sum(x):
    sum = 0
    for i in str(x):
        sum = sum + int(i)
        x = sum
    return x


number = int(input("Enter numbers: "))
result = sum(number)
print("Summation of numbers is:", result)
