# LOGICAL OPERATOS
# AND operator--------------
# True AND True   → True
# True AND False  → False
# False AND True  → False
# False AND False → False
from operator import truediv

# OR operator ----------------
# True OR True    → True
# True OR False   → True
# False OR True   → True
# False OR False  → False
# NOT operator ----------------
# not True  → False
# not False → True


# lets practice
# LEVEL 1 — BASICS (Build Confidence)
# Check if a number is positive AND even.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# # Check if a number is negative OR zero.
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Negative")
# elif num == 0:
#     print("Zero")
# else:
#     print("Positive")
# Print "Adult" if age is 18 or above, otherwise "Minor"
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an Adult.")
# elif age < 18:
#     print("You are a minor.")

# Check if a number is between 1 and 100 (inclusive).
# num = int(input("Enter a number: "))
# if num <= 100 and num >= 0:
#     print("inclusive in between 1 to 100")
# else:
#     print("not inclusive")
#
# Print "Valid password" if length is ≥ 6.
# password = input("Enter your password: ")
# if len(password) >= 6:
#     print("Your password is valid")
# else:
#     print("Your password is must be at least 6 characters.")
#
# Check if a character is a vowel (a e i o u).
# ch = str(input("Enter a value: "))
# if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#     print(f"{ch} is a vovel")
# else:
#     print(f"{ch} is not a vovel")
# Print "Weekend" if day is "Saturday" OR "Sunday"
# day = str(input("Enter a day: "))
# if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
#     print("it's not a weekend")
# elif day == "saturday" or day == "sunday":
#     print("it's a weekend")
# else:
#     print("it's not a day")
# Check if a number is NOT divisible by 3.
# num = int(input("Enter number: "))
# if not (num % 3 == 0):
#     print("Not divisible by 3")
# else:
#     print("Divisible by 3")

# Check if temperature is NOT below 0.
# temp = float(input("Enter temperature: "))
# if temp > 0:
#     print(f"Temperature is above 0% the Temperature id {temp}.")
# else:
#     print("Temperature is below 0%")
# #
# Print "Eligible" if height is ≥ 5.4 ft.

# eligible_height = float(input("Enter your height: "))
#
# if eligible_height >= 5.4 and eligible_height <= 6.0:
#     print("You are eligible")
# elif eligible_height >= 6.0:
#     print("You are above your height")
# else:
#     print("Your height must be between 5.4 and 6.0")

# lets try somthing harder in operators
#
# Check if a number is divisible by 3 AND 5.
# num = int(input("Enter number: "))
# if not (num % 3 == 0) and not (num % 5 == 0):
#     print("Not divisible by 3 & 5")
# else:
#     print("Divisible by 3 and 5")
# Check if a student passes if marks ≥ 50 AND attendance ≥ 75%.
#
# std_marks = int(input("enter you marks: "))
# std_attendance = int(input("your attendance in class: "))
#
# marks_ok = std_marks >= 50
# attendance_ok = std_attendance >= 75
#
# if marks_ok and attendance_ok:
#     print(
#         f"CONGRATULATIONS YOU HAVE PASSED THE EXAM "
#     )
# else:
#     print("SORRY, TRY AGAIN.")
#     if not marks_ok :
#         print("you don't have enough marks")
#     if not attendance_ok :
#         print("you don't have enough attendance")


# Print "Allowed" if user is 18+ OR has permission.

# AGE = int(input("Enter your age: "))
# if AGE >= 18:
#     print("Yes YOUR ARE ALLOWED")
# else:
#     print("NO YOU ARE NOT ALLOWED")
#
# Check if a year is leap year using logical operators.
# year = int(input("Enter a year: "))
#
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0) or (year % 100 == 0)):
#     print(year, " is a leap year.")
# else:
#     print(year, " is not a leap year.")

#
# Check if a username is not empty AND not "admin".
# username = 'rohail'
# is_admin = True
#
# if username == True or is_admin == True:
#     print(f"Hello sir you are and admin.")
# else:
#     print(f"Hello {username}! you are not admin.")
#     if username == None:
#         print(f"Username is not provided.")
#     if is_admin == False:
#         print(f"is_admin is not true")

# Print "Discount" if price ≥ 5000 OR user is "premium".

# product_price =  int(input("Enter the product price: "))
# user_is_Premium = True
# if product_price >= 5000 and user_is_Premium == True:
#     print("You have Discount on this product")
# else:
#     print("You have not Discount on this product please try again later")

