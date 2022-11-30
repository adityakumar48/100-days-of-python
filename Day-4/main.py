import random
# import myModule

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)


love_score = random.randint(1, 100)
print(f"Your love score is  {love_score}")

# print(myModule.pi)

random_Number = random.randint(0, 3)
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[random_Number])
fruits.append("Peach")
print(fruits)
