# Variable and String
print("Hello World")  # print using the print function

# print from a variable
msg = 'Hello World'
print(msg)

# concatenate strings
first_msg = 'Hello Zahid,'
second_msg = 'Welcome to Reality'
combine_msg = first_msg + ' ' + second_msg
print(combine_msg)

# 3.3.5 exercise [Lab Task]
# 1st question
''' Write a Python program which accepts the user’s first and last name and print them in a single line as
full name.'''

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")
full_name = first_name + ' ' + second_name
print('Hello , ' + full_name)

# 2nd question
'''Write a Python program that accepts an integer (n) and computes the value of n + nn + nnn.'''

n = int(input("Enter an integer number: "))
result = n + n * n + n * n * n
print('Result:', result)

# 3rd question
'''Write a Python program which accepts the radius of a circle from the user and compute the area.'''

r = float(input("Enter the value of the radius: "))
pi = 3.1416
area = pi * (r * r)
print("The area of the circle is:", area)

# 4th question
'''Write a Python program to find whether a given number (accept from the user)'''

num = int(input("Enter a random number: "))
if num % 2 == 0:
    print(num, "is an EVEN number")
else:
    print(num, "is an ODD number")

# 3.4.25 [Lab Task]
# 1st question
'''Write a Python program which accepts a sequence of comma-separated numbers from user and generate
a list with those numbers.'''

best_xi = input("Best 11 of Ban XI in CWC-2023: ")
x = best_xi.split(",")  # Split the string into a list using a comma as the delimiter
print(x)

# 2nd question
'''Write a Python program to display the first and last colors from the following list. Go to the editor
colorList == ["Red","Green","White" ,"Black"]'''

colorList = ["Red", "Green", "White", "Black"]
print(colorList[0])  # Print the first element of the list
print(colorList[-1])  # Print the last element of the list

# Exercise 3.5.7 [Lab Task]
# Write a Python program to find the largest among three numbers.
print("***Enter three numbers to find the largest among them***")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number among three.")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number among three.")
else:
    print(num3, "is the largest number among three.")

# Write a Python program to display student grades.
# grade sheet of GUB:
# 80-100 = A+
# 75-79 = A
# 70-74 = A-
# 65-69 = B+
# 60-64 = B
# 55-59 = B-
# 50-54 = C+
# 45-49 = C
# 40-44 = D
# 0-39 = F

print("\n\n***Enter marks to display grades***")
while True:
    mark = int(input("Enter your mark (0-100): "))
    if 0 <= mark <= 100:
        if mark >= 80:
            print("You got A+ in this subject")
        elif mark >= 75:
            print("You got A in this subject")
        elif mark >= 70:
            print("You got A- in this subject")
        elif mark >= 65:
            print("You got B+ in this subject")
        elif mark >= 60:
            print("You got B in this subject")
        elif mark >= 55:
            print("You got B- in this subject")
        elif mark >= 50:
            print("You got C+ in this subject")
        elif mark >= 45:
            print("You got C in this subject")
        elif mark >= 40:
            print("You got D in this subject")
        else:
            print("You got F in this subject")
        break
    else:
        print("Enter a valid mark")

# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times their sum.
# Check if the sum is even or odd and print an appropriate message to the user.
print("\n\n***Sum of 3 numbers and check if they are equal and if the sum is even or odd***")
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
c = float(input("Enter the 3rd number: "))

# Calculate the sum of three numbers
sum = a + b + c
print(f"The sum of three numbers is: {sum}")

# Check if the numbers are equal and calculate three times their sum if they are
if a == b == c:
    multiply = 3 * (a + b + c)
    print(f"The numbers are equal. Three times their sum is: {multiply}")

# Check if the sum is even or odd
if sum % 2 == 0:
    print("The sum is an even number")
else:
    print("The sum is an odd number")
