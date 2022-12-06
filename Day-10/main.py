# Function with Output

def format_name(f_name, l_name):
    """"" This function takes in the first and last name and formats it to return the title case version of the name. """""

    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    f_name = f_name.title()
    l_name = l_name.title()
    return (f"{f_name} {l_name}")


f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
print(format_name(f_name, l_name))
