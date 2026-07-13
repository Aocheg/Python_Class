# DAY 1 PYTHON BASIC(HANDS ON)

print("Hello, WOrld!")

name = "Oche"
age = 30
height = 1.68
student = True

print(name)
print(age)
print(height)
print(student)


name = input("Enter your name: ")
print("Hello", name)

a = 6
b = 3

print(a + b)
print(a - b)
print(a / b)
print(a * b)

num1 = float(input("Enter a first number"))
num2 = float(input("Enter a second number"))

print("sum: ", num1 + num2)
print("Difference: ", num1 - num2)
print("Division: ", num1 / num2)
print("Product: ", num1 * num2)

name = input("Enter your name")
age = input("Enter your age")

print("My name is", name)
print("I am", age, "years old")

value1 = float(input("Enter your 1st value"))
value2 = float(input("Enter your 2nd value"))

print(value1 % value2)

name = input("Please enter your name: ")
food = input("Enter your favourite food: ")

print(name, "loves", food)

# # DAY 2 CONDITIONS AND LOGIC

age = 18

if age >= 18:
    print("You are an adult")


age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You are too young")


score = int(input("Enter your score: "))

if score >= 70:
    print("Grade: A")
elif score >= 50:
    print("Grade: B")
else:
    print("Grade: C")


# # Logical Operator

age = 20

has_id = True

if age >= 18 and has_id:
    print("Access granted")


# ## Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# # Simple Login

username = input("Enter username: ")
password = input("Enter passoword: ")

if username == "admin" and password == "308":
    print("Login successful")
else:
    print("Invalid credentials")

# #MY TASKS

# ## TASK 1
#     #Create a program that:
        #Prints:
            # "Positive"
            # "Negetive"
            # "Zero"

numbe = int(input("Enter a number"))

if numbe >= 1:
    print("Postive")
elif numbe <= -1:
    print("Negetive")
else:
    print("Zero")

# ## TASK 2

#     #Create a grading system:
    # 70+ = A
    # 60-69 = B
    # 50-59 = C
    # below 50 = Fail

grade = int(input("Enter your grade: "))

if grade >= 70:
    print("A")
elif grade >= 60:
    print("B")
elif grade >= 50:
    print("C")
else:
    print("Fail")


# ## TASK 3 (Challenge)
#     #Create a program that:
        # ask for age
    # if age < 13 = child
    # 13-19 = Teen
    # 20 = Adult

age = int(input("Enter your age: "))

if age >= 20:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")


# DAY 3 (Loops)

    # for Loop
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

# While Loop

count = 1

while count <= 5:
    print(count)
    count += 1

# Break(stop loop)

for i in range(10):
    if i == 5:
        break
    print(i)

# Continue(skip)

for i in range(5):
    if i == 2:
        continue
    print(i)