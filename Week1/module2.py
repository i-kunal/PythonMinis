print("Welcome Dr")
# to prompt input from the stdin
password = input("Please enter your password\n")
print(type(password))  # to get the type of the variable
print("Thank you...")
if password:
    print("You are now successfully logged in Dr" + password)
else:
    print('Sorry doc your authentication failed')

print('5' * 5)  # will print the string 5 times
