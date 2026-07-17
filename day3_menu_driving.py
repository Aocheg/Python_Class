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
