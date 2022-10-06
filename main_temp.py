import xml.etree.ElementTree as ET

from PersonalDetails import PersonalDetails

tree = ET.parse('data.xml')
root = tree.getroot()

#obj = PersonalDetails("-1", "James", "34", "male", "washinton")
#obj.createTag(root)
obj = PersonalDetails.readTag(PersonalDetails.findTag(root, '0'))
#obj.name = "Mgonal"
#print(obj)
#obj.modifyTag(root)
obj.deleteTag(root)
tree.write("data.xml")

