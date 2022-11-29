# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

# Size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

# Pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3

# Extra Cheese
if extra_cheese == "Y":
    bill = bill + 1

print(f"Your final bill is: ${bill}.")
