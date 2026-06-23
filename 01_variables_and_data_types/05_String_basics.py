"""
Python String Fundamentals
Author: Krishna Panchal

This program demonstrates the core string operations
every Python developer should know.
"""

print("=" * 60)
print("PYTHON STRING FUNDAMENTALS")
print("=" * 60)

text = "Artificial Intelligence"

print("\nOriginal String")
print("-" * 30)
print(text)

print("\nBasic Information")
print("-" * 30)
print(f"Length: {len(text)}")
print(f"First Character: {text[0]}")
print(f"Last Character: {text[-1]}")

print("\nIndexing")
print("-" * 30)
print(f"Character at index 5: {text[5]}")
print(f"Character at index 10: {text[10]}")

print("\nString Slicing")
print("-" * 30)
print(f"First 10 characters: {text[:10]}")
print(f"Last 12 characters: {text[-12:]}")
print(f"Characters 3 to 10: {text[3:11]}")

print("\nString Concatenation")
print("-" * 30)
language = "Python"
combined = text + " with " + language
print(combined)

print("\nString Repetition")
print("-" * 30)
print(language * 3)

print("\nMembership Testing")
print("-" * 30)
print("Python" in combined)
print("Machine" in combined)

print("\nSummary")
print("-" * 30)
print("Strings are immutable sequences of characters.")
print("Indexing, slicing, concatenation, and membership")
print("form the foundation of string manipulation in Python.")
