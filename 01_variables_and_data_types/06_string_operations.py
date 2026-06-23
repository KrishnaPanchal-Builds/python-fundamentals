"""
Python String Operations Showcase
Author: Krishna Panchal

This program demonstrates the most commonly used
string methods in Python.
"""

print("=" * 60)
print("PYTHON STRING OPERATIONS SHOWCASE")
print("=" * 60)

text = "  artificial intelligence with python  "

print("\nOriginal String")
print("-" * 40)
print(f"'{text}'")

# Case Conversion Methods
print("\nCase Conversion Methods")
print("-" * 40)
print("Upper Case      :", text.upper())
print("Lower Case      :", text.lower())
print("Title Case      :", text.title())
print("Capitalized     :", text.capitalize())
print("Swap Case       :", text.swapcase())

# Removing Whitespaces
print("\nWhitespace Operations")
print("-" * 40)
print("Strip           :", text.strip())
print("Left Strip      :", text.lstrip())
print("Right Strip     :", text.rstrip())

# Search Operations
clean_text = text.strip()

print("\nSearch Operations")
print("-" * 40)
print("Find 'python'   :", clean_text.find("python"))
print("Count 'i'       :", clean_text.count("i"))
print("Starts With 'artificial' :", clean_text.startswith("artificial"))
print("Ends With 'python'       :", clean_text.endswith("python"))

# Replace Operation
print("\nReplace Operation")
print("-" * 40)
print(clean_text.replace("python", "machine learning"))

# Split Operation
print("\nSplit Operation")
print("-" * 40)
words = clean_text.split()
print(words)

# Join Operation
print("\nJoin Operation")
print("-" * 40)
joined_text = " | ".join(words)
print(joined_text)

# String Validation Methods
sample1 = "Python123"
sample2 = "12345"

print("\nValidation Methods")
print("-" * 40)
print(f"{sample1}.isalnum() :", sample1.isalnum())
print(f"{sample1}.isalpha() :", sample1.isalpha())
print(f"{sample2}.isdigit() :", sample2.isdigit())

# Formatting Example
name = "Krishna"
domain = "Artificial Intelligence"

print("\nFormatted Output")
print("-" * 40)
print(f"{name} is learning {domain}.")

print("\n" + "=" * 60)
print("STRING OPERATIONS COMPLETED SUCCESSFULLY")
print("=" * 60)
