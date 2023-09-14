# Ask user for their name

name = input("What is your name? ").strip().title()

# Remove whitespace from string
# name = name.strip()
# Capitalize user's name
# name = name.title()
# Split user's name into first name and last name
# first, last = name.split(" ")


# Say hello to user

# concatenate
print("hello, " + name)

# args
print("hello,", name)

# end
print("hello,", end=" ")
print(name)

# sep
print("hello, ", name, sep="")

# fstring
print(f"hello, {name}")

# It works? YES :)
print("hello,", input("What is your name? "))
