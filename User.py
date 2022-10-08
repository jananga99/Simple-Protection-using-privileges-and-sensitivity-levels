import xml.etree.ElementTree as ET
import Validation as validation

configurationFile = 'conf.xml'
configurationTree = ET.parse(configurationFile)
configurationRoot = configurationTree.getroot()

dataFile = 'data.xml'
dataTree = ET.parse(dataFile)
dataRoot = dataTree.getroot()


class User:

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

    def findUserTag(self):
        for userRoot in configurationRoot:
            if userRoot.find('Username').text == self.username and userRoot.find('Password').text and userRoot.find(
                    'Usertype').text == self.usertype:
                return True, userRoot
        return False, None

    def findUserDataTag(self):
        if not self.isLoggedIn:
            raise Exception("Tried to access user data when no user is logged in.")
        for userDataRoot in dataRoot:
            if userDataRoot.find('Username').text == self.username:
                return True, userDataRoot
        return False, None

    def login(self):
        if self.isLoggedIn:
            return False, "User already logged in."
        for userRoot in configurationRoot:
            if self.findUserTag()[0]:
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
        success, userDataRoot = self.findUserDataTag()
        if not success:
            raise Exception("No user data found for this user.")
        subDataRoot = userDataRoot.find('PersonalDetails')
        if subDataRoot is None:
            raise Exception("No personal details for user data")
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
        success, userDataRoot = self.findUserDataTag()
        if not success:
            raise Exception("No user data found for this user.")
        subDataRoot = userDataRoot.find('SicknessDetails')
        if subDataRoot is None:
            raise Exception("No sickness details for user data")
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
        success, userDataRoot = self.findUserDataTag()
        if not success:
            raise Exception("No user data found for this user.")
        subDataRoot = userDataRoot.find('DrugPrescription')
        if subDataRoot is None:
            raise Exception("No Drug Prescriptions for user data")
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
        success, userDataRoot = self.findUserDataTag()
        if not success:
            raise Exception("No user data found for this user.")
        subDataRoot = userDataRoot.find('LabTestPrescription')
        if subDataRoot is None:
            raise Exception("No Lab Test Prescriptions for user data")
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
