name = "Gabriel"
age = 25
height = 1.65
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))

# Getting information from the user

name = input("What is your name? ")
print("Hello, " + name)

# conversion

age = input("How old are you? ")
age = int(age)
next_year = age + 1
print("Next year you are ", next_year)

name = input("What is your name? ")
age = int(input("How old are you? "))
next_year = age + 1
print("Hello," + name,"next year you'll be",next_year )

# DAY ONE PROJECT1

print("\nPERSONAL CARBON FOOTPRINT ESTIMATOR")
print("-----------------------------------")
print("\nAnswer a few questions")

km_drive = float(input("How many km you drive today? "))
kwh_used = float(input("How many KWh of electricity you used today?"))
meals_with_meat = int(input("How many meals with meet did you eat today?"))

print("you drove:", km_drive, "km")
print("you used:", kwh_used, "kWh")
print("you ate",meals_with_meat, "meat meals")

car_emmission = km_drive * 0.192
electricity_emission = kwh_used * 0.475
meat_emission = meals_with_meat * 3.3

total = car_emmission + electricity_emission + meat_emission

print("\n----Your Daily FootPrint ----")
print("Driving:", round(car_emmission, 2), "kg CO2")
print("Electricity", round(electricity_emission, 2), "kg CO2")
print("Meals", round(meat_emission, 2), "Kg CO2")
print("TOTAL:", round(total, 2), "kg CO2")

if total > 20:
    print("\nThat's above the global daily average!!! - try walking or biking for short trips")
else:
    print("\nNice! You're below the global daily average.")



#  DAY 1 Exercise Project: BMI Health Checker
print("\nBMI HEALTH CHECKER")
print("---------------------")
print("\nFill your details Bellow")

weight = float(input("Enter your weight in kg "))
height = float(input("Enter your height in metres "))

height_in_meters = height ** 2

bmi = weight / height_in_meters

print("Your BMI:", round(bmi, 1))

if bmi >= 25:
    print("You are overweight, try to engage in more exercise to keep fit")
elif bmi >= 18.5:
    print("You have a normal Body Mass Index (BMI), keep it up!!")
else:
    print("You are Underweight, try to eat healthy to gain weight")




