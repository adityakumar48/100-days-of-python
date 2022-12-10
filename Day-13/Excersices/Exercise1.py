#  check odd or even python program

# 1. get input from user
# 2. check if input is even or odd
# 3. print result

# get input from user
num = int(input("Enter a number: "))
# check if input is even or odd
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
