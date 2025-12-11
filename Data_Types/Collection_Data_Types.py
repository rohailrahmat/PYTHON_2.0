# - Learn Collection Data-Types:
#     🔹List
#     🔹Tuple
#     🔹Set
#     🔹Dict
# - How to Get Items
# - Slicing
# - Methods
# - Common Functions

# 1️⃣ List (Mutable Ordered Collection)  - ⭐MOST USED

# 📜 Basic Syntax
#-------------------------
# empty_list = [] # or list()
# my_list    = ['Wall', 'Floor', 'Roof', 'Ceiling', 'Door','window']
# print(my_list)

# my_list2 = ["rohail","romail","raheel","wasim","hasnain"]
# print(my_list2)

# # 📥 Get Items by Index
# first_item = my_list2[0]
# print("First Item is:", first_item)

# secound_item = my_list2[2]
# print("Secound Item is:", secound_item)

# # 📤 Change Item by Index
# my_list2[3] = "rahmat"
# print("After Changing Item:", my_list2)
# # ➕ Add Item to List
# my_list2.append("sheryar")
# print("After Appending Item:", my_list2)

# new_list = ["a","b","c","d","e","f","g","h","i","j"]
# sliced_list_1 = new_list[2:]
# # ya index 2 pa jo c hai waha se agay sab ko include karay ga INCLUDING c  
# sliced_list_2 = new_list[:7]
# # ya index 0 se index 7 tak sab print karay ga lekin 7 ko include nahi karay ga   
# sliced_list_3 = new_list[2:5]
# # ya index 2 se index 5 tak print karay ga lekin 5 ko include nahi karay ga 


# print("Sliced List from C to J:",sliced_list_1)
# print("Sliced List from a to g:",sliced_list_2)
# print("Sliced List from C to e:",sliced_list_3)

# # ya ak trick hai apnay list ko reverse karna hai to ap negative indexing use kar saktay hain
# new_list_2 = [1,2,3,4,5,6,7,8,9,0]
# reversed_list = new_list_2[::-1]
# # print("Reversed List is:",reversed_list)


# # i want a list of birds sorted in alphabetical order
# list_of_birds = ["sparrow", "eagle", "parrot", "pigeon", "owl", "peacock", "penguin", "duck","seagul"]
# collection_of_new_birds = list_of_birds[::2]
# # yaha ::2 ka matlab hai k har dosray item ko include karna hai
# print(collection_of_new_birds)


# # ['sparrow', 'parrot', 'owl', 'penguin']
# print(collection_of_new_birds[2:4:2])
# # yaha 2:4:2 ka matlab hai k index 2 se index 4 tak jao lekin har dosray item ko include karo



# scling use-case examples

# my_data = ["catagories","height","weight","age","color","breed","name"]
# header = my_data[0]
# values = my_data[1:]

# print("Header is:",header)
# print("Values are:",values)
# # OUTPUT
# Header is: catagories
# Values are: ['height', 'weight', 'age', 'color', 'breed', 'name']

# now let learn more about the other list methods in python

# # list_methods = ["append", "insert", "extend", "remove", "pop", "clear", "index", "count", "sort", "reverse", "copy"]
# my_list2 = ["rohail","romail","raheel","wasim","hasnain"]
# print("Original List:", my_list2)

# # append() - adds an item to the end of the list
# my_list2.append("sheryar")
# print("After Append:", my_list2)

# # # insert() - adds an item at a specified index
# my_list2.insert(6,"ammar")
# print("After Insert at index 6:", my_list2)

# # # remove() - removes the first occurrence of a specified item
# my_list2.remove("wasim")
# print("After Remove 'wasim':", my_list2)

# # pop() - removes and returns an item at a specified index (default is the last item)
# removed_item = my_list2.pop(2)
# print(f"After Pop at index 2 (removed item: {removed_item}:", my_list2)

# # # sort() - sorts the list in ascending order
# my_list2.sort()
# print("After Sort:", my_list2)

# extended_list = ["ali","umer","hassan"]
# my_list2.extend(extended_list)
# # yaha pa extend method use kiya hai jismei hum nay aik aur list ko apni original list mei add kar diya hai.
# #  extended_list ki tamam items ko my_list2 mei add kar diya hai 
# print("After Extend:", my_list2)

# # copy method bhi hota hai list ka jismei hum aik list ko dusri list mei copy kar saktay hain
# copied_list = my_list2.copy()
# print("Copied List:", copied_list)

