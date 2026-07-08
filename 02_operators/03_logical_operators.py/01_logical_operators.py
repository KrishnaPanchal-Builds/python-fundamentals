"""
======================================================================
🐍 Python Fundamentals

Module 02 : Operators
File       : 01_logical_operators.py

Topic:
Logical Operators

Description:
This program demonstrates the practical use of Python
logical operators through multiple real-world examples.

Concepts Covered:
• and
• or
• not

Author : Krishna Panchal
======================================================================
"""

print("=" * 70)
print("                 PYTHON LOGICAL OPERATORS")
print("=" * 70)

# ==============================================================
# Example 1 : AND Operator
# ==============================================================

print("\nEXAMPLE 1 : AND OPERATOR")
print("-" * 70)

age = 22
has_license = True

print("Age:", age)
print("Has Driving License:", has_license)

print("\nResult:")
print((age >= 18) and has_license)

# ==============================================================
# Example 2 : OR Operator
# ==============================================================

print("\n" + "=" * 70)
print("EXAMPLE 2 : OR OPERATOR")
print("=" * 70)

email_verified = False
phone_verified = True

print("Email Verified:", email_verified)
print("Phone Verified:", phone_verified)

print("\nResult:")
print(email_verified or phone_verified)

# ==============================================================
# Example 3 : NOT Operator
# ==============================================================

print("\n" + "=" * 70)
print("EXAMPLE 3 : NOT OPERATOR")
print("=" * 70)

is_raining = True

print("Is it raining?", is_raining)

print("\nResult:")
print(not is_raining)

# ==============================================================
# Example 4 : Student Eligibility
# ==============================================================

print("\n" + "=" * 70)
print("EXAMPLE 4 : STUDENT ELIGIBILITY")
print("=" * 70)

marks = 78
attendance = 86

print("Marks:", marks)
print("Attendance:", attendance)

print("\nEligible Condition:")
print((marks >= 40) and (attendance >= 75))

# ==============================================================
# Example 5 : Online Shopping
# ==============================================================

print("\n" + "=" * 70)
print("EXAMPLE 5 : ONLINE SHOPPING")
print("=" * 70)

cart_value = 3500
premium_member = False

print("Cart Value:", cart_value)
print("Premium Member:", premium_member)

print("\nFree Delivery Eligibility:")
print((cart_value >= 1000) or premium_member)

# ==============================================================
# Example 6 : Login Authentication
# ==============================================================

print("\n" + "=" * 70)
print("EXAMPLE 6 : LOGIN AUTHENTICATION")
print("=" * 70)

username_correct = True
password_correct = True

print("Username Correct:", username_correct)
print("Password Correct:", password_correct)

print("\nAuthentication Result:")
print(username_correct and password_correct)

# ==============================================================
# Example 7 : Account Status
# ==============================================================

print("\n" + "=" * 70)
print("EXAMPLE 7 : ACCOUNT STATUS")
print("=" * 70)

account_blocked = False

print("Account Blocked:", account_blocked)

print("\nAccount Accessible:")
print(not account_blocked)

# ==============================================================
# SUMMARY
# ==============================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
Logical Operators Learned:

✓ and
✓ or
✓ not

These operators combine or modify Boolean expressions
and are widely used before introducing conditional
statements.
""")
