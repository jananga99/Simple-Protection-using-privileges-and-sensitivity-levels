import xml.etree.ElementTree as ET


class LabTestPrescription:

    # tagId = '-1' for new object who not in XML yet
    def __init__(self, tagId, personalId, name, details='', sensitivity='2'):
        tagId = str(tagId)
        personalId = str(personalId)
        sensitivity = str(sensitivity)
        if not tagId.isnumeric() and tagId != "-1":
            raise Exception("Tag id must be an integer")
        if not personalId.isnumeric() and personalId != "-1":
            raise Exception("Personal id must be an integer")
        self.tagId = tagId
        self.personalId = personalId
        self.name = name
        self.details = details
        self.sensitivity = sensitivity

    def __str__(self):
        return "LabTestPrescription Object: %s, %s, %s, %s %s" % (
            self.tagId, self.personalId, self.name, self.details, self.sensitivity)

    @staticmethod
    def readTag(tag):
        if tag.tag != "labTestPrescription":
            raise Exception(tag.tag + " is not a tag of type labTestPrescription.")
        elif tag.find("tagId") is None or tag.find("name") is None or tag.find(
                "personalId") is None or tag.find("details" or tag.find("sensitivity")):
            raise Exception("Tag does not have all necessary data tags.")
        else:
            return LabTestPrescription(tag.find("tagId").text, tag.find('personalId').text, tag.find("name").text,
                                    tag.find("details").text, tag.find('sensitivity').text)

    @staticmethod
    def findTag(root, tagId):
        tagId = str(tagId)
        for r in root:
            if r.tag == "labTestPrescription" and r.find('tagId').text == tagId:
                return r
        return None

    def createTag(self, root):
        if root[0].tag != "header":
            raise Exception("Root tag does not contain a header")
        if root[0].find('nextIdLabTestPrescription') is None:
            raise Exception("Header does not contain nextId tag for this object type.")
        tagId = root[0].find('nextIdLabTestPrescription').text
        new = ET.SubElement(root, 'labTestPrescription')
        ET.SubElement(new, 'tagId').text = tagId
        ET.SubElement(new, 'personalId').text = self.personalId
        ET.SubElement(new, 'name').text = self.name
        ET.SubElement(new, 'details').text = self.details
        ET.SubElement(new, 'sensitivity').text = self.sensitivity
        root[0].find('nextIdLabTestPrescription').text = str(int(tagId) + 1)
        return new.find('tagId').text

    def modifyTag(self, root):
        r = LabTestPrescription.findTag(root, self.tagId)
        if r is None:
            raise Exception("labTestPrescription XML tag is not found for root tag, " + root.tag)
        r.find('personalId').text = self.personalId
        r.find('name').text = self.name
        r.find('details').text = self.details
        r.find('sensitivity').text = self.sensitivity

    def deleteTag(self, root):
        r = LabTestPrescription.findTag(root, self.tagId)
        if r is None:
            raise Exception("labTestPrescription XML tag is not found for root tag " + root)
        root.remove(LabTestPrescription.findTag(root, self.tagId))
