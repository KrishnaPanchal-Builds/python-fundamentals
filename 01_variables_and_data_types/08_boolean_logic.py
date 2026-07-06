"""
===============================================================================
File    : 08_boolean_logic.py
Project : Smart Login & Access Verification System
Author  : Krishna Panchal

Concepts Covered
----------------
✓ Variables
✓ Data Types
✓ Type Casting
✓ User Input
✓ String Operations
✓ Boolean Logic
===============================================================================
"""

print("=" * 80)
print("SMART LOGIN & ACCESS VERIFICATION SYSTEM")
print("=" * 80)

# ------------------------------------------------------------------------------
# USER DETAILS
# ------------------------------------------------------------------------------

full_name = input("Enter Full Name             : ").title()

username = input("Enter Username              : ").strip()

password = input("Enter Password              : ")

email = input("Enter Email Address         : ").strip().lower()

phone = input("Enter Phone Number          : ").strip()

age = int(input("Enter Age                   : "))

country = input("Enter Country               : ").title()

# ------------------------------------------------------------------------------
# ACCOUNT INFORMATION
# ------------------------------------------------------------------------------

print("\nAccount Information")

is_registered = input(
    "Registered User (yes/no) : "
).strip().lower() == "yes"

is_email_verified = input(
    "Email Verified (yes/no)  : "
).strip().lower() == "yes"

is_phone_verified = input(
    "Phone Verified (yes/no)  : "
).strip().lower() == "yes"

is_two_factor_enabled = input(
    "2FA Enabled (yes/no)     : "
).strip().lower() == "yes"

is_premium_member = input(
    "Premium Member (yes/no)  : "
).strip().lower() == "yes"

is_employee = input(
    "Company Employee (yes/no): "
).strip().lower() == "yes"

is_admin = input(
    "Administrator (yes/no)   : "
).strip().lower() == "yes"

# ------------------------------------------------------------------------------
# BOOLEAN VALIDATIONS
# ------------------------------------------------------------------------------

username_valid = len(username) >= 5

password_valid = len(password) >= 8

email_valid = (
    "@" in email and
    "." in email
)

phone_valid = (
    phone.isdigit() and
    len(phone) == 10
)

adult_user = age >= 18

eligible_for_login = (
    is_registered and
    username_valid and
    password_valid and
    email_valid and
    is_email_verified and
    phone_valid and
    is_phone_verified and
    adult_user
)

premium_access = (
    eligible_for_login and
    is_premium_member
)

employee_portal = (
    eligible_for_login and
    is_employee
)

admin_panel = (
    employee_portal and
    is_admin
)

secure_account = (
    eligible_for_login and
    is_two_factor_enabled
)

# ------------------------------------------------------------------------------
# VALIDATION REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("ACCOUNT VALIDATION REPORT")
print("=" * 80)

print(f"Username Valid          : {username_valid}")
print(f"Password Valid          : {password_valid}")
print(f"Email Valid             : {email_valid}")
print(f"Phone Valid             : {phone_valid}")
print(f"Adult User              : {adult_user}")

print("-" * 80)

print(f"Eligible For Login      : {eligible_for_login}")
print(f"Premium Access          : {premium_access}")
print(f"Employee Portal Access  : {employee_portal}")
print(f"Administrator Access    : {admin_panel}")
print(f"Secure Account          : {secure_account}")

print("-" * 80)

print("Part 1 Completed Successfully.")

# ==============================================================================
# SECURITY SCORE
# ==============================================================================

security_score = 0

if username_valid:
    security_score += 1

if password_valid:
    security_score += 2

if email_valid:
    security_score += 1

if phone_valid:
    security_score += 1

if is_email_verified:
    security_score += 1

if is_phone_verified:
    security_score += 1

if is_two_factor_enabled:
    security_score += 2

if is_registered:
    security_score += 1

# ==============================================================================
# ACCOUNT RISK LEVEL
# ==============================================================================

if security_score >= 9:
    risk_level = "Very Low"

elif security_score >= 7:
    risk_level = "Low"

elif security_score >= 5:
    risk_level = "Medium"

else:
    risk_level = "High"

# ==============================================================================
# FINAL LOGIN DECISION
# ==============================================================================

login_allowed = (
    eligible_for_login and
    not (
        is_admin and
        not is_two_factor_enabled
    )
)

# ==============================================================================
# SECURITY RECOMMENDATIONS
# ==============================================================================

print("\n" + "=" * 80)
print("SECURITY RECOMMENDATIONS")
print("=" * 80)

if not username_valid:
    print("• Username should contain at least 5 characters.")

if not password_valid:
    print("• Password should contain at least 8 characters.")

if not email_valid:
    print("• Enter a valid email address.")

if not phone_valid:
    print("• Enter a valid 10-digit phone number.")

if not is_email_verified:
    print("• Verify your email address.")

if not is_phone_verified:
    print("• Verify your phone number.")

if not is_two_factor_enabled:
    print("• Enable Two-Factor Authentication.")

if not is_registered:
    print("• Complete account registration.")

if is_admin and not is_two_factor_enabled:
    print("• Administrator accounts must enable 2FA.")

# ==============================================================================
# ACCOUNT SUMMARY
# ==============================================================================

print("\n" + "=" * 80)
print("ACCOUNT SUMMARY")
print("=" * 80)

print(f"User Name              : {full_name}")
print(f"Username               : {username}")
print(f"Country                : {country}")
print(f"Premium Member         : {is_premium_member}")
print(f"Company Employee       : {is_employee}")
print(f"Administrator          : {is_admin}")

print("-" * 80)

print(f"Security Score         : {security_score}/10")
print(f"Risk Level             : {risk_level}")
print(f"Secure Account         : {secure_account}")
print(f"Login Allowed          : {login_allowed}")

print("-" * 80)

print(f"Premium Dashboard      : {premium_access}")
print(f"Employee Portal        : {employee_portal}")
print(f"Administrator Panel    : {admin_panel}")

print("=" * 80)

# ==============================================================================
# FINAL MESSAGE
# ==============================================================================

if login_allowed:

    print("✅ Login Successful!")

    if secure_account:
        print("Your account is well protected.")

    else:
        print("Login successful, but your account security can be improved.")

else:

    print("❌ Login Failed!")
    print("Please resolve the issues listed above before trying again.")

print("=" * 80)
print("SMART LOGIN & ACCESS VERIFICATION COMPLETED")
print("=" * 80)
