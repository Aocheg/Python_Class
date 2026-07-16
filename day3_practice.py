# DAY 3 FUNCTIONS: 
    # A Function let you package a block of code, give it a name,
    #  and run it whenever you want from anywhere in your program.

def greet(name):
    print("Hello, " + name + "!")

greet("Gabriel")
greet("Adanu")

# COncept 2: return(getting a value back from a function)
    # return handles a value back to wherever the function was called,
    # so you can store it or use it in more calculations.

def add(a, b):
    return a + b

result = add(4, 7)
print(result)

# Exercise: Calculate bmi:

def calculate_bmi(weight, height):
    return weight / (height ** 2)

my_bmi = calculate_bmi(68, 1.68)
print(round(my_bmi, 1))

# Concept 3: File Handling (saving data permantly)

# with open("notes.txt", "w") as file:
#     file.write("Hello, file!")

# with open("notes.txt", "r") as file:
#     print(file.read())

# COncept 4: Append mode("a"):
    # Append add to the end of a file without deleting what's already there.

with open("notes.txt", "a") as file:
    file.write("\nAnother line added!")

with open("notes.txt", "r") as file:
    print(file.read())

# Note that: in running append ("a") if you have "w" which is write above the append,
# the first "w" above the append overwrite everythin, then append once wiping,
#  out anything previously append.


# DAY 3 PROJECT: STUDENT ATTENDANCE & REPORT LOGGER
    # This let a teacher log daily attendance for student,
    # permanetly saving records to a file and calculating eache
    # student's attendance rate from that saved history.

    # this could help identify students at risk of dropping out.
    