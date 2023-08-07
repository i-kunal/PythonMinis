# Formatting strings

email = """
Hi John,

This is our first email to you.

Thank you,
Boss

"""

print(email)

email2 = "Hi John, \n\nThis is our first email to you. \n\nThank you,\n\nBoss"

print(email2)

sol = 'Some string chars'

print(sol[2])
# negative indices are allowed in python, it starts looking up from the last element
print(sol[-1])
print(sol[0:4])  # take the substring out from index 0 to index n-1
# if we leave the end index, it will take the value until the last character of that string
print(sol[0:])
# if we don't specify the start index, it will automatically take the 0 as the default value
print(sol[:9])
print(sol[:])  # if we don't specify the start and end index, it is going to take the default values 0 & n-1 where n is the length of string
print(len(sol))  # to get the length of the string.
print(sol[-5:-2])
print(sol[5:-5])


sol2 = "Brodah"
print(sol2.upper())  # .lower() to make all lower case
print(sol2)

sol2 = " jAKE   "
print(len(sol2))
sol2 = sol2.strip()
print(len(sol2))  # moves any whitespace from the beginning or the end:

sol2 = "Blake, Jake, Drake, Stake"
sol2 = sol2.split(',')  # string split method in python
print(sol2[0])


# Formatted strings
# All string methods return new values. They do not change the original string.
age = 16
address = 'unique'
txt = "YOLO age = {} address = '{}'"
print(txt.format(age, address))

price = 12.45789
display_price = "The price is {0:.2f}"
print(display_price.format(price))


example = f'The age is {age}. The address is {address}'
print(example)
