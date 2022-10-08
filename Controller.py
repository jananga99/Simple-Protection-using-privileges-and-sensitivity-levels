import xml.etree.ElementTree as ET
import Validation as validation

configurationFile = 'conf.xml'
configurationTree = ET.parse(configurationFile)
configurationRoot = configurationTree.getroot()

dataFile = 'data.xml'
dataTree = ET.parse(dataFile)
dataRoot = dataTree.getroot()


class Controller:

    def __init__(self, username, password, usertype, privilege='0'):  # default privilege level
        self.username = username
        self.password = password
        self.usertype = usertype
        self.privilege = privilege
        self.isLoggedIn = False

    def register(self):
        if not validation.validUsername(self.username):
            return False, "Invalid username"
        elif not validation.validPassword(self.password):
            return False, "Invalid password"
        new = ET.SubElement(configurationRoot, 'User')
        ET.SubElement(new, 'Username').text = self.username
        ET.SubElement(new, 'Password').text = self.password
        ET.SubElement(new, 'Usertype').text = self.usertype
        ET.SubElement(new, 'Privilege').text = self.privilege
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

    def __findUserTag(self):
        for userRoot in configurationRoot:
            if userRoot.find('Username').text == self.username and userRoot.find('Password').text and userRoot.find(
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
        for _ in configurationRoot:
            if self.__findUserTag()[0]:
                self.isLoggedIn = True
                return True, self
        return False, "Invalid username or password"

    def logout(self):
        if not self.isLoggedIn:
            return False, None
        self.isLoggedIn = False
        return True, None

    def addPersonalDetails(self, data, sensitivity='0'):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(self.username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            return False, "No personal details for user data"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        ET.SubElement(new, 'sensitivity').text = sensitivity
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "sensitivity": sensitivity}

    def addSicknessDetails(self, data, sensitivity='0'):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(self.username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            return False, "No personal details for user data"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        ET.SubElement(new, 'sensitivity').text = sensitivity
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "sensitivity": sensitivity}

    def addDrugPrescription(self, data, sensitivity='0'):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(self.username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            return False, "No personal details for user data"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        ET.SubElement(new, 'sensitivity').text = sensitivity
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "sensitivity": sensitivity}

    def addLabTestPrescription(self, data, sensitivity='0'):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(self.username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            return False, "No personal details for user data"
        count = 0
        for _ in subDataRoot:
            count += 1
        new = ET.SubElement(subDataRoot, 'data')
        ET.SubElement(new, 'id').text = str(count)
        ET.SubElement(new, 'desc').text = data
        ET.SubElement(new, 'sensitivity').text = sensitivity
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)
        return True, {"id": str(count), "desc": data, "sensitivity": sensitivity}

    def viewPersonalDetails(self, username):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user exits for given username"
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            return False, "No personal details for username"
        retData = []
        for dataRecord in subDataRoot:
            retData.append(
                {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                 "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    def viewSicknessDetails(self, username):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user exits for given username"
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            raise Exception("No sickness details for username")
        retData = []
        for dataRecord in subDataRoot:
            retData.append(
                {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                 "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    def viewDrugPrescription(self, username):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user exits for given username"
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            return False, "No personal details for username"
        retData = []
        for dataRecord in subDataRoot:
            retData.append(
                {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                 "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    def viewLabTestPrescription(self, username):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user exits for given username"
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            return False, "No personal details for username"
        retData = []
        for dataRecord in subDataRoot:
            retData.append(
                {"id": dataRecord.find("id").text, "desc": dataRecord.find("desc").text,
                 "sensitivity": dataRecord.find("sensitivity").text})
        return True, retData

    def editPersonalDetails(self, username, data):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            return False, "No personal details for username"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"]:
                dataRecord.find("desc").text = data["desc"]
                dataRecord.find("sensitivity").text = data["sensitivity"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"], "sensitivity": data["sensitivity"]}
        return False, "No data record for given id"

    def editSicknessDetails(self, username, data):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            return False, "No sickness details for username"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"]:
                dataRecord.find("desc").text = data["desc"]
                dataRecord.find("sensitivity").text = data["sensitivity"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"], "sensitivity": data["sensitivity"]}
        return False, "No data record for given id"

    def editDrugPrescription(self, username, data):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            return False, "No drug prescription for username"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"]:
                dataRecord.find("desc").text = data["desc"]
                dataRecord.find("sensitivity").text = data["sensitivity"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"], "sensitivity": data["sensitivity"]}
        return False, "No data record for given id"

    def editLabTestPrescription(self, username, data):
        if not self.isLoggedIn:
            return False, "User not logged in."
        success, userDataRoot = self.__findUserDataTag(username)
        if not success:
            return False, "No user data found for this user."
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            return False, "No lab test prescription for username"
        for dataRecord in subDataRoot:
            if dataRecord.find("id").text == data["id"]:
                dataRecord.find("desc").text = data["desc"]
                dataRecord.find("sensitivity").text = data["sensitivity"]
                dataTree.write(dataFile)
                return True, {"id": data["id"], "desc": data["desc"], "sensitivity": data["sensitivity"]}
        return False, "No data record for given id"