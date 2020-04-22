# Python CC -  Variables and Simple Data Types

message = "Hello :)"
print(message)

message = "Hello Python CC World :O"
print(message)

# print(mesage) - typical typo error

# --------------------------------------------------------Strings and Methods-ish-----------------------------------------------------------


name = "richard peterson"
print(name.title())  # makes the string title case
print(name.upper())  # makes the string upper case
print(name.lower())  # makes the string lowe case

print("here is the name uppercase" + " " + name.upper() + " " + "and here is the name lowercase " + name.lower() + " using concatenation :)")


# ---------------------white space adding with tabs or newlines---------------------

print("\tLanguages:\nPython\nJavaScript\nC#\nHTML\nCSS")

# ---------------------removing white space using strip-----------------------------

language = " Python "
no_white_space_on_right = language.rstrip()

print(no_white_space_on_right) # however this removes only right (left would be with an "l" infront)

print(no_white_space_on_right.strip()) # removes both left and right (not in between)