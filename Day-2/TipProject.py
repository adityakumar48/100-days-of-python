print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
bill = float(bill)
percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")

percentage = int(percentage)

people = input("How many people to split the bill? ")

people = int(people)

tip = bill * (percentage / 100)
total = bill + tip
split = total / people

print(f"Each person should pay: ${split}")
