"""
==============================================================
Assignment Operators Demonstration
==============================================================
"""

print("=" * 70)
print("           ASSIGNMENT OPERATORS DEMONSTRATION")
print("=" * 70)

salary = 50000

print(f"\nInitial Salary: ₹{salary}")

salary += 5000
print(f"After Bonus (+=): ₹{salary}")

salary -= 2500
print(f"After Tax Deduction (-=): ₹{salary}")

salary *= 2
print(f"After Performance Multiplier (*=): ₹{salary}")

salary /= 2
print(f"After Division (/=): ₹{salary}")

salary //= 3
print(f"After Floor Division (//=): ₹{salary}")

salary %= 1000
print(f"After Modulus (%=): ₹{salary}")

number = 5

print(f"\nOriginal Number: {number}")

number **= 2
print(f"After Exponentiation (**=): {number}")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
Assignment operators update the value of an existing
variable without repeatedly writing the variable name.

Operators Covered

✓ =
✓ +=
✓ -=
✓ *=
✓ /=
✓ //=
✓ %=
✓ **=
""")
