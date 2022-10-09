import xml.etree.ElementTree as ET

import Validation

configurationFile = 'conf.xml'
configurationTree = ET.parse(configurationFile)
configurationRoot = configurationTree.getroot()

dataFile = 'data.xml'
dataTree = ET.parse(dataFile)
dataRoot = dataTree.getroot()


class Controller:
    createDeleteSensitivities = {
        "PersonalDetails": "26",
        "SicknessDetails": "56",
        "DrugPrescription": "36",
        "LabTestPrescription": "46",
    }

    def __init__(self, username, password, usertype):  # default privilege level
        self.username = username
        self.password = password
        self.usertype = usertype
        self.privilege = '0'
        self.isLoggedIn = False

    def register(self, privilege='0'):
        new = ET.SubElement(configurationRoot, 'User')
        ET.SubElement(new, 'Username').text = self.username
        ET.SubElement(new, 'Password').text = self.password
        ET.SubElement(new, 'Usertype').text = self.usertype
        ET.SubElement(new, 'Privilege').text = privilege
        ET.indent(configurationTree, '  ')
        configurationTree.write(configurationFile)

        newData = ET.SubElement(dataRoot, 'UserData')
        ET.SubElement(newData, 'Username').text = self.username
        ET.SubElement(newData, 'PersonalDetails')
        ET.SubElement(newData, 'SicknessDetails')
        ET.SubElement(newData, 'LabTestPrescription')
        ET.SubElement(newData, 'DrugPrescription')
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

        return True, {"username": self.username, "usertype": self.usertype, "privilege": privilege}

    def __findUserTag(self, username):
        for userRoot in configurationRoot:
            if userRoot.find('Username').text == username and userRoot.find('Password').text and userRoot.find(
                    'Usertype').text == self.usertype:
                return True, userRoot
        return False, None

    def __findUserDataTag(self, username):
        if not self.isLoggedIn:
            raise Exception("Tried to access user data when no user is logged in.")
        for userDataRoot in dataRoot:
            if userDataRoot.find('Username').text == username:
                return True, userDataRoot
        return False, None

    def login(self):
        if self.isLoggedIn:
            return False, "User already logged in."
        success, userRecord = self.__findUserTag(self.username)
        if success:
            self.isLoggedIn = True
            self.privilege = userRecord.find('Privilege').text
            return True, self
        else:
            return False, "Invalid username or password"

    def logout(self):
        if not self.isLoggedIn:
            return False, None
        self.privilege = '0'
        self.isLoggedIn = False
        return True, None

    def addPersonalDetails(self, username, data, readSensitivity='23456', writeSensitivity='26'):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["PersonalDetails"]:
            return False, "not authorized"
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "no user"
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            return False, "no section"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        sensitivityRoot = ET.SubElement(new, 'sensitivity')
        ET.SubElement(sensitivityRoot, 'read').text = readSensitivity
        ET.SubElement(sensitivityRoot, 'write').text = writeSensitivity
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "readSensitivity": readSensitivity,
                      "writeSensitivity": writeSensitivity}

    def addSicknessDetails(self, username, data, readSensitivity='3456', writeSensitivity='56'):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["SicknessDetails"]:
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
        ET.SubElement(sensitivityRoot, 'read').text = readSensitivity
        ET.SubElement(sensitivityRoot, 'write').text = writeSensitivity
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "readSensitivity": readSensitivity,
                      "writeSensitivity": writeSensitivity}

    def addDrugPrescription(self, username, data, readSensitivity='356', writeSensitivity='36'):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["DrugPrescription"]:
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
        ET.SubElement(sensitivityRoot, 'read').text = readSensitivity
        ET.SubElement(sensitivityRoot, 'write').text = writeSensitivity
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "readSensitivity": readSensitivity,
                      "writeSensitivity": writeSensitivity}

    def addLabTestPrescription(self, username, data, readSensitivity='46', writeSensitivity='46'):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["LabTestPrescription"]:
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
        ET.SubElement(sensitivityRoot, 'read').text = readSensitivity
        ET.SubElement(sensitivityRoot, 'write').text = writeSensitivity
        ET.SubElement(new, "isDeleted").text = str(False)
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "readSensitivity": readSensitivity,
                      "writeSensitivity": writeSensitivity}

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
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'readSensitivity').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

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
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'readSensitivity').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

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
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'readSensitivity').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

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
            if dataRecord.find("isDeleted").text == "False" and self.privilege in dataRecord.find('sensitivity').find(
                    'readSensitivity').text:
                retData.append(
                    {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                     "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

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
                if self.privilege not in dataRecord.find('sensitivity').find('writeSensitivity').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

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
                if self.privilege not in dataRecord.find('sensitivity').find('writeSensitivity').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

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
                if self.privilege not in dataRecord.find('sensitivity').find('writeSensitivity').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

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
                if self.privilege not in dataRecord.find('sensitivity').find('writeSensitivity').text:
                    return False, "not authorized"
                dataRecord.find("desc").text = data["desc"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"],
                              "sensitivity": dataRecord.find("sensitivity").text}
        return False, "no record"

    def deletePersonalDetails(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["PersonalDetails"]:
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

    def deleteSicknessDetails(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["SicknessDetails"]:
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

    def deleteDrugPrescription(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["DrugPrescription"]:
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

    def deleteLabTestPrescription(self, username, dataId):
        if not self.isLoggedIn:
            return False, "not log in"
        if self.privilege not in Controller.createDeleteSensitivities["LabTestPrescription"]:
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
