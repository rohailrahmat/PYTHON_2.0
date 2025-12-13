# LOGICAL OPERATOS
# AND operator--------------
# True AND True   → True
# True AND False  → False
# False AND True  → False
# False AND False → False

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
















