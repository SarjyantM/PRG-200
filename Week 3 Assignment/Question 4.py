#Password Strength Checker By Sarjyant 

known_weak_passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if ch in "!@#$%^&*":
        has_special = True

meets_length = len(password) >= 8

# Check if all criteria are met
if meets_length and has_upper and has_lower and has_digit and has_special:
    if password in known_weak_passwords:
        print("Weak Password! try making a stronger one.")
    else:
        print("Strong Password!")
else:
    print("Weak Password")
    print("Criteria Not Fulfilled! Please ensure:")
    
    # Print specific missing criteria
    if not meets_length:
        print("- At least 8 characters long")
    if not has_upper:
        print("- Contains at least one uppercase letter")
    if not has_lower:
        print("- Contains at least one lowercase letter")
    if not has_digit:
        print("- Contains at least one digit")
    if not has_special:
        print("- Contains at least one special character from !@#$%^&*")
