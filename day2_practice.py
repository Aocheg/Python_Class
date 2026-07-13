# DAY 2 (LOOP) while loops
# concept 1: A while loop keeps running as long as condition is True. 
# Think of it like: "Keep doing this while this thin is stil true".

count = 0

while count < 5:
    print("Count is:", count)
    count = count + 1

# The Core mental model for every 'while' loop is that,
# it checks the condition before each run, and stopes the moment it's false.

# CONCEPT 2: for LOOPs
# A for loop is used when you know (or can genrate) exactly how many times to repeat something.
# The most common pattern use range():

for i in range(5):
    print("Number:", i)

# DAY 2 PROJECRT: WATER ROTATION & SAFETY CHECKER
    # What it does: Lets a health/aid worker check multiple households' water access in one session, 
    # without restarting the program each time — this is where loops actually become useful in a real tool.

# STEP 1: The Loop Skeleton

print("\nWATER ROTATION & SAFETY CHECKER")
print("--------------------------------")

WHO_MINIMUM_LITERS_PER_PERSON = 50

checking = True
critical_count = 0

while checking:
    hoursehold_name = input("\nHousehold name (or 'quit' to stop): ")
    if hoursehold_name.lower() == "quit":
        checking = False
    else:
       
# STEP 2: Adding the water math

       people = int(input("Number of people in household: "))
       liters_available = float(input("Liters of water available today: "))

       liters_per_person = liters_available / people
       needed = people * WHO_MINIMUM_LITERS_PER_PERSON

       print(f"--- {hoursehold_name} ---")
       print(f"Liters per person: {round(liters_per_person, 1)} L")

       if liters_available >= needed:
            print("Status: Sufficient water supply")
       elif liters_available >= needed * 0.5:
            print("Status: Below recommended - monitor closely")
       else:
            critical_count = critical_count + 1
            print("Status: CRITICAL shortage - needs urgent support")

print(f"Total number of Critical Households in this session: {critical_count}")
print("\nSession ended.")

# DAY 2 Challenge: Track Critical Households


