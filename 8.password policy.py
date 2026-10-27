'''Password Policy Validation Engine'''

password = input("Enter password: ")

if len(password) >= 8 and any(c.isdigit() for c in password):
    print("Valid Password")
else:
    print("Invalid Password")