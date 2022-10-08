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

        newData = ET.SubElement(dataRoot, 'User')
        ET.SubElement(new, 'Username').text = self.username
        ET.SubElement(newData, 'PersonalDetails')
        ET.SubElement(newData, 'SicknessDetails')
        ET.SubElement(newData, 'LabTestPrescription')
        ET.SubElement(newData, 'DrugPrescription')
        ET.indent(dataTree, '  ')
        dataTree.write(dataFile)

    def login(self):
        if self.isLoggedIn:
            return False, "User already logged in."
        for userRoot in configurationRoot:
            if userRoot.find('Username').text == self.username and userRoot.find('Password').text and userRoot.find('Usertype').text == self.usertype:
                self.isLoggedIn = True
                return True, "User logged in."
        return False, "Invalid username or password"

    def logout(self):
        if not self.isLoggedIn:
            return False, "User is not logged in."
        self.isLoggedIn = False
        return True, "User logged out."