# # copy method is liye use hota hai kyu k agar hum direct aik list ko dusri list mei assign kar day to dono list aik hi memory location ko point karengi
# # aur agar hum aik list mei koi change kar day to dusri list mei bhi wo change reflect ho jayega
# # lekin agar hum copy method use karte hain to dono list alag alag memory location ko point karengi
# # aur agar hum aik list mei koi change kar day to dusri list mei wo change reflect nahi hoga 

# # is ka example kuch is tarah hoga
# my_list2.append("new_item_in_original")
# print("After Appending new item in original list:", my_list2)
# # print("Copied List after original list is changed:", copied_list)



# # replacing item through Index
# my_list2[-1] = "changed_item"
# print("After Replacing item at index 1:", my_list2)




# OUTPUT




# Original List: ['rohail', 'romail', 'raheel', 'wasim', 'hasnain']
# After Append: ['rohail', 'romail', 'raheel', 'wasim', 'hasnain', 'sheryar']
# After Insert at index 6: ['rohail', 'romail', 'raheel', 'wasim', 'hasnain', 'sheryar', 'ammar']
# After Remove 'wasim': ['rohail', 'romail', 'raheel',  'hasnain', 'sheryar', 'ammar']
# After Pop at index 2 (removed item: raheel: ['rohail', 'romail', 'hasnain', 'sheryar', 'ammar']
# After Sort: ['ammar', 'hasnain', 'romail', 'rohail', 'sheryar']
# After Extend: ['ammar', 'hasnain', 'romail', 'rohail', 'sheryar', 'ali', 'umer', 'hassan']    
# --------------------------------------------------

# # NESTED LISTS

# nested_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#     ]
# # print("Nested List:", nested_list)

# # Accessing items in nested list

# first_row = nested_list[0][0]
# print(first_row)

# secound_row = nested_list[1][2]
# print(secound_row)

# third_row = nested_list[2][0]
# print(third_row)



# # 2️⃣ Tuples (Immutable Ordered Collection) - ⭐LESS USED


# empty_tuple = () # or tuple()
# my_tuple    = ('Wall', 'Floor', 'Roof', 'Ceiling', 'Door','window')
# print("list_1:", my_tuple)

# my_tuple2 = ("rohail","romail","raheel","wasim","hasnain")
# print("list_2:", my_tuple2)
# # 📥 Get Items by Index

# first_item = my_tuple2[0]
# print("First Item is:", first_item)
# secound_item = my_tuple2[2]
# print("Secound Item is:", secound_item)
# # 📤 Change Item by Index - Not Possible in Tuple
# # my_tuple2[3] = "rahmat" # This will raise an error
# # print("After Changing Item:", my_tuple2)
# # ➕ Add Item to Tuple - Not Possible in Tuple
# # my_tuple2.append("sheryar") # This will raise an error
# # print("After Appending Item:", my_tuple2)
# new_tuple = ("a","b","c","d","e","f","g","h","i","j")
# sliced_tuple_1 = new_tuple[2:]
# # ya index 2 pa jo c hai waha se agay sab ko include karay ga INCLUDING c
# sliced_tuple_2 = new_tuple[:7]
# # ya index 0 se index 7 tak sab print karay ga lekin 7 ko include nahi karay ga
# sliced_tuple_3 = new_tuple[2:5]
# # ya index 2 se index 5 tak print karay ga lekin 5 ko include nahi karay ga
# print("Sliced Tuple from C to J:",sliced_tuple_1)
# print("Sliced Tuple from a to g:",sliced_tuple_2)
# print("Sliced Tuple from C to e:",sliced_tuple_3)
# # ya ak trick hai apnay tuple ko reverse karna hai to ap negative indexing use kar saktay hain
# new_tuple_2 = (1,2,3,4,5,6,7,8,9,0)
# reversed_tuple = new_tuple_2[::-1]  
# print("Reversed Tuple is:",reversed_tuple)
# # OUTPUT
# # list_1: ('Wall', 'Floor', 'Roof', 'Ceiling', 'Door', 'window')
# # list_2: ('rohail', 'romail', 'raheel', 'wasim', 'hasnain')
# # First Item is: rohail
# # Secound Item is: raheel
# # Sliced Tuple from C to J: ('c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# # Sliced Tuple from a to g: ('a', 'b', 'c', 'd', 'e', 'f', 'g')
# # Sliced Tuple from C to e: ('c', 'd', 'e')
# # Reversed Tuple is: (0, 9, 8, 7,
# #  6, 5, 4, 3, 2, 1)
# # NESTED TUPLES
# nested_tuple = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
#     )
# print("Nested Tuple:", nested_tuple)
# # Accessing items in nested tuple
# first_row = nested_tuple[0][0]
# print(first_row)
# secound_row = nested_tuple[1][2]
# print(secound_row)
# third_row = nested_tuple[2][0]
# print(third_row)
# # OUTPUT
# # Nested Tuple: ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# # 1
# # 6
# # 7

