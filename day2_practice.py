# DAY 2 (LOOP) while loops
# concept 1: A while loop keeps running as long as condition is True. Think of it like: "Keep doing this while this thin is stil true".

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
