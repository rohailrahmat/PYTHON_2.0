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