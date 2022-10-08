def validUsername(data):
    return data.isalnum()


def validPassword(data):
    return len(data) >= 8
