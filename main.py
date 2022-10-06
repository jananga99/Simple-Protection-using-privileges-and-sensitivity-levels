import hashlib
import xml.etree.ElementTree as ET

from DrugPrescription import DrugPrescription
from LabTestPrescription import LabTestPrescription
from PersonalDetails import PersonalDetails
from SicknessDetails import SicknessDetails
from User import User

configurationFile = 'conf.xml'
configurationTree = ET.parse(configurationFile)
configurationRoot = configurationTree.getroot()

dataFile = 'data.xml'
dataTree = ET.parse(dataFile)
dataRoot = dataTree.getroot()


keepGoing = True
while keepGoing:
    print("Available Options (type option number e.g. Add option : 1)")
    print("0 - Add new staff")
    print("1 - Add new patient")
    print("2 - Add personal details")
    print("3 - Add sickness details")
    print("4 - Add drug prescription")
    print("5 - Add lab test prescription")
    print("6 - Modify personal details")
    print("7 - Modify sickness details")
    print("8 - Modify drug prescription")
    print("9 - Modify lab test prescription")
    option = input("Add option: ").strip()
    while option not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("Option must be one of given number options")
        option = input("Add option: ").strip()
    if option == "1" or option == "0":
        if option == "1":
            print("Add new patient")
            usertype = 'patient'
        else:
            print("Add new staff")
            usertype = "hospital_staff"
        username = input("Username : ").strip()
        password = hashlib.md5(input("Password : ").strip().encode())
        if option == "0":
            privilege = input("Privilege Level : ").strip()
            while not privilege.isnumeric():
                print("Privilege level must be 0 or positive integer.")
                privilege = input("Privilege Level : ").strip()
        else:
            privilege = '0'
        user = User(username, password, usertype, privilege)
        user.createTag(configurationRoot)
        configurationTree.write(configurationFile)

    elif option == '2':
        print("Add personal details")
        name = input("Full Name : ").strip()
        age = input("Age : ").strip()
        while not age.isnumeric():
            print("Age must be a positive integer")
            age = input("Age : ").strip()
        gender = input("Gender (male/female) : ").strip().lower()
        while gender not in ['male', 'female']:
            print("Gender must be 'male' or 'female'")
            gender = input("Gender (male/female) : ").strip().lower()
        city = input("City : ").strip()
        sensitivity = input("Sensitivity : ").strip()
        while not sensitivity.isnumeric():
            print("Sensitivity is a number")
            sensitivity = input().strip()
        personalDetails = PersonalDetails("-1", name, age, gender, city, sensitivity)
        tagId = personalDetails.createTag(dataRoot)
        print("Personal Id : " + tagId)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

    elif option == '6':
        print("Modify personal details")
        print("Keep the field empty not to modify")
        personalId = input("PersonalId : ").strip()
        while not personalId.isnumeric() or PersonalDetails.findTag(dataRoot, personalId) is None:
            print("Add valid personal id")
            personalId = input("PersonalId : ").strip()
        personalDetails = PersonalDetails.readTag(PersonalDetails.findTag(dataRoot, personalId))
        name = input("Full Name : "+"("+personalDetails.name+") ").strip()
        if name == '':
            name = personalDetails.name
        age = input("Age : "+"("+personalDetails.age+") ").strip()
        while not age.isnumeric() and age!='':
            print("Age must be a positive integer")
            age = input("Age : "+"("+personalDetails.age+") ").strip()
        if age=='':
            age = personalDetails.age
        gender = input("Gender (male/female) : "+"("+personalDetails.gender+") ").strip().lower()
        while gender not in ['male', 'female'] and gender!='':
            print("Gender must be 'male' or 'female'")
            gender = input("Gender (male/female) : "+"("+personalDetails.gender+") ").strip().lower()
        if gender=='':
            gender = personalDetails.gender
        city = input("City : "+"("+personalDetails.city+") ").strip()
        if city=='':
            city = personalDetails.city
        sensitivity = input("Sensitivity : "+"("+personalDetails.sensitivity+") ").strip()
        while not sensitivity.isnumeric() and sensitivity!='':
            print("Sensitivity is a number")
            sensitivity = input("Sensitivity : "+"("+personalDetails.sensitivity+") ").strip()
        if sensitivity=='':
            sensitivity = personalDetails.sensitivity
        personalDetails = PersonalDetails(personalId, name, age, gender, city, sensitivity)
        personalDetails.modifyTag(dataRoot)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

    elif option == '3':
        print("Add sickness details")
        personalId = input("PersonalId : ").strip()
        while not personalId.isnumeric() or PersonalDetails.findTag(dataRoot, personalId) is None:
            print("Add valid personal id")
            personalId = input("PersonalId : ").strip()
        name = input("Sickness Name : ").strip()
        details = input("Details : ").strip()
        sensitivity = input("Sensitivity : ").strip()
        while not sensitivity.isnumeric():
            print("Sensitivity is a number")
            sensitivity = input().strip()
        sicknessDetails = SicknessDetails("-1", personalId, name, details, sensitivity)
        tagId = sicknessDetails.createTag(dataRoot)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

    elif option == '7':
        print("Modify sickness details")
        personalId = input("PersonalId : ").strip()
        while not personalId.isnumeric() or PersonalDetails.findTag(dataRoot, personalId) is None:
            print("Add valid personal id")
            personalId = input("PersonalId : ").strip()
        personalDetails = PersonalDetails.readTag(PersonalDetails.findTag(dataRoot, personalId))
        name = input("Full Name : "+"("+personalDetails.name+") ").strip()
        if name == '':
            name = personalDetails.name
        name = input("Sickness Name : "+"("+personalDetails.name+") ").strip()
        details = input("Details : ").strip()
        sensitivity = input("Sensitivity : ").strip()
        while not sensitivity.isnumeric():
            print("Sensitivity is a number")
            sensitivity = input().strip()
        sicknessDetails = SicknessDetails("-1", personalId, name, details, sensitivity)
        tagId = sicknessDetails.createTag(dataRoot)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

    elif option == '4':
        print("Add drug prescription")
        personalId = input("PersonalId : ").strip()
        while not personalId.isnumeric() or PersonalDetails.findTag(dataRoot, personalId) is None:
            print("Add valid personal id")
            personalId = input("PersonalId : ").strip()
        name = input("Drug Name : ").strip()
        details = input("Details : ").strip()
        sensitivity = input("Sensitivity : ").strip()
        while not sensitivity.isnumeric():
            print("Sensitivity is a number")
            sensitivity = input().strip()
        drugPrescription = DrugPrescription("-1", personalId, name, details, sensitivity)
        tagId = drugPrescription.createTag(dataRoot)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

    elif option == '5':
        print("Add lab test prescription")
        personalId = input("PersonalId : ").strip()
        while not personalId.isnumeric() or PersonalDetails.findTag(dataRoot, personalId) is None:
            print("Add valid personal id")
            personalId = input("PersonalId : ").strip()
        name = input("Lab test Name : ").strip()
        details = input("Details : ").strip()
        sensitivity = input("Sensitivity : ").strip()
        while not sensitivity.isnumeric():
            print("Sensitivity is a number")
            sensitivity = input().strip()
        tagId = labTestPrescription = LabTestPrescription("-1", personalId, name, details, sensitivity)
        labTestPrescription.createTag(dataRoot)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)



    exitOption = input("Want to exit?/(y/N) : ")
    while exitOption.lower() not in ["y", "n"]:
        print("Exit option must be 'y' or 'N'")
        exitOption = input("Want to exit?/(y/N")

    if exitOption == "y":
        keepGoing = False

print("The program finished.")