# build in funtions for collections
# data = (1, 2, 3, 4, 5)
# print("Length of data:", len(data))          # Output: 5
# print("Max value in data:", max(data))       # Output: 5 
# print("Min value in data:", min(data))       # Output: 1
# print("Sum of data:", sum(data))             # Output: 15
# print("Sorted data:", sorted(data))         # Output: [1, 2, 3, 4, 5]
# print("Type of data:", type(data))         # Output: <class 'tuple'>
# print(data.count(3))               # Output: 1
# print(data.index(4))               # Output: 3

# # 3️⃣ Set (Mutable Unordered Collection of Unique Items) - ⭐LESS USED

# empty_set = set() # Note: {} creates an empty dictionary, not a set
# my_set    = {'Wall', 'Floor', 'Roof', 'Ceiling', 'Door','window'}
# print("Set 1:", my_set)


# # set ko hum hamisha {} ma use kartay hai 
# # example  set_1 = {1,3,4,5,6,7,8,5,3,2}
# # empty_set_2 = set()
# #  ya ak empty_set_2 ko show karany ka tariqa hai 
# # set hamisha chiz ko non repeated or Unorder form ma show karta hai
# my_set_2 = {"rohail","romail","wasim","ashoo","raheeel","rehan","sheryar",}
# print("this is my set:", my_set_2)
# print("sorted Set", sorted(my_set_2))


# # convert a list into a set
# list_1 = [1,2,4,5,6,7,8,9,6,4,"rohail","raheel","romail","rehan"]

# set_data = set(list_1)
# unique_data = set_data
# print(list_1)
# print(set_data)
# print(unique_data)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print("Union:", a | b)               # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# print("Intersection:", a & b)        # Output: {4, 5}
# print("Difference:", a - b)          # Output: {1, 2, 3}
# print("Symmetric Difference:", a ^ b)  # Output: {1, 2, 3, 6, 7, 8}
# # OUTPUT
# # Union: {1, 2, 3, 4, 5, 6, 7, 8}
# # Intersection: {4, 5}
# # Difference: {1, 2, 3}
# # Symmetric Difference: {1, 2, 3, 6, 7, 8}




# # 4️⃣ Dict (Mutable Unordered Collection of Key-Value Pairs) - ⭐MOST USED


# empty_dict = {} # or dict()
# my_dict = {
#     'name': 'rohail',
#     'age': 25,
#     'city': 'Karachi',
#     'profession': 'Developer',
#     'skills': ['Python', 'JavaScript', 'SQL'],
#     'is_employed': False,
#     'address': '123 Main Danyore',
# }

# print("Original Dictionary:", my_dict)
# print('Name:',my_dict['name'])
# print('age:',my_dict['age'])
# print('profession:',my_dict['profession'])
# # 

my_dict = {
    "int" : "a whole number like 1,2 or 3",
    "float" : "a decimal number like 1.5, 2.5 or 3.5",
    "str" : "a sequence of characters like 'hello' or 'python'",
    "bool" : "a data type that can be either True or False",
    "list" : "a collection of items that can be changed, like [1, 2, 3]",
    "tuple" : "a collection of items that cannot be changed, like (1, 2, 3)",
    "set" : "a collection of unique items, like {1, 2, 3}",
    "dict" : "a collection of key-value pairs, like {'name': 'Alice', 'age': 25}",


}
# # yaha pa hum nay aik dictionary banai hai jismei hum nay data types ke naam ko key banaya hai aur unki definition ko value banaya hai
# # phir hum nay for loop use kar kay dictionary ke tamam items ko print karwaya hai
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

# # OUTPUT
# # int: a whole number like 1,2 or 3
# # float: a decimal number like 1.5, 2.5 or 3.5
# # str: a sequence of characters like 'hello' or 'python'
# # bool: a data type that can be either True or False
# # list: a collection of items that can be changed, like [1, 2, 3]
# # tuple: a collection of items that cannot be changed, like (1, 2, 3)
# # set: a collection of unique items, like {1, 2, 3}
# # dict: a collection of key-value pairs, like {'name': 'Alice', 'age': 25}
# # # accessing items in dictionary
# print("string:", my_dict['str'])

# print(len(my_dict))  # Output: 8
# print(list(my_dict.keys()))  # Output: ['int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict']
# print(list(my_dict.values()))  # Output: ['a whole number like 1,2]
# print(list(my_dict.items()))  # Output: a data type that can be either True or False



