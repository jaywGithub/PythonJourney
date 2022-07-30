

print("Welcome to the Tip Calculator")
total = input("How much is the total bill? R")
tip = input("How much is your tip? 10, 12, or 15 percent: ")
people_count = input("How many people to split the bill? ")

tip_percentage = int(tip)

total_tip = float(total) * float(tip_percentage) / 100
total_bill = (float(total) + total_tip)
total_bill_split = "{:.2f}".format(total_bill / int(people_count))

print(f"Bill per person: R{total_bill_split}")