# Arithmetic division

# Python does a true divsion by default

a = 1/2
print(f'value of {a}')
print(type(a))


# LIST
# LIST ARE ORDERED SEQUENCE THAT CAN store  A VARIETY OF Object types
# Syntax [] and  ',' to separate objects
# LIST support indexing and slicing and can even be nested

my_list = [1, 2, 3]

second_list = ['ab', 1, 'kj']

print(len(my_list))  # to retrieve the lenght of string
print(my_list[2])
print(second_list[1:])  # slicing and indexing works just like string with list

another_list = [2, 'kj', 4]

result_list = second_list + another_list
print(result_list)

# the difference between list and string is that LIST is mutable while string is not
result_list[0] = 'ba'
print(result_list)

result_list.append('adding at the end of the list')
print(result_list)

item_popped = result_list.pop()
print(result_list)  # remove last element from the list
print(item_popped)
print(result_list.pop(0))

alpha_list = [5, 7, 3, 62]
alpha_list.sort()  # sort the list in ascending order , this method mutates the orignal list
print(alpha_list)

# In python, there is a None type as well, which basically means function or method hasn't returned anything or that object has no value assigned
log = None

print(log)
print(type(log))

alpha_list.append('a')
alpha_list.pop()
print(alpha_list)
# alpha_list.sort() this will throw an error as it cannot compare objects of different type
print(alpha_list)

# To insert a list item at a specified index, use the insert() method.

alpha_list.reverse()  # to reverse the order of the list
alpha_list.sort(reverse=True)  # to sort the list desccending wise
print(alpha_list)


alpha_list1 = alpha_list  # alpha_list1 will simply point to what alpha_list is pointing in memory. Any modification on alpha_list will be cascaded to alpha_list2
alpha_list1[0] = 63
print(alpha_list)
# create new list from existing list

alpha_list1 = alpha_list.copy()
alpha_list1[0] = 62
print(alpha_list)
print(alpha_list1)


alpha_list1 = alpha_list + list((6,))
bol = list()  # Another way to create empty list, using constructor
bol.append(1)
print(bol)

print(alpha_list1)
