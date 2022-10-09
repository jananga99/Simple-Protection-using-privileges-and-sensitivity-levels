def validUsername(data):
    return data.isalnum()


def validPassword(data):
    return len(data) >= 8


def validSensitivity(data):
    return data in ["1", "2", "3", "4", "5", "6", "9"]


def validSensitivitySeq(data):
    for _ in data:
        if not validSensitivity(_):
            return False
    return True
