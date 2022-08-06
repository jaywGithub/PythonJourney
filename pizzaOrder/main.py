print("Welcome to ABC Pizza Deliveries!\n")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25\n")

print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
print("Extra cheese for any pizza: +$1\n")

size = input("What size pizza do you want? S, M, L ")
add_pepperoni = input("Would you like pepperoni? Y or N ")
extra_cheese = input("Would you like extra cheese? Y or N ")

bill = 0

if size.upper() == "S":
    bill += 15
    if add_pepperoni.upper() == "Y":
        bill += 2

elif size.upper() == "M":
    bill += 20
    if add_pepperoni.upper() == "Y":
        bill += 3

elif size.upper() == "L":
    bill += 25
    if add_pepperoni.upper() == "Y":
        bill += 3

else:
    print("Invalid value. Please try again.")

if extra_cheese.upper() == "Y":
    bill += 1

print(f"Your total bill is: ${bill}.")