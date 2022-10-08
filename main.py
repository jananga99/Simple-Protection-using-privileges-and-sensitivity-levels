import hashlib

import Validation
from Controller import Controller

keepGoing = True
while keepGoing:
    print("Available Options (type option number e.g. Add option : 1)")
    print("11 - Register as patient")
    print("12 - Log in as patient")
    print("21 - Register as hospital staff")
    print("22 - Log in as hospital staff")

    option = input("Add option: ").strip()

    if option == "11":
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username can only contain letters and numbers)")
            username = input("Username : ").strip()
        password = input("Password : ").strip()
        while not Validation.validPassword(password):
            print("Password must be longer than 8 characters.")
            password = input("Password : ").strip()
        password = hashlib.md5(password.encode())
        confirmPassword = hashlib.md5(input("Confirm password : ").strip().encode())
        while password.hexdigest() != confirmPassword.hexdigest():
            print("Password and confirm password does not match, try again.")
            password = hashlib.md5(input("Password : ").strip().encode())
            confirmPassword = hashlib.md5(input("Password : ").strip().encode())
        controller = Controller(username, password.hexdigest(), "patient")
        success, result = controller.register()
        if success:
            print("Patient registered successfully")
        else:
            print(result)

    elif option == "21":
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username can only contain letters and numbers)")
            username = input("Username : ").strip()
        password = hashlib.md5(input("Password : ").strip().encode())
        confirmPassword = hashlib.md5(input("Confirm Password : ").strip().encode())
        while password.hexdigest() != confirmPassword.hexdigest():
            print("Password and confirm password does not match, try again.")
            password = hashlib.md5(input("Password : ").strip().encode())
            confirmPassword = hashlib.md5(input("Password : ").strip().encode())
        controller = Controller(username, password.hexdigest(), "hospital staff")
        success, result = controller.register()
        if success:
            print("Hospital staff registered successfully")
        else:
            print(result)

    elif option == "12":
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username can only contain letters and numbers)")
            username = input("Username : ").strip()
        password = hashlib.md5(input("Password : ").strip().encode())
        controller = Controller(username, password.hexdigest(), "patient")
        success, result = controller.login()
        if success:
            print("Patient logged in successfully.")
        else:
            print(result)

    elif option == "22":
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username can only contain letters and numbers)")
            username = input("Username : ").strip()
        password = hashlib.md5(input("Password : ").strip().encode())
        controller = Controller(username, password.hexdigest(), "hospital staff")
        success, result = controller.login()
        if success:
            print("Hospital staff logged in successfully.")
        else:
            print(result)

    else:
        print("Add a valid option")
        continue

    exitOption = input("Want to exit?/(y/N) : ")
    while exitOption.lower() not in ["y", "n"]:
        print("Exit option must be 'y' or 'N'")
        exitOption = input("Want to exit?/(y/N")

    if exitOption == "y":
        keepGoing = False

print("The program finished.")
