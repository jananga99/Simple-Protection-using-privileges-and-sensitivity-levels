import xml.etree.ElementTree as ET

from PersonalDetails import PersonalDetails
from SicknessDetails import SicknessDetails

tree = ET.parse('data.xml')
root = tree.getroot()

#obj = PersonalDetails("-1", "James", "34", "male", "washinton")

obj = SicknessDetails("-1", "0", "Maleria", "Very severe situation")
obj.createTag(root)
ET.indent(tree, '  ')
#obj = SicknessDetails.readTag(SicknessDetails.findTag(root, '2'))
#obj = PersonalDetails.readTag(PersonalDetails.findTag(root, '3'))
#print(obj)
#obj.name = "Jesse"
#obj.name = "Dengue"
#print(obj)
#obj.modifyTag(root)
#obj.deleteTag(root)
tree.write("data.xml")

