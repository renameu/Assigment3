print("1")
myset = set(map(int, input("Enter your set with spaces: ").split()))
print(myset)

'''
Output:

Enter your set with spaces4 3 5 6 4 8 6 8
{4, 3, 5, 6, 8}
'''




print("2")
mylist1 = {15, 21, 23, 43, 55, 66, 78, 89}
mylist2 = {1, 43, 66, 87, 54, 13, 32, 99}

print("Mylist1: ", mylist1)
print("Mylist2: ", mylist2)

print("Union of two sets is: ", mylist1.union(mylist2))
print("Intersection of two sets is: ", mylist1.intersection(mylist2))
print("Difference of two sets is: ", mylist1.difference(mylist2))
print("Symmetric difference of two sets is: ", mylist1.symmetric_difference(mylist2))

"""
Output:

Mylist1:  {66, 43, 78, 15, 21, 55, 23, 89}
Mylist2:  {32, 1, 66, 99, 43, 13, 54, 87}
Union of two sets is:  {32, 1, 66, 99, 43, 13, 78, 15, 21, 55, 23, 54, 89, 87}
Intersection of two sets is:  {66, 43}
Difference of two sets is:  {78, 15, 23, 21, 55, 89}
Symmetric difference of two sets is:  {32, 1, 99, 13, 78, 15, 23, 21, 54, 87, 55, 89}
"""



print("3")
mydict = dict()

mydict['key1'] = input("Enter a value for key1: ")
mydict['key2'] = input("Enter a value for key2: ")
mydict['key3'] = input("Enter a value for key3: ")

print("The dictionary is: ")
print(mydict.items())




print("4")

mydict = {"bird ": "parrot", "cat": "lion", "panda": "red panda", "beer ": "grey beer"}

user_input = input("Enter key to dict: ")

if user_input in mydict.keys():
    print("Yes, ", user_input, " in my dictionary")
else:
    print("No, ", user_input, " is not in my dictionary")

"""
Output:

Enter key to dict: dog
No,  dog  is not in my dictionary

Enter key to dict: bird
No,  bird  is not in my dictionary

"""



print("5")

userInput = input("Enter a string: ")
myDict = {}
for letter in userInput:
    myDict[letter] = myDict.get(letter, 0) + 1
print("Frequency:", myDict)


print("#6. Set Membership")
myset = set("Assingment")
print(myset)
user_input = input("Enter a char: ")
if user_input in myset:
    print("Yes it is in my set")
else:
    print("No is in my set")

"""
Output:
{'i', 'A', 'g', 'e', 's', 'n', 't', 'm'}
Enter a char: e
Yes it is in my set

{'i', 'A', 'g', 'e', 's', 'n', 't', 'm'}
Enter a char: r
No it is not in my set
"""


print("7")
mydict = {"bird ": "parrot", "cat": "lion", "panda": "red panda", "beer ": "grey beer"}
print("All values :")
print(mydict.values())
"""
Output:
All values :
dict_values(['parrot', 'lion', 'red panda', 'grey beer'])
"""




print("8")
mydict1 = {"bird ": "parrot", "cat": "lion", "panda": "red panda", "beer ": "grey beer"}
mydict2 = {"People": "Adam", "fly": "fly", "Home": "Dom"}

mydict1.update(mydict2)
print(mydict1)


print("9")
d_data1 = {'Artyom': 17,
           'Raim': 8,
           'Bayr': 12}
print("Given dictionary is: ", d_data1)
removal = input("Enter the key to be removed: ")
d_data1.pop(removal, None)  # remove entered element
print("After removal: ", d_data1)



print("10")
l_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Given list:", l_elements)
u_elements = set(l_elements)  # show repeated elements once
print("Unique Elements set: ", u_elements)


