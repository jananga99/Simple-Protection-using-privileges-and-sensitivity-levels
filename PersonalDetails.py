import xml.etree.ElementTree as ET


class PersonalDetails:

    # tagId = '-1' for new object who not in XML yet
    def __init__(self, tagId, name, age, gender, city, sensitivity='2'):
        tagId = str(tagId)
        age = str(age)
        sensitivity = str(sensitivity)
        if not tagId.isnumeric() and tagId != "-1":
            raise Exception("Tag id must be an integer")
        self.tagId = tagId
        self.name = name
        self.age = age
        if gender.lower() not in ('male', 'female'):
            raise Exception("Gender must be male or female.")
        self.gender = gender
        self.city = city
        self.sensitivity = sensitivity

    def __str__(self):
        return "Personal Object: %s, %s, %s, %s, %s, %s" % (
            self.tagId, self.name, self.age, self.gender, self.city, self.sensitivity)

    @staticmethod
    def readTag(tag):
        if tag.tag != "personalDetails":
            raise Exception(tag.tag + " is not a tag of type personalDetails.")
        elif tag.find("tagId") is None or tag.find("name") is None or tag.find(
                "age") is None or tag.find("gender") is None or tag.find("city"):
            raise Exception("Tag does not have all necessary data tags.")
        else:
            return PersonalDetails(tag.find("tagId").text, tag.find("name").text, tag.find("age").text,
                                   tag.find("gender").text, tag.find("city").text, tag.find('sensitivity').text)

    @staticmethod
    def findTag(root, tagId):
        tagId = str(tagId)
        for r in root:
            if r.tag == "personalDetails" and r.find('tagId').text == tagId:
                return r
        return None

    def createTag(self, root):
        if root[0].tag != "header":
            raise Exception("Root tag does not contain a header")
        if root[0].find('nextIdPersonalDetails') is None:
            raise Exception("Header does not contain nextId tag for this object type.")
        tagId = root[0].find('nextIdPersonalDetails').text
        new = ET.SubElement(root, 'personalDetails')
        ET.SubElement(new, 'tagId').text = tagId
        ET.SubElement(new, 'city').text = self.city
        ET.SubElement(new, 'name').text = self.name
        ET.SubElement(new, 'age').text = self.age
        ET.SubElement(new, 'gender').text = self.gender
        ET.SubElement(new, 'sensitivity').text = self.sensitivity
        root[0].find('nextIdPersonalDetails').text = str(int(tagId) + 1)
        return new.find('tagId').text

    def modifyTag(self, root):
        r = PersonalDetails.findTag(root, self.tagId)
        if r is None:
            raise Exception("personalDetails XML tag is not found for root tag, " + root.tag)
        r.find('name').text = self.name
        r.find('age').text = self.age
        r.find('gender').text = self.gender
        r.find('city').text = self.city
        r.find('sensitivity').text = self.sensitivity

    def deleteTag(self, root):
        r = PersonalDetails.findTag(root, self.tagId)
        if r is None:
            raise Exception("personalDetails XML tag is not found for root tag " + root)
        root.remove(PersonalDetails.findTag(root, self.tagId))
