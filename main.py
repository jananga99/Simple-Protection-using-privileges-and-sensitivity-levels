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
    print("6 - View patient")
    print("7 - View staff")
    print("8 - View personal details")
    print("9 - View sickness details")
    print("10 - View drug prescription")
    print("11 - View lab test prescription")
    print("Log - Log in")
    print("Out - Log out")

    option = input("Add option: ").strip()
    while option not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'Log', 'Out']:
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

    elif option == '6':
        print('View patient')
        username = input("Patient username : ").strip()
        user = User.readTag(User.findTag(configurationRoot, username))
        while user is None or user.usertype != 'patient':
            print('Enter valid username')
            username = input("Patient username : ").strip()
            user = User.readTag(User.findTag(configurationRoot, username))
        print("Username : " + username)
        print("User type : " + user.usertype)
        print("Privilege Level : " + user.privilege)

    elif option == '7':
        print('View staff')
        username = input("Hospital Staff username : ").strip()
        user = User.readTag(User.findTag(configurationRoot, username))
        while user is None or user.usertype != 'hospital_staff':
            print('Enter valid username')
            username = input("Hospital staff username : ").strip()
            user = User.readTag(User.findTag(configurationRoot, username))
        print("Username : " + username)
        print("User type : " + user.usertype)
        print("Privilege Level : " + user.privilege)

    elif option == '8':
        print("View personal details")
        personalId = input("PersonalId : ").strip()
        while not personalId.isnumeric() or PersonalDetails.findTag(dataRoot, personalId) is None:
            print("Add valid personal id")
            personalId = input("PersonalId : ").strip()
        personalDetails = PersonalDetails.readTag(PersonalDetails.findTag(dataRoot, personalId))
        print("Personal Id : " + personalDetails.tagId)
        print("Full name : "+personalDetails.name)
        print("Age : "+personalDetails.age)
        print("Gender : "+personalDetails.gender)
        print("City : "+personalDetails.city)
        print("Sensitivity : "+personalDetails.sensitivity)

    elif option == '9':
        print("View sickness details")
        sicknessId = input("SicknessId : ").strip()
        while not sicknessId.isnumeric() or SicknessDetails.findTag(dataRoot, sicknessId) is None:
            print("Add valid sickness id")
            sicknessId = input("SicknessId : ").strip()
        sicknessDetails = SicknessDetails.readTag(SicknessDetails.findTag(dataRoot, sicknessId))
        print("Sickness Id : " + sicknessDetails.tagId)
        print("Patient Id : " + sicknessDetails.personalId)
        print("Sickness name : "+sicknessDetails.name)
        print("Details : "+sicknessDetails.details)
        print("Sensitivity : "+sicknessDetails.sensitivity)

    elif option == '10':
        print("View drug prescription")
        drugPrescriptionId = input("Drug prescription id : ").strip()
        while not drugPrescriptionId.isnumeric() or DrugPrescription.findTag(dataRoot, drugPrescriptionId) is None:
            print("Add valid drug prescription id")
            drugPrescriptionId = input("DrugPrescriptionId : ").strip()
        drugPrescription = DrugPrescription.readTag(DrugPrescription.findTag(dataRoot, drugPrescriptionId))
        print("Sickness Id : " + drugPrescription.tagId)
        print("Patient Id : " + drugPrescription.personalId)
        print("Sickness name : "+drugPrescription.name)
        print("Details : "+drugPrescription.details)
        print("Sensitivity : "+drugPrescription.sensitivity)

    elif option == '11':
        print("View lab test prescription")
        labTestPrescriptionId = input("Lab test prescription id : ").strip()
        while not labTestPrescriptionId.isnumeric() or LabTestPrescription.findTag(dataRoot, labTestPrescriptionId) is None:
            print("Add valid lab test prescription id")
            labTestPrescriptionId = input("LabTestPrescriptionId : ").strip()
        labTestPrescription = LabTestPrescription.readTag(LabTestPrescription.findTag(dataRoot, labTestPrescriptionId))
        print("Sickness Id : " + labTestPrescription.tagId)
        print("Patient Id : " + labTestPrescription.personalId)
        print("Sickness name : "+labTestPrescription.name)
        print("Details : "+labTestPrescription.details)
        print("Sensitivity : "+labTestPrescription.sensitivity)

    exitOption = input("Want to exit?/(y/N) : ")
    while exitOption.lower() not in ["y", "n"]:
        print("Exit option must be 'y' or 'N'")
        exitOption = input("Want to exit?/(y/N")

    if exitOption == "y":
        keepGoing = False

print("The program finished.")
