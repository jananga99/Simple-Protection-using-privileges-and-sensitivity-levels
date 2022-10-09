
import hashlib

import Validation
from Model import Model

keepGoing = True
options = {
    "101": "101 - Register patient",
    "102": "102 - Log in patient",
    "103": "103 - Log out",
    "201": "201 - Register hospital staff",
    "202": "202 - Log in hospital staff",
    "211": "211 - Add Personal Details",
    "212": "212 - Add Sickness Details",
    "213": "213 - Add Drug Prescription",
    "214": "214 - Add Lab Test Prescription",
    "221": "221 - View Personal Details",
    "222": "222 - View Sickness Details",
    "223": "223 - View Drug Prescription",
    "224": "224 - View Lab Test Prescription",
    "231": "231 - Edit Personal Details",
    "232": "232 - Edit Sickness Details",
    "233": "233 - Edit Drug Prescription",
    "234": "234 - Edit Lab Test Prescription",
    "241": "241 - Delete Personal Details",
    "242": "242 - Delete Sickness Details",
    "243": "243 - Delete Drug Prescription",
    "244": "244 - Delete Lab Test Prescription",
}
availableOptions = ["101", "102", "201", "202"]
controller = None
while keepGoing:
    print("Available Options (type option number e.g. Add option : 1)")

    for _ in availableOptions:
        print(options[_])

    option = input("Add option: ").strip()
    while option not in availableOptions:
        print("Add a valid option")
        option = input("Add option: ").strip()

    # Register patient
    if option == "101":
        print("Register patient")
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username can only contain letters and numbers)")
            username = input("Username : ").strip()

        password = input("Password : ").strip()
        while not Validation.validPassword(password):
            print("Password must be longer than 8 characters.")
            password = input("Password : ").strip()
        confirmPassword = input("Confirm password : ").strip()
        while password != confirmPassword:
            password = input("Password : ").strip()
            while not Validation.validPassword(password):
                print("Password must be longer than 8 characters.")
                password = input("Password : ").strip()
            confirmPassword = input("Confirm password : ").strip()
        password = hashlib.md5(password.encode())
        confirmPassword = hashlib.md5(confirmPassword.encode())

        controller = Model(username, password.hexdigest(), "patient")
        success, result = controller.register()
        if success:
            print("Patient registered successfully")
        else:
            print(result)

    # Register as Hospital Staff
    elif option == "201":
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username must have at least 4 character)")
            username = input("Username : ").strip()
        password = input("Password : ").strip()
        while not Validation.validPassword(password):
            print("Password must be longer than 8 characters.")
            password = input("Password : ").strip()
        confirmPassword = input("Confirm password : ").strip()
        while password != confirmPassword:
            password = input("Password : ").strip()
            while not Validation.validPassword(password):
                print("Password must be longer than 8 characters.")
                password = input("Password : ").strip()
            confirmPassword = input("Confirm password : ").strip()
        password = hashlib.md5(password.encode())
        confirmPassword = hashlib.md5(confirmPassword.encode())
        print("Available professions (type profession number e.g. profession : 6 for doctor)")
        print("6 - Doctor")
        print("5 - Nurse")
        print("4 - LabTechnician")
        print("3 - Pharmacist")
        print("2 - Receptionist")
        print("1 - Attendant")
        privilege = input("Enter privilege : ").strip()
        while privilege not in {"1", "2", "3", "4", "5", "6"}:
            print("Enter valid profession number")
            privilege = input("Enter privilege : ").strip()
        controller = Model(username, password.hexdigest(), "hospital staff")
        success, result = controller.register(privilege)
        if success:
            print("Hospital staff registered successfully")
        else:
            print(result)

    # Log in patient
    elif option == "102":
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username can only contain letters and numbers)")
            username = input("Username : ").strip()
        password = hashlib.md5(input("Password : ").strip().encode())
        controller = Model(username, password.hexdigest(), "patient")
        success, result = controller.login()
        if success:
            availableOptions = ["103"]
            print("Patient logged in successfully.")
        else:
            print(result)

    # Log out
    elif option == "103":
        controller.logout()
        availableOptions = ["101", "102", "201", "202"]
        print("User logged out")

    # Log in hospital staff
    elif option == "202":
        print("Log in hospital staff")
        username = input("Username : ").strip()
        while not Validation.validUsername(username):
            print("Username is invalid. (username must have at least 4 character)")
            username = input("Username : ").strip()
        password = input("Password : ").strip()
        password = hashlib.md5(password.encode())
        controller = Model(username, password.hexdigest(), "hospital staff")
        success, result = controller.login()
        if success:
            availableOptions = [
                "103",
                "211",
                "212",
                "213",
                "214",
                "221",
                "222",
                "223",
                "224",
                "231",
                "232",
                "233",
                "234",
                "241",
                "242",
                "243",
                "244",
            ]
            print("Hospital staff logged in successfully.")
        else:
            print(result)

    # Add personal details
    elif option == "211":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Add personal details")
            username = input("Username : ").strip()
            details = input("Description : ").strip()
            optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            while optionManualSensitivity not in ["y", "n"]:
                print("Enter y (yes) or N (no)")
                optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            if optionManualSensitivity == "y":
                print(
                    "Enter the numbers as a sequence for privileges need to give as sensitivity (Example Read "
                    "Sensitivity : 234 for giving reading privilege to Receptionist, pharmacist and lab technician")
                print("6 - Doctor")
                print("5 - Nurse")
                print("4 - LabTechnician")
                print("3 - Pharmacist")
                print("2 - Receptionist")
                print("1 - Attendant")
                read = input("Read Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(read):
                    print('Enter valid privilege number sequence')
                    read = input("Read Sensitivity : ").strip()
                read += "9"
                write = input("Write Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(write):
                    print('Enter valid privilege number sequence')
                    write = input("Write Sensitivity : ").strip()
                write += "9"
                success, result = controller.addPersonalDetails(username, details, read, write)
            else:
                success, result = controller.addPersonalDetails(username, details)
            if success:
                print("Personal details added.")
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no personal details section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a receptionist.")
                else:
                    print("An error occurred. Please try again.")

    # Add sickness details
    elif option == "212":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Add sickness details")
            username = input("Username : ").strip()
            details = input("Description : ").strip()
            optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            while optionManualSensitivity not in ["y", "n"]:
                print("Enter y (yes) or N (no)")
                optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            if optionManualSensitivity == "y":
                print(
                    "Enter the numbers as a sequence for privileges need to give as sensitivity (Example Read "
                    "Sensitivity : 234 for giving reading privilege to Receptionist, pharmacist and lab technician")
                print("6 - Doctor")
                print("5 - Nurse")
                print("4 - LabTechnician")
                print("3 - Pharmacist")
                print("2 - Receptionist")
                print("1 - Attendant")
                read = input("Read Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(read):
                    print('Enter valid privilege number sequence')
                    read = input("Read Sensitivity : ").strip()
                read += "9"
                write = input("Write Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(write):
                    print('Enter valid privilege number sequence')
                    write = input("Write Sensitivity : ").strip()
                write += "9"
                success, result = controller.addSicknessDetails(username, details, read, write)
            else:
                success, result = controller.addSicknessDetails(username, details)
            if success:
                print("Sickness details added.")
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no sickness details section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a nurse.")
                else:
                    print("An error occurred. Please try again.")

    # Add drug prescription
    elif option == "213":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Add drug prescriptions")
            username = input("Username : ").strip()
            details = input("Description : ").strip()
            optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            while optionManualSensitivity not in ["y", "n"]:
                print("Enter y (yes) or N (no)")
                optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            if optionManualSensitivity == "y":
                print(
                    "Enter the numbers as a sequence for privileges need to give as sensitivity (Example Read "
                    "Sensitivity : 234 for giving reading privilege to Receptionist, pharmacist and lab technician")
                print("6 - Doctor")
                print("5 - Nurse")
                print("4 - LabTechnician")
                print("3 - Pharmacist")
                print("2 - Receptionist")
                print("1 - Attendant")
                read = input("Read Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(read):
                    print('Enter valid privilege number sequence')
                    read = input("Read Sensitivity : ").strip()
                read += "9"
                write = input("Write Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(write):
                    print('Enter valid privilege number sequence')
                    write = input("Write Sensitivity : ").strip()
                write += "9"
                success, result = controller.addDrugPrescription(username, details, read, write)
            else:
                success, result = controller.addDrugPrescription(username, details)
            if success:
                print("Drug prescription added.")
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no drug prescription section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a pharmacist.")
                else:
                    print("An error occurred. Please try again.")

    # Add lab test prescription
    elif option == "214":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Add Lab Test prescriptions")
            username = input("Username : ").strip()
            details = input("Description : ").strip()
            optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            while optionManualSensitivity not in ["y", "n"]:
                print("Enter y (yes) or N (no)")
                optionManualSensitivity = input("Set manual sensitivity (y/N) : ").strip().lower()
            if optionManualSensitivity == "y":
                print(
                    "Enter the numbers as a sequence for privileges need to give as sensitivity (Example Read "
                    "Sensitivity : 234 for giving reading privilege to Receptionist, pharmacist and lab technician")
                print("6 - Doctor")
                print("5 - Nurse")
                print("4 - LabTechnician")
                print("3 - Pharmacist")
                print("2 - Receptionist")
                print("1 - Attendant")
                read = input("Read Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(read):
                    print('Enter valid privilege number sequence')
                    read = input("Read Sensitivity : ").strip()
                read += "9"
                write = input("Write Sensitivity : ").strip()
                while not Validation.validSensitivitySeq(write):
                    print('Enter valid privilege number sequence')
                    write = input("Write Sensitivity : ").strip()
                write += "9"
                success, result = controller.addLabTestPrescription(username, details, read,
                                                                    write)
            else:
                success, result = controller.addLabTestPrescription(username, details)
            if success:
                print("Lab test prescription added.")
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no lab test prescription section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a lab technician.")
                else:
                    print("An error occurred. Please try again.")

    # View Personal Details
    elif option == "221":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("View Personal Details")
            username = input("Username : ").strip()
            success, result = controller.viewPersonalDetails(username)
            if success:
                if len(result) == 0:
                    print("There are no personal details records.")
                else:
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no personal details section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a receptionist.")
                else:
                    print("An error occurred. Please try again.")

    # View Sickness Details
    elif option == "222":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("View Sickness Details")
            username = input("Username : ").strip()
            success, result = controller.viewSicknessDetails(username)
            if success:
                if len(result) == 0:
                    print("There are no sickness details records.")
                else:
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no sickness details section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a nurse.")
                else:
                    print("An error occurred. Please try again.")

    # View Drug Prescriptions
    elif option == "223":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("View Drug Prescriptions")
            username = input("Username : ").strip()
            success, result = controller.viewDrugPrescription(username)
            if success:
                if len(result) == 0:
                    print("There are no drug prescriptions records.")
                else:
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no drug prescriptions section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact the pharmacist.")
                else:
                    print("An error occurred. Please try again.")

    # View Lab Test Prescriptions
    elif option == "224":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("View Lab Test Prescriptions")
            username = input("Username : ").strip()
            success, result = controller.viewLabTestPrescription(username)
            if success:
                if len(result) == 0:
                    print("There are no lab test prescriptions records.")
                else:
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
            else:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no lab test prescriptions section for given user.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact the lab technician.")
                else:
                    print("An error occurred. Please try again.")

    # Edit Personal Details
    elif option == "231":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Edit Personal Details")
            username = input("Username : ").strip()
            success, result = controller.viewPersonalDetails(username)
            if success:
                if len(result) == 0:
                    print("There are no personal details records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to modify( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    modifiedDesc = input("Enter Description : ").strip()
                    modifiedData = {"desc": modifiedDesc, 'id': recordId}
                    success, result = controller.editPersonalDetails(username, modifiedData)
                    if success:
                        print("Data record edited.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no personal details section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a receptionist.")
                else:
                    print("An error occurred. Please try again.")

    # Edit Sickness Details
    elif option == "232":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Edit Sickness Details")
            username = input("Username : ").strip()
            success, result = controller.viewSicknessDetails(username)
            if success:
                if len(result) == 0:
                    print("There are no sickness details records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to modify( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    modifiedDesc = input("Enter Description : ").strip()
                    modifiedData = {"desc": modifiedDesc, 'id': recordId}
                    success, result = controller.editSicknessDetails(username, modifiedData)
                    if success:
                        print("Data record edited.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no Sickness details section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a nurse.")
                else:
                    print("An error occurred. Please try again.")

    # Edit Drug Prescriptions
    elif option == "233":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Edit Drug Prescription")
            username = input("Username : ").strip()
            success, result = controller.viewDrugPrescription(username)
            if success:
                if len(result) == 0:
                    print("There are no Drug Prescription records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to modify( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    modifiedDesc = input("Enter Description : ").strip()
                    modifiedData = {"desc": modifiedDesc, 'id': recordId}
                    success, result = controller.editDrugPrescription(username, modifiedData)
                    if success:
                        print("Data record edited.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no Drug Prescription section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact the pharmacist.")
                else:
                    print("An error occurred. Please try again.")

    # Edit LabTest Prescriptions
    elif option == "234":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Edit Lab Test Prescription")
            username = input("Username : ").strip()
            success, result = controller.viewLabTestPrescription(username)
            if success:
                if len(result) == 0:
                    print("There are no Lab Test Prescription records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to modify( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    modifiedDesc = input("Enter Description : ").strip()
                    modifiedData = {"desc": modifiedDesc, 'id': recordId}
                    success, result = controller.editLabTestPrescription(username, modifiedData)
                    if success:
                        print("Data record edited.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no Lab Test Prescription section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact the lab test technician.")
                else:
                    print("An error occurred. Please try again.")

    # Delete Personal Information Record
    elif option == "241":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Delete Personal Detail")
            username = input("Username : ").strip()
            success, result = controller.viewPersonalDetails(username)
            if success:
                if len(result) == 0:
                    print("There are no personal details records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to delete( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    success, result = controller.deletePersonalDetails(username, recordId)
                    if success:
                        print("Data record deleted.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no personal details section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a receptionist.")
                else:
                    print("An error occurred. Please try again.")

    # Delete Sickness Information Record
    elif option == "242":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Delete Sickness Detail")
            username = input("Username : ").strip()
            success, result = controller.viewSicknessDetails(username)
            if success:
                if len(result) == 0:
                    print("There are no Sickness details records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to delete( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    success, result = controller.deleteSicknessDetails(username, recordId)
                    if success:
                        print("Data record deleted.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no Sickness details section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a nurse.")
                else:
                    print("An error occurred. Please try again.")

    # Delete drug prescription Record
    elif option == "243":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Delete Drug Prescription")
            username = input("Username : ").strip()
            success, result = controller.viewDrugPrescription(username)
            if success:
                if len(result) == 0:
                    print("There are no drug prescription records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to delete( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    success, result = controller.deleteDrugPrescription(username, recordId)
                    if success:
                        print("Data record deleted.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no drug prescription section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a nurse.")
                else:
                    print("An error occurred. Please try again.")

    # Delete Lab Test prescription Record
    elif option == "244":
        if controller is None or not controller.isLoggedIn:
            print("You need to be logged in.")
        else:
            print("Delete Lab Test Description")
            username = input("Username : ").strip()
            success, result = controller.viewLabTestPrescription(username)
            if success:
                if len(result) == 0:
                    print("There are no Lab Test prescription records.")
                else:
                    recordIds = []
                    for record in result:
                        print("Record id : %s \n %s " % (record["id"], record["desc"]))
                        recordIds.append(record["id"])
                    print("Enter the ids of records you need to delete( e.g. Record id : 3)")
                    recordId = input("Record id : ").strip()
                    while recordId not in recordIds:
                        print("Enter a valid record id")
                        recordId = input("Record id : ").strip()
                    success, result = controller.deleteLabTestPrescription(username, recordId)
                    if success:
                        print("Data record deleted.")
            if not success:
                if result == "not log in":
                    print("You need to be logged in.")
                elif result == "no user":
                    print("There is no user exists for given username.")
                elif result == "no section":
                    print("There is no Lab Test prescription section for given user.")
                elif result == "no record":
                    print("There is no available record for given record id.")
                elif result == "not authorized":
                    print("Action is not authorized. Contact a nurse.")
                else:
                    print("An error occurred. Please try again.")

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
