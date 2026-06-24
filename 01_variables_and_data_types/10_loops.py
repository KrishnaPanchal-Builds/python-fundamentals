"""
File: 10_loops.py

Project: Number Analysis Toolkit

Concepts Covered:
- for loops
- while loops
- nested loops
- break
- continue
- mathematical computations
"""

print("=" * 60)
print("NUMBER ANALYSIS TOOLKIT")
print("=" * 60)

number = int(input("Enter a positive integer: "))

print("\n" + "=" * 60)
print("1. FACTORIAL")
print("=" * 60)

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} = {factorial}")

print("\n" + "=" * 60)
print("2. MULTIPLICATION TABLE")
print("=" * 60)

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n" + "=" * 60)
print("3. PRIME NUMBER CHECK")
print("=" * 60)

is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is NOT a Prime Number")

print("\n" + "=" * 60)
print("4. FIBONACCI SERIES")
print("=" * 60)

terms = int(input("How many Fibonacci terms would you like? "))

a = 0
b = 1

count = 0

while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

print()

print("\n" + "=" * 60)
print("5. ARMSTRONG NUMBER CHECK")
print("=" * 60)

num = number

digits = len(str(num))

total = 0

temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is NOT an Armstrong Number")

print("\n" + "=" * 60)
print("6. NUMBER STATISTICS")
print("=" * 60)

even_count = 0
odd_count = 0

for i in range(1, number + 1):

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers:", even_count)
print("Odd Numbers :", odd_count)

print("\n" + "=" * 60)
print("7. STAR PATTERN")
print("=" * 60)

rows = min(number, 10)

for i in range(1, rows + 1):
    print("*" * i)

print("\n" + "=" * 60)
print("8. BREAK & CONTINUE DEMO")
print("=" * 60)

for i in range(1, 21):

    if i == 15:
        print("Breaking at 15")
        break

    if i % 2 == 0:
        continue

    print(i, end=" ")

print()

print("\nProgram Completed Successfully.")
