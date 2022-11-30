# Import the random module here

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# random_number = random.randint(0, len(names)-1)
person = random.choice(names)
# print(f"{names[random_number]} is going to buy the meal today!")
print(f"{person(names)} is going to buy the meal today!")
