# # write all the data types in python with example below
# # Strings
# string_example = "Hello, World!"
# print("String Example:", string_example)
# # Integer
# integer_example = 42
# print("Integer Example:", integer_example)
# # Float
# float_example = 3.14159
# print("Float Example:", float_example)
# # Boolean
# boolean_example = True
# print("Boolean Example:", boolean_example)
# # List
# list_example = [1, 2, 3, "apple", "banana"]
# print("List Example:", list_example)
# # Tuple
# tuple_example = (1, 2, 3, "orange", "grape")
# print("Tuple Example:", tuple_example)
# # Dictionary
# dictionary_example = {"name": "Alice", "age": 30, "city": "New York"}
# print("Dictionary Example:", dictionary_example)
# # Set
# set_example = {1, 2, 3, 4, 5}
# print("Set Example:", set_example)
# # NoneType
# none_example = None
# print("NoneType Example:", none_example)
# # Complex Number
# complex_example = 2 + 3j
# print("Complex Number Example:", complex_example)
# # Bytes
# bytes_example = b"Hello"
# print("Bytes Example:", bytes_example)
# # Bytearray
# bytearray_example = bytearray(b"Hello")
# print("Bytearray Example:", bytearray_example)
# # Frozenset
# frozenset_example = frozenset([1, 2, 3, 4, 5])
# print("Frozenset Example:", frozenset_example)
# # Range
# range_example = range(1, 10)
# print("Range Example:", list(range_example))
# # Memoryview
# memoryview_example = memoryview(b"Hello")
# print("Memoryview Example:", memoryview_example.tolist())
# # Decimal
# from decimal import Decimal
# decimal_example = Decimal('10.5')
# print("Decimal Example:", decimal_example)
# # Fraction
# from fractions import Fraction
# fraction_example = Fraction(1, 3)
# print("Fraction Example:", fraction_example)


#  Get user input with input() function.
# - Check types withy type() function.
# - Convert Types in python
# - Create a simple calculator

# num_a = int(input("Enter First Number: "))
# num_b = int(input("Enter Second Number: "))

# total = num_a + num_b
# print(total)


# 📦Random Values
# num_x = "10"
# num_y = 20
# list_nums = ["10", 20]

# # 🔎Check Types
# print(type(num_y))
# print(type(num_x))
# print(type(list_nums))


# str() – Create an empty string "" or convert a value into a string

# int() – Create 0 or convert a value into an integer 

# float() – Create 0.0 or convert a value into a floating-point number

# bool() – Create False or convert a value into True/False

# list() – Create [] or convert an iterable into a list

# tuple() – Create () or convert an iterable into a tuple

# set() – Create empty set or convert an iterable into a set (unique elements)

# dict() – Create empty dict or convert a mapping/sequence of pairs into a dictionary




# # Practice 

# x = 10

# num_x = int(x)
# print(num_x)

# float_x = float(x)
# print(float_x)

# str_x = str(x)
# print(str_x)

# bool_x = bool(x)
# print(bool_x)

"----- Practice 2 -----"

# data conversion in python
# getting user input

# 🙋‍♂️Get User Input

user  =  str(input("Enter Your Name: "))
age   =  int(input("Enter Your Age: "))
height=  float(input("Enter Your Height: "))

# 🖨️Print User Data
print(f"User Name is {user} and i am {age} years  old and my height is {height} fts")

# typeOfData
print(type(user))
print(type(age))
print(type(height))