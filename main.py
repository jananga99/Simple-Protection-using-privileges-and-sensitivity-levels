import xml.etree.ElementTree as ET

from User import User

tree = ET.parse('conf.xml')
root = tree.getroot()


keepGoing = True
while keepGoing:
    option = input("Add option: ").strip()
    if option == "1":
        print("Add new user")
        username = input("Username : ").strip()
        password = input("Password : ").strip()
        usertype = input("Usertype(hospital_staff or patient) : ").strip()
        while usertype not in ["hospital_staff", "patient"]:
            print("Usertype can be only 'hospital_staff or 'patient")
            usertype = input("Usertype(hospital_staff or patient): ").strip()
        privilege = '2'
        user = User(username, password, usertype, privilege)
        user.createTag(root)
        tree.write("conf.xml")

    exitOption = input("Want to exit?/(y/N) : ")
    while exitOption.lower() not in ["y", "n"]:
        print("Exit option must be 'y' or 'N'")
        exitOption = input("Want to exit?/(y/N")

    if exitOption == "y":
        keepGoing = False

print("The program finished.")
