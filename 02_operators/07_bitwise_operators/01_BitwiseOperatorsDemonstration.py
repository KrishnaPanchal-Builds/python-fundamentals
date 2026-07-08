"""
======================================================================
🐍 Python Fundamentals

Module 02 : Operators

Demonstration : Bitwise Operators Demonstration

Description:
This program demonstrates the practical use of Python
bitwise operators by performing operations on two integers.

Concepts Covered:
• &
• |
• ^
• ~
• <<
• >>

Difficulty Level : Beginner
Python Version   : 3.x

Author : Krishna Panchal
======================================================================
"""

# =====================================================================
# BITWISE OPERATORS DEMONSTRATION
# =====================================================================

print("=" * 70)
print("            BITWISE OPERATORS DEMONSTRATION")
print("=" * 70)

print("""
Bitwise operators perform operations directly on the
binary representation of integers.

This demonstration shows how each bitwise operator
works using two numbers.
""")

# =====================================================================
# USER INPUT
# =====================================================================

print("\n" + "=" * 70)
print("                    USER INPUT")
print("=" * 70)

number1 = int(input("Enter First Number  : "))
number2 = int(input("Enter Second Number : "))

# =====================================================================
# BITWISE OPERATIONS
# =====================================================================

bitwise_and = number1 & number2

bitwise_or = number1 | number2

bitwise_xor = number1 ^ number2

bitwise_not = ~number1

left_shift = number1 << 1

right_shift = number1 >> 1

# =====================================================================
# BITWISE REPORT
# =====================================================================

print("\n" + "=" * 70)
print("                 BITWISE REPORT")
print("=" * 70)

print(f"""
First Number                 : {number1}

Second Number                : {number2}

Bitwise AND (&)              : {bitwise_and}

Bitwise OR (|)               : {bitwise_or}

Bitwise XOR (^)              : {bitwise_xor}

Bitwise NOT (~{number1})      : {bitwise_not}

Left Shift ({number1} << 1)   : {left_shift}

Right Shift ({number1} >> 1)  : {right_shift}
""")

# =====================================================================
# SUMMARY
# =====================================================================

print("\n" + "=" * 70)
print("                     SUMMARY")
print("=" * 70)

print("""
Bitwise Operators Used

✓ &
Performs Bitwise AND.

✓ |
Performs Bitwise OR.

✓ ^
Performs Bitwise XOR.

✓ ~
Performs Bitwise NOT.

✓ <<
Shifts bits to the left.

✓ >>
Shifts bits to the right.

Bitwise operators work directly on the binary
representation of integers and are commonly used
in system programming and performance optimization.
""")

# =====================================================================
# REAL-WORLD APPLICATIONS
# =====================================================================

print("\n" + "=" * 70)
print("               REAL-WORLD APPLICATIONS")
print("=" * 70)

print("""
Bitwise operators are widely used in:

💻 Operating Systems

🌐 Computer Networks

🔐 Encryption & Security

📦 Data Compression

🤖 Embedded Systems

🎮 Game Development

🛰️ Device Drivers

☁️ Cloud Computing

📡 Communication Protocols

⚡ High-Performance Computing
""")

# =====================================================================
# INTERVIEW CORNER
# =====================================================================

print("\n" + "=" * 70)
print("                  INTERVIEW CORNER")
print("=" * 70)

print("""
1. What are bitwise operators?

Answer:
Bitwise operators perform operations on the binary
representation of integers.

--------------------------------------------------------------

2. Which operator performs Bitwise AND?

Answer:
&

--------------------------------------------------------------

3. Which operator performs Bitwise OR?

Answer:
|

--------------------------------------------------------------

4. Which operator performs Bitwise XOR?

Answer:
^

--------------------------------------------------------------

5. What does the left shift operator (<<) do?

Answer:
It shifts all bits to the left and is equivalent
to multiplying a positive integer by powers of two.

--------------------------------------------------------------

6. What does the right shift operator (>>) do?

Answer:
It shifts all bits to the right and is equivalent
to dividing a positive integer by powers of two.
""")

# =====================================================================
# COMMON BEGINNER MISTAKES
# =====================================================================

print("\n" + "=" * 70)
print("             COMMON BEGINNER MISTAKES")
print("=" * 70)

print("""
❌ Confusing bitwise operators with logical operators.

❌ Using bitwise operators on non-integer values.

❌ Assuming '^' means exponentiation.
(In Python, exponentiation uses '**'.)

❌ Forgetting that '~' returns the two's complement
of a number.

❌ Not understanding how binary representation
affects the result.
""")

# =====================================================================
# PRACTICE CHALLENGE
# =====================================================================

print("\n" + "=" * 70)
print("                PRACTICE CHALLENGE")
print("=" * 70)

print("""
Try different pairs of numbers and observe how the
results change.

Experiment with:

• Different values for AND (&)
• Different values for OR (|)
• Different values for XOR (^)
• Larger left shifts (<<)
• Larger right shifts (>>)

Compare the decimal results with their binary
representations.
""")

# =====================================================================
# DEMONSTRATION COMPLETED
# =====================================================================

print("\n" + "=" * 70)
print("        DEMONSTRATION COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("""
Demonstration:
💡 Bitwise Operators Demonstration

Congratulations!

You have successfully learned the fundamentals of
Python bitwise operators.

Keep Learning.
Keep Practicing.
Keep Building.

🐍 Python Fundamentals Repository

Author : Krishna Panchal
""")

print("=" * 70)
