# Lab Exercise
# Task 1: Find the sum of odd and even numbers from a set of numbers.

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

# Task 2: Check if a triangle is valid or not

print("\n*** Triangle is valid or not ***\n")


def is_valid_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


a = float(input('Enter the length of side a: '))
b = float(input('Enter the length of side b: '))
c = float(input('Enter the length of side c: '))

if is_valid_triangle(a, b, c):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')
