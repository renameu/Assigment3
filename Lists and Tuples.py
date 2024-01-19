print("1")
fruits = []
for i in range(5):
    fruits.append(input("Enter a fruit: "))

print(fruits)
"""
Output:

Enter a fruit: apple
Enter a fruit: banana
Enter a fruit: orange
Enter a fruit: qiwi
Enter a fruit: watermelon
['apple', 'banana', 'orange', 'qiwi', 'watermelon']
"""


print("2")

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# not clear explanation of task
print(myList[2:7])

"""
Output:
[3, 4, 5, 6, 7]
"""



print("3")

print("Enter first number: ", end="")
num1 = int(input())
print("Enter second number: ", end="")
num2 = int(input())
print("Enter third number: ", end="")
num3 = int(input())

mytuple = (num1, num2, num3)
print(mytuple)

"""
Output:

Enter first number: 9
Enter second number: 3
Enter third number: 4
(9, 3, 4)
"""



print("4")

mylist = ["apple", "banana",  "orange", "cherry", "pear"]
fruit = input("What fruit would you like to append: ")

mylist.append(fruit)
mylist.pop(0)
mylist.sort()

print(mylist)

"""
Output:

What fruit would you like to append: lemon
['banana', 'cherry', 'lemon', 'orange', 'pear']
"""




print("5")


num = int(input("Enter number to check if it in list: "))
mylist = [3, 73, 86, 42, 52, 8, 7]
if num in mylist:
    print("Yes it is!")
else:
    print("No")

"""
Output:

Enter number to check if it in list: 3
Yes it is!

Enter number to check if it in list: 11
No
"""


print("6")


mylist = ["apple", "banana",  "orange", "pineapple", "pear"]
mylist.reverse()
print(mylist)
"""
Output:
['pear', 'pineapple', 'orange', 'banana', 'apple']
"""




print("7")


mytuple = ("apple", "orange", "banana", "lemon",)
fristvar, secondvar, thirdvar, fourthvar = mytuple
print(f"first tuple member: {fristvar}")
print(f"second tuple member: {secondvar}")
print(f"third tuple member: {thirdvar}")
print(f"fourth tuple member: {fourthvar}")

"""
Output:
first tuple member: apple
second tuple member: orange
third tuple member: banana
fourth tuple member: lemon
"""




print("8")
u_input = list(map(int, input("Enter the list of nums separated by space: ").split()))
print("Max: ", max(u_input))
print("Min: ", min(u_input))
"""
Outpu:

Enter the list of nums separated by space: 3 7 31 84 31 12 
Maximum number: 84
Minimum number: 3
"""


print("9")
list1 = list(map(int, input("Enter the list of nums separated by space: ").split()))
list2 = list(map(int, input("Enter the list of nums separated by space: ").split()))
list1 += list2
print("Concatenated list:", list1)
"""
Output:
Enter the list of nums separated by space: 4 6 7 8 9 0
Enter the list of nums separated by space: 4  5 3 2 1 34  5
Concatenated list: [4, 6, 7, 8, 9, 0, 4, 5, 3, 2, 1, 34, 5]
"""


print("10")
user_input = list(map(int, input("Enter the list of nums separated by space: ").split()))
user_tuple = tuple(user_input)
print("Converted to tuple:",  user_tuple)

"""
Output:
Enter the list of nums separated by space: 9 4 7 1 3
Converted to tuple: (9, 4, 7, 1, 3)
"""



