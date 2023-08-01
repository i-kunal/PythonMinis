# 1st program
# python marks the end of the statement with newline token instead of ';'
# if the statment is too lengthy to fit in one physical line, you can use \ to join 2 phsycial line as one logical statemet

a = 4
b = 4
print(a)
print(
    b)

a = b + 3 + 9 + \
    9

# Above statement joins line 10 & 11 and python interprets it as single statement

d = (8 + 8 + 9 +
     9 + 10)
# Another example , but using paranthesis instead of \
print(a)
print(d)

if a > 50:
    print('a is greater than 5')
else:
    print('a is not greater 5')


"""
Mutliline
comment 
"""

'hello'  # Python will ignore string literal and treat it as a comment if that value is not assigned to a variable

print('multiline comment above')