# Check if number is outside range 10–50.
# num = int(input("Enter a number: "))
# if num >= 10 and num <= 50:
#     print(f"{num} is in the range of 10 to 50")
# else:
#     print(f"{num} is not in the range of 10 to 50")
#
# Check if a triangle is valid:
# side_1 = int(input("Enter side 1: "))
# side_2 = int(input("Enter side 2: "))
# side_3 = int(input("Enter side 3: "))
#
# a = side_1
# b = side_2
# c = side_3
#
# if a + b > c and a + c > b and b + c > a:
#     print("the Trinanlge is valid")
# else:
#     print("the Trinanlge is invalid")

# a + b > c AND a + c > b AND b + c > a
#
#
# Check if login is valid:
# username = str(input("Enter your username: "))
# password = int(input("Enter password: "))
#
# if username == "user" and password == 1234:
#     print(f"Logged in as {username}")
# else:
#     print(f"you credentials are not correct")


#
# Check if person is eligible for driving license:
# age = int(input("Enter your age: "))
# vision = str(input("Enter your vision: "))
#
# if age >= 18 and vision == "clear":
#     print("You are eligible for driving license")
# else:
#     print("you are not eligible for driving")
#     if age < 18:
#         print("You are young for a driving lincence")



# let say we are recuirting solider for pak army and we have to decide wether the person is fit for it or not
# so the height should be aleast 5.4ft , ages should be 18 to 25 , and qualification should be fsc with 60% marks
#
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# user_height = float(input("Enter your height (in feet): "))
# user_qualification = input("What is your qualification: ").lower()
# user_marks = float(input("Enter your marks percentage: "))
#
# # Logical checks
# age_ok = user_age >= 18
# height_ok = user_height >= 5.4
# qualification_ok = user_qualification == "fsc"
# marks_ok = user_marks >= 60
#
# if age_ok and height_ok and qualification_ok and marks_ok:
#     print(
#         f"\nTHANK YOU {user_name} for the information.\n"
#         f"You have completed {user_qualification.upper()} with {user_marks}% marks.\n"
#         f"Your height is {user_height} ft.\n"
#         f"🎉 Congratulations! You are eligible for the test."
#     )
# else:
#     print(f"\nSORRY {user_name}, you are NOT eligible for the test.\n")
#
#     if not age_ok:
#         print("- Age must be at least 18 years")
#     if not height_ok:
#         print("- Height must be at least 5.4 ft")
#     if not qualification_ok:
#         print("- Qualification must be FSC")
#     if not marks_ok:
#         print("- Marks must be at least 60%")
#
#

# LEVEL 4 — THINKING CHALLENGE (MASTER LEVEL)
#
# Check if a number is prime using logical conditions.
# num = int(input("Enter a number: "))
#
# if num <= 1:
#     print("Not Prime")
# else:
#     is_prime = True
#
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not Prime")
# Validate password:
# ≥ 8 chars
# contains digit
# contains uppercase

# password = input("Enter password: ")
#
# has_digit = True
# has_upper = True
#
# if len(password) >= 8:
#     for char in password:
#         if char.isdigit():
#             has_digit = True
#         if char.isupper():
#             has_upper = True
#     if has_digit and has_upper:
#         print("Your Password is valid")
#     else:
#         print("Password must contain at least one digit and one uppercase letter")
#
# else:
#     print("Password must be at least 8 characters long")

# Voting system:
# citizen AND age ≥ 18 AND NOT banned

# citizen = int(input("Enter the your age please: "))
#
# age_ok  = citizen >= 18
# banned  = citizen < 18
#
# if age_ok and not banned:
#     print("You can vote!!")
# else:
#     print("Sorry, you can't vote!")
#     if banned:
#         print("you are underage !")



# E-commerce checkout:
# items > 0
# address added
# payment method selected

