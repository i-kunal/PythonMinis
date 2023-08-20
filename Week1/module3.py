"""
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions

numberValue = 10
stringValue = '10'
booleanValue = True  # False
floatValue = 10.01
floatEValue = 12e5

if numberValue == int(stringValue):  # here we are typecasting string into integer
    print(booleanValue)

print(type(floatValue))

# Assigning multiple values to multiple variables at the same time

x = y = z = 100
to = 3
bo = '3'
# In python int cannot be concated with string as it is in JAVA.
print("The value of x is "+str(x)+"\n The value of y is " +
      str(y)+"\n The value of z is "+str(z))

# Another way to print
print('The value of x is ', x, 'The value of y is ', y, 'The value of z is ', z)
print(floatEValue)

# complex numbers
comp = 8j
print(comp)

# casting between numbers
print(type(numberValue), numberValue)
# implicit casting  to convert a smaller data type to a higher data type to prevent data loss.
numberValue = floatEValue
print(type(numberValue), numberValue)
numberValue = float(numberValue)
print(type(numberValue), numberValue)
numberValue = numberValue + 0.4
print(numberValue)
# explicit casting to type cast a bigger  data type to a smaller data type
numberValue = int(numberValue)
print(numberValue)

# jolo = int(comp) -- cannot type cast complex numbers into any other numeric type

jolo = str(comp)
print(jolo)

# yet to discuss the random module
