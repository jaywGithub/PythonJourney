# Rollercoaster

print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Odd or even

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# BMI check

height = float(input("enter you height in m: "))
weight = float(input("enter you height in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI IS {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI IS {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI IS {bmi}, you are obese.")
else:
    print(f"Your BMI IS {bmi}, you are clinically obese.")

# To leap or not to leap

year = int(input("Which year would you like to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
