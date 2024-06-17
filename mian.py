

# name = input("Enter your full name: ")
# phone_number = input("Enter your number: ")

# result = len(name)
# result = name.find(" ")  # find the FIRST occurrence of a given character
# result = name.rfind(" ")  # find the LAST occurrence of a given character

# name = name.capitalize()  # capitalize the first letter

# name = name.upper()  # capitalize all the letters
# name = name.lower()

# result = name.isdigit()  # it returns true is only contains digit (number)

# result = name.isalpha()  #  it returns true is only contains alphabetical characters

# phone_number.replace("-", " ")  # you can replace any occurrence with one character with another


# print(help(str))

######

# validate user input
# 1. username in no more than 12 characters
# 2. unsername must not contain spaces
# 3. username must not contain digits

username = input("Enter a username")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