# print("="*50)
# items = int(input("Enter number of items you want to buy: "))
#
# address = []
# payment_method = ["easypaisa","jazzcash","banktransfer"]
# stock_available = items > 0
# # checking for the items in store
# if items > 0:
#     print("stock available")
# else:
#     print("stock unavailable")
#
# if stock_available == True:
#         print(f"stock available how will you pay \n"
#               f"1. easypaisa \n"
#               f"2. jazzcash \n"
#               f"3. banktransfer \n"
#               )
# print("="*50)
#
# pay_method = int(input("Enter your selection 1,2 and 3: "))
# if pay_method == 1:
#     print(f"payment method is {payment_method[0]}")
#     num = int(input(f"please Enter your number: "))
# elif pay_method == 2:
#     print(f"payment method is {payment_method[1]}")
#     num = int(input(f"please Enter your number: "))
#
# elif pay_method == 3:
#     print(f"payment method is {payment_method[2]}")
#     num = int(input(f"please Enter your number: "))
#
# else:
#     print(f"payment method is invalid")
# print("="*50)
#
# print(f" Thank you for your payment plaease enter you address")
#
#
#
# #         print(f"Your payment method is {payment_method} and your number is {num} ")
# #         print("Thank you for the payment detail now please add an address")
# # else:
# #     print("please enter your choice again")
#
#     # now if the payment is done add the address and send msg on the number
# address_in = input("Enter address: ")
# address_added = address.append(address_in)
# print("address added")
# print(address)
# print("="*50)
# print(f"Thank you for shopping you shipment is on the way to {address}")




# Loan approval:
# income ≥ 50,000
# credit_score ≥ 700 OR guarantor
#
# color1 = input('Enter First Color (red, blue, yellow): ').lower()
# color2 = input('Enter Second Color (red, blue, yellow): ').lower()
# colors = [color1, color2]
#
# print('-'*50)
# print(f"🥼 Let's Mix {color1} + {color2}\n")
#
# #🎨 Calculate New Color
# if color1 == color2:
#     emoji = None
#     if color1 == 'red':
#         emoji = '❤️'
#     elif color1 == 'blue':
#         emoji = '💙'
#     elif color1 == 'yellow':
#         emoji = '💛'
#
#     print("🎨 You're mixing the same color!")
#     print(f'🧪{color1} + 🧪{color2} = {color1} {emoji}.')
#
# elif 'red' in colors and 'blue' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Purple 💜.')
#
# elif 'red' in colors and 'yellow' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Orange 🧡.')
#
# elif 'blue' in colors and 'yellow' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Green 💚.')
#
# else:
#     print('❌ Invalid Color Combination. \nPlease use Red, Blue or Yellow.')




import random

# Rules
# min_       = 1
# max_       = 20
# secret_num = random.randint(min_, max_) #🤐Set any number you like!
#
# for i in range(6):
#     print('-'*40, f'Attempt {i+1}/6')
#
#     # Ask User for Input!
#     guess = input(f'❓Guess the secret number between {min_} and {max_}: ')
#     guess = int(guess)
#
#     #💡 Check the Input
#     if guess < min_ or guess > max_:
#         print(f'⛔Incorrect Input. Guess a number between {min_} and {max_}')
#
#     #👀 Check Results
#     elif guess == secret_num:
#         print('🥳Correct! You guessed it!')
#         break
#
#     elif guess > secret_num:
#         print('❌ Too High! Try Again.')
#
#     else:
#         print('❌ Too Low! Try Again.')

# Game access:
#
# level ≥ 10 OR premium_user
#
# Flight boarding:
#
# ticket_confirmed
#
# not late
#
# Bank account:
#
# balance ≥ 1000 AND not frozen
#
# Online class:
#
# internet_available
#
# device_working
#
# Emergency override:
#
# admin AND (code_verified OR supervisor_approved)



#
# # taking user input
# name = str(input("What is your name: "))
# print(f"Hello {name.upper()} how are you nice to meet you! \n"
#       f"please enter your info to check you eligiblity !!")
# age = int(input("What is your age: "))
# qualification = str(input("What is your qualification: "))
# marks = int(input("What are your marks: "))
# height = float(input("What is your height(in fts): "))
#
# # now setting the requirements of the selection
# age_ok = age > 18
# qualification_ok = qualification == "fsc"
# marks_ok = marks >= 250
# height_ok = height >= 5.4
#
# # now making the conditions and making it real
#
# while age_ok and qualification_ok and marks_ok and height_ok == True:
#     print(f"Hello {name} your are {age} years old and you have {marks} marks in {qualification}\n "
#           f"and you have {height} ft height \n"
#           f"CONGRATULATIONS!! YOU ARE ELIGIBLE! FOR THE TEST")
#
# else:
#     print(f"WE REGRETE TO INFORM YOU THAT YOU ARE NOT ELIGIBLE FOR THE TEST \n"
#           f"BECAUSE")
#     if not age_ok:
#         print("- Age must be at least 18 years")
#     if not height_ok:
#         print("- Height must be at least 5.4 ft")
#     if not qualification_ok:
#         print("- Qualification must be FSC")
#     if not marks_ok:
#         print("- Marks must be at least 60%")












