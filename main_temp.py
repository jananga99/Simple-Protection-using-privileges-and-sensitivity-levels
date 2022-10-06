import xml.etree.ElementTree as ET

from DrugPrescription import DrugPrescription
from LabTestPrescription import LabTestPrescription
from PersonalDetails import PersonalDetails
from SicknessDetails import SicknessDetails

tree = ET.parse('data.xml')
root = tree.getroot()

# obj = PersonalDetails("-1", "James", "34", "male", "washinton")
# obj = PersonalDetails.readTag(PersonalDetails.findTag(root, '3'))
# obj.name = "Jesse"

# obj = SicknessDetails("-1", "0", "Maleria", "Very severe situation")
# obj = SicknessDetails.readTag(SicknessDetails.findTag(root, '2'))
# obj.name = "Dengue"

# obj = DrugPrescription("-1", "0", "ERT", "Do not use often", 4)
# obj = DrugPrescription.readTag(DrugPrescription.findTag(root, '0'))
# obj.name = "PRBG*"

#obj = LabTestPrescription("-1", "0", "PET-SCAN", "Dangerous", 3)
#obj = LabTestPrescription.readTag(LabTestPrescription.findTag(root, '0'))
#obj.name = "VR"


#print(obj)
#obj.createTag(root)
#obj.modifyTag(root)
#ET.indent(tree, '  ')
#obj.deleteTag(root)

a = input().strip()

print(a == '')

tree.write("data.xml")
