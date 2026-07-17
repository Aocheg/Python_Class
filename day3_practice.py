# DAY 3 FUNCTIONS: 
    # A Function let you package a block of code, give it a name,
    #  and run it whenever you want from anywhere in your program.

# def greet(name):
#     print("Hello, " + name + "!")

# greet("Gabriel")
# greet("Adanu")

# COncept 2: return(getting a value back from a function)
    # return handles a value back to wherever the function was called,
    # so you can store it or use it in more calculations.

# def add(a, b):
#     return a + b

# result = add(4, 7)
# print(result)

# Exercise: Calculate bmi:

# def calculate_bmi(weight, height):
#     return weight / (height ** 2)

# my_bmi = calculate_bmi(68, 1.68)
# print(round(my_bmi, 1))

# Concept 3: File Handling (saving data permantly)

# with open("notes.txt", "w") as file:
#     file.write("Hello, file!")

# with open("notes.txt", "r") as file:
#     print(file.read())

# COncept 4: Append mode("a"):
    # Append add to the end of a file without deleting what's already there.

# with open("notes.txt", "a") as file:
#     file.write("\nAnother line added!")

# with open("notes.txt", "r") as file:
#     print(file.read())

# Note that: in running append ("a") if you have "w" which is write above the append,
# the first "w" above the append overwrite everythin, then append once wiping,
#  out anything previously append.


# DAY 3 PROJECT: STUDENT ATTENDANCE & REPORT LOGGER
    # This let a teacher log daily attendance for student,
    # permanetly saving records to a file and calculating eache
    # student's attendance rate from that saved history.

    # this could help identify students at risk of dropping out.

# FILENAME = "attendace.csv"

# def log_attendance(student_name, status):
#     """Append one attendance record to the file."""
#     with open(FILENAME, "a") as file:
#         file.write(f"{student_name},{status}\n")

# # STEP 2: CALCULATING ATTENDANCE RATE:

# def calculate_attendance_rate(student_name):
#     """Read the file and calculate % of days present for a student."""
#     total_days = 0 
#     present_days = 0

#     with open(FILENAME, "r") as file:
#         for line in file:
#             name, status = line.strip().split(",")
#             if name == student_name:
#                 total_days += 1
#                 if status == "present":
#                     present_days += 1
    
#     if total_days == 0:
#         return None
#     return (present_days / total_days) * 100

# log_attendance("Ada", "present")
# log_attendance("Musa", "absent")
# log_attendance("Ada", "present")
# log_attendance("jerri", "present")


# rate = calculate_attendance_rate("jerri")
# print(rate)


# DAY 3 THREE COMBINE PROJECT: MENUE-DRIVEN ATTENDANCE SYSTEM

# The goal: instead of Hardcoding (log_attendance("Ada", "present")) directly in the code, 
# a teacher should should be ale to run the program, pick an option from a menu, 
# and keep logging/cheking students repeatedly.

FILENAME = "attendance.csv"

def log_attendance(student_name, status):
    """Append one attendance record to the file."""
    with open(FILENAME, "a") as file:
        file.write(f"{student_name},{status}\n")

def calculate_attendance_rate(student_name):
    """Read the file and calculate % of days present for a student."""
    total_days = 0
    present_days = 0

    with open(FILENAME, "r") as file:
        for line in file:
            name, status = line.strip().split(",")
            if name == student_name:
                total_days += 1
                if status == "present":
                    present_days += 1

    if total_days == 0:
        return None
    return (present_days / total_days) * 100

running = True
while running:
    print("\n1. Log attendance")
    print("2. Check attendance rate")
    print("3. Quit")
    choice = input("choose an option: ")

    if choice == "1":
        name = input("student name: ")
        status = input("status (present/absent): ").lower()
        log_attendance(name, status)
        print(f"Logged: {name} - {status}")

    elif choice == "2":
        name = input("student name to ckeck: ")
        rate = calculate_attendance_rate(name)
        if rate is None:
            print("No records found for that student.")
        else:
            print(f"{name}'s attendance rate: {round(rate, 1)}%")

    elif choice == "3":
        running = False
    else:
        print("Invalid option, tyr again.")
print("Program closed.")
