# For-Loop Basic Syntax
# So let's start with the basics. How do we create a loop?
#
# To create a loop we need to do the following:
#
# 🔹Use for keyword to initiate for-loop.
# 🔹Specify any variable name (used for each item)
# 🔹Point to a Container (list, tuple, dict, str…)
# 🔹Create Code-Block (Code for each iteration)
#
# Here is an example:
from itertools import count
from math import factorial

from urllib3 import proxy_from_url

from Data_Types.Collection_Data_Types import my_dict

# container = [1,2,3,4,5,6,7,8,]
#
# for i in container:
#     print(i)

# example 1

# # let print my name characters in a loop
# my_name = 'Rohail Rahmat'
#
# for char in my_name:
#      print(char.upper(),"="*3, char.upper(),)

# big_number = 123456789
#
# for str_num in str(big_number):   #we have converted the num in to string by str
#     num = int(str_num)           #then we store the str in num to make it a int
#     square = num ** 2
#     # cube = num ** 3
#     print(f"the number is :{num} ------------- its square is {square}")


# IN RANGE FUNCTION

# for i in range(10):    # now here the number will start from 0 to 9 and 10 excluding cuz
#     print(i)           # we staer from 0 and exclude the last one

# # same code
#
# for i in range(10):
#     print("rohail")

# we can also specify the Start and End number in the range():
#
# for i in range(10,20):
#     print(i)

# And you can even specify the step between start and end numbers.
# for i in range(10,100,2):       #here 10 is the starting point 100 is the ending and 2 is the step which we will go on like 2,4,6, etc
#     print(i)

# we will do an example of a todo items using list and  for loop
#
# todo_items = []         #we have set a list to store the appended items
#
# for i in range(1,10):
#     todo_list = f'TODO_ITEM - {i}'              #we have stored the items in the variable
#     todo_items.append(todo_list)                #now we have append the items in the list by append method
# print(todo_items)



# In case you want to iterate over values, then you'd need to use values() method on your dictionary to get a list of values.

# my_info = {
#     "name"  : "rohail",
#     "email" : "rohail@gmail.com",
#     "phone" : "23456789",
#     "age"   : "31"
# }
#
#
# for key,value in my_info.items():
#     print(f'Key: {key}, Value: {value}')


# ⛓️‍💥Break out of loops

# for example we have a list and we have to find the first even number in the list

# nums = [0, 99, 10, 20, 33, 80, 57, 6, 81,]
#
# for n in nums:
#     if n % 2 == 0 and n != 0:             # so we have set a condition that if you find a even number than print it and break the loop
#         print(f"the first even number is {n}")
#         break
# print("finished")



pak_rupee  = [10,20,50,100,500,1000,5000]
wallet = [20,50,1000,200,500,40]

total = 0
for rupee in wallet:
    if rupee not in pak_rupee:
        continue
    total += rupee

print(f'Total: {total} PKR')







# tasks = []
# for i in range(1, 11,2):
#     task_name = f"Task {i}"
#     tasks.append(task_name)
# print(tasks)
# Print numbers from 1 to 20.
# for i in range(1,21):
#     print(i)
# Print even numbers from 1 to 50.
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)
# Print odd numbers from 1 to 50.
# for i in range(1,51):
#     if i%2 == 1:
#         print(i)
# Print multiplication table of 5.
# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")
# Print all characters of a string.
# name = 'rohail'
# for ch in name:
#     print(ch.upper())
# Print sum of numbers from 1 to 10.
# total = 0
# for i in range(1, 11):
#     total = total + i
# print("Sum =", total)

# Print squares of numbers from 1 to 10.
# square = 0
# for i in range (1,11):
#     square = i**2
#     print(square)
# # Print numbers in reverse order (10 to 1).
# for i in range(10, 0, -1):
#     print(i)

# Count how many numbers are divisible by 3 between 1–100.
# count = 0
# for i in range(1,101):
#     if i%3 == 0:
#         count += 1
# print("count =",count)
# Print each element of a list.
# list_1 =['item-1','item-2','item-3','item-4']
#
# for item in list_1:
#     print(item)


# LEVEL_2

# Find factorial of a number using loop.
# num = int(input("Enter a number: "))
# facto = 1
# for i in range(1, num + 1):
#     facto *= i
#     print("factorial=",facto)

#
# Check if a number is prime using loop.
#
# Print Fibonacci series up to n terms.
#
# Find maximum number in a list using loop.
#
# Count vowels in a string.
#
# Print pattern:
#
# *
# **
# ***
# ****
#
#
# Sum only even numbers from a list.
#
# Reverse a number using loop.
#
# Check if string is palindrome.
#
# Menu-driven calculator using while.




