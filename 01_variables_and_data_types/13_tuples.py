"""
File: 13_tuples.py
Author : Krishna Panchal

Project: Employee Database Snapshot System

Concepts Covered:
- Tuples
- Tuple Packing
- Tuple Unpacking
- Tuple Methods
- Immutable Data
- Nested Tuples
"""

print("=" * 60)
print("EMPLOYEE DATABASE SNAPSHOT SYSTEM")
print("=" * 60)

employees = (
    ("E101", "Rahul", "Data Analyst", 55000),
    ("E102", "Priya", "Data Scientist", 85000),
    ("E103", "Amit", "ML Engineer", 95000),
    ("E104", "Neha", "AI Engineer", 120000)
)

print("\nEmployee Records")

for emp_id, name, role, salary in employees:
    print(
        f"{emp_id} | {name} | {role} | ₹{salary}"
    )

print("\n" + "=" * 60)
print("SEARCH EMPLOYEE")
print("=" * 60)

search_id = input(
    "Enter Employee ID: "
).upper()

found = False

for employee in employees:

    if employee[0] == search_id:

        emp_id, name, role, salary = employee

        print("\nRecord Found")

        print("ID     :", emp_id)
        print("Name   :", name)
        print("Role   :", role)
        print("Salary :", salary)

        found = True
        break

if not found:
    print("Employee Not Found")

print("\n" + "=" * 60)
print("SALARY ANALYSIS")
print("=" * 60)

salaries = tuple(
    employee[3]
    for employee in employees
)

print("Highest Salary :", max(salaries))
print("Lowest Salary  :", min(salaries))
print("Average Salary :", sum(salaries)/len(salaries))

print("\n" + "=" * 60)
print("TUPLE METHODS")
print("=" * 60)

sample = (10, 20, 30, 20, 40, 20)

print("Count of 20 :", sample.count(20))
print("Index of 40 :", sample.index(40))

print("\nProgram Completed Successfully.")
