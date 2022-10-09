import xml.etree.ElementTree as ET

import Validation

# Configuration file
configurationFile = 'conf.xml'
configurationTree = ET.parse(configurationFile)
configurationRoot = configurationTree.getroot()

# Data file
dataFile = 'data.xml'
dataTree = ET.parse(dataFile)
dataRoot = dataTree.getroot()


class Model:
    # Hardcoded create and delete sensitivities
    createDeleteSensitivities = {
        "PersonalDetails": "29",
        "SicknessDetails": "69",
        "DrugPrescription": "369",
        "LabTestPrescription": "49",
    }

    def __init__(self, username, password, usertype):  # default privilege level
        self.username = username
        self.password = password
        self.usertype = usertype

        # Denotes the privilege of the logged in user.
        self.privilege = '0'

        # Denotes whether the user logged in or not
        self.isLoggedIn = False

    # Register the current user correspond to the object
    def register(self, privilege='0'):

        # User is added for configuration file.
        new = ET.SubElement(configurationRoot, 'User')
        ET.SubElement(new, 'Username').text = self.username
        ET.SubElement(new, 'Password').text = self.password
        ET.SubElement(new, 'Usertype').text = self.usertype
        ET.SubElement(new, 'Privilege').text = privilege
        ET.indent(configurationTree, '  ')
        configurationTree.write(configurationFile)

        # Empty user data is added to data file.
        newData = ET.SubElement(dataRoot, 'UserData')
        ET.SubElement(newData, 'Username').text = self.username
        ET.SubElement(newData, 'PersonalDetails')
        ET.SubElement(newData, 'SicknessDetails')
        ET.SubElement(newData, 'LabTestPrescription')
        ET.SubElement(newData, 'DrugPrescription')
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

        return True, {"username": self.username, "usertype": self.usertype, "privilege": privilege}

    # Finds the relevant user tag for given username from the configuration file
    def __findUserTag(self, username):
        for userRoot in configurationRoot:
            if userRoot.find('Username').text == username and userRoot.find('Password').text and userRoot.find(
                    'Usertype').text == self.usertype:
                return True, userRoot
        return False, None

    # Finds the relevant user tag for given username from the data file
    def __findUserDataTag(self, username):
        if not self.isLoggedIn:
            raise Exception("Tried to access user data when no user is logged in.")
        for userDataRoot in dataRoot:
            if userDataRoot.find('Username').text == username:
                return True, userDataRoot
        return False, None

    # Log in the current user of the object
    def login(self):
        if self.isLoggedIn:
            return False, "User already logged in."
        success, userRecord = self.__findUserTag(self.username)
        if success and userRecord.find('Password').text != self.password:
            success = False
        if success:
            # Sets the privilege level
            self.isLoggedIn = True
            self.privilege = userRecord.find('Privilege').text
            return True, self
        else:
            return False, "Invalid username or password"

    # Logs out the current user for object
    def logout(self):
        if not self.isLoggedIn:
            return False, None
        # privilege level is reset to default lowest level.
        self.privilege = '0'
        self.isLoggedIn = False
        return True, None

    # Adds given personal details.
    # Default sensitivities are defined if they are not passed.
    def addPersonalDetails(self, username, data, read='234569', write='269'):
        # Check whether the user is logged in or not
        if not self.isLoggedIn:
            return False, "not log in"
        # Checks the privilege level with sensitivities
        if self.privilege not in Model.createDeleteSensitivities["PersonalDetails"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        # If there is no user for given username
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('PersonalDetails')
        # If there is no personal details tag
        if subDataRoot is None:
            return False, "no section"
        count = 0
        for _ in subDataRoot:
            count += 1
        # Sets the personal details tag
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        sensitivityRoot = ET.SubElement(new, 'sensitivity')
        ET.SubElement(sensitivityRoot, 'read').text = read
        ET.SubElement(sensitivityRoot, 'write').text = write
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "read": read,
                      "write": write}

    # Adds given sickness details.
    # Default sensitivities are defined if they are not passed.
    def addSicknessDetails(self, username, data, read='34569', write='569'):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Model.createDeleteSensitivities["SicknessDetails"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            return False, "no user"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        sensitivityRoot = ET.SubElement(new, 'sensitivity')
        ET.SubElement(sensitivityRoot, 'read').text = read
        ET.SubElement(sensitivityRoot, 'write').text = write
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "read": read,
                      "write": write}

    # Adds given drug prescription.
    # Default sensitivities are defined if they are not passed.
    def addDrugPrescription(self, username, data, read='3569', write='369'):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Model.createDeleteSensitivities["DrugPrescription"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            return False, "no user"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        sensitivityRoot = ET.SubElement(new, 'sensitivity')
        ET.SubElement(sensitivityRoot, 'read').text = read
        ET.SubElement(sensitivityRoot, 'write').text = write
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "read": read,
                      "write": write}

    # Adds given lab test prescription.
    # Default sensitivities are defined if they are not passed.
    def addLabTestPrescription(self, username, data, read='469', write='469'):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Model.createDeleteSensitivities["LabTestPrescription"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            return False, "no user"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        sensitivityRoot = ET.SubElement(new, 'sensitivity')
        ET.SubElement(sensitivityRoot, 'read').text = read
        ET.SubElement(sensitivityRoot, 'write').text = write
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "read": read,
                      "write": write}

    # Returns personal details for given username.
    def viewPersonalDetails(self, username):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            return False, "no section"
        retData = []
        for dataRecord in subDataRoot:
            # Authentication using privilege and sensitivity levels
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'read').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    # Returns sickness details for given username.
    def viewSicknessDetails(self, username):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            return False, "section empty"
        retData = []
        for dataRecord in subDataRoot:
            # Authentication using privilege and sensitivity levels
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'read').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    # Returns drug prescription for given username.
    def viewDrugPrescription(self, username):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            return False, "no section"
        retData = []
        for dataRecord in subDataRoot:
            # Authentication using privilege and sensitivity levels
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'read').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    # Returns lab test prescription for given username.
    def viewLabTestPrescription(self, username):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            return False, "no section"
        retData = []
        for dataRecord in subDataRoot:
            # Authentication using privilege and sensitivity levels
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'read').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    # Edits personal details for given username using given data.
    def editPersonalDetails(self, username, data):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            return False, "no section"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"] and dataRecord.find("isDeleted").text == "False":
                # Authentication using privilege and sensitivity levels
                if self.privilege not in dataRecord.find('sensitivity').find('write').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

    # Edits personal details for given username using given data.
    def editSicknessDetails(self, username, data):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            return False, "no section"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"] and dataRecord.find("isDeleted").text == "False":
                # Authentication using privilege and sensitivity levels
                if self.privilege not in dataRecord.find('sensitivity').find('write').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

    # Edits drug prescriptions for given username using given data.
    def editDrugPrescription(self, username, data):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            return False, "no section"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"] and dataRecord.find("isDeleted").text == "False":
                # Authentication using privilege and sensitivity levels
                if self.privilege not in dataRecord.find('sensitivity').find('write').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

    # Edits lab test prescriptions for given username using given data.
    def editLabTestPrescription(self, username, data):
        if not self.isLoggedIn:
            return False, "not log in"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            return False, "no section"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"] and dataRecord.find("isDeleted").text == "False":
                # Authentication using privilege and sensitivity levels
                if self.privilege not in dataRecord.find('sensitivity').find('write').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

    # Deletes personal detail record for given username and id
    def deletePersonalDetails(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Model.createDeleteSensitivities["PersonalDetails"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            return False, "No personal details for user data"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == dataId and dataRecord.find("isDeleted").text == "False":
                dataRecord.find("isDeleted").text = "True"
                dataTree.write(dataFile)
                return True, {"id": dataId, "isDeleted": "True"}
        return False, "no record"

    # Deletes sickness detail record for given username and id
    def deleteSicknessDetails(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Model.createDeleteSensitivities["SicknessDetails"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            return False, "no user"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == dataId and dataRecord.find("isDeleted").text == "False":
                dataRecord.find("isDeleted").text = "True"
                dataTree.write(dataFile)
                return True, {"id": dataId, "isDeleted": "True"}
        return False, "no record"

    # Deletes drug prescription record for given username and id
    def deleteDrugPrescription(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Model.createDeleteSensitivities["DrugPrescription"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            return False, "no section"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == dataId and dataRecord.find("isDeleted").text == "False":
                dataRecord.find("isDeleted").text = "True"
                dataTree.write(dataFile)
                return True, {"id": dataId, "isDeleted": "True"}
        return False, "no record"

    # Deletes lab test prescription record for given username and id
    def deleteLabTestPrescription(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Model.createDeleteSensitivities["LabTestPrescription"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            return False, "No lab test prescription for user data"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == dataId and dataRecord.find("isDeleted").text == "False":
                dataRecord.find("isDeleted").text = "True"
                dataTree.write(dataFile)
                return True, {"id": dataId, "isDeleted": "True"}
        return False, "no record"
