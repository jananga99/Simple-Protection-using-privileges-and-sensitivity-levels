import xml.etree.ElementTree as ET

class User:

    def __init__(self, username, password, usertype, privilege):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.privilege = privilege

    @staticmethod
    def readTag(userTag):
        if userTag.tag != "user":
            raise Exception(userTag.tag + " is not a tag of type user.")
        elif userTag.find("username") is None or userTag.find("password") is None or userTag.find(
                "usertype") is None or userTag.find("privilege") is None:
            raise Exception("User tag does not have all necessary data tags.")
        else:
            return User(userTag.find("username").text, userTag.find("password").text, userTag.find("usertype").text,
                        userTag.find("privilege").text)

    def findTag(self, root):
        for r in root:
            if r.find('username').text == self.username:
                return r
        return None

    def createTag(self, root):
        r = self.findTag(root)
        if r is not None:
            raise Exception("Same username exists")
        new = ET.SubElement(root, 'user')
        ET.SubElement(new, 'username').text = self.username
        ET.SubElement(new, 'password').text = self.password
        ET.SubElement(new, 'usertype').text = self.usertype
        ET.SubElement(new, 'privilege').text = self.privilege
        return new

    def modifyTag(self, root):
        r = self.findTag(root)
        if r is None:
            raise Exception("user XML tag is not found for root tag, " + root.tag)
        r.find('username').text = self.username
        r.find('password').text = self.password
        r.find('usertype').text = self.usertype
        r.find('privilege').text = self.privilege

    def deleteTag(self, root):
        r = self.findTag(root)
        if r is None:
            raise Exception("user XML tag is not found for root tag " + root)
        root.remove(self.findTag(root))