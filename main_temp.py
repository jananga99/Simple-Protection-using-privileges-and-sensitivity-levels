

from User import User


user = User("a", "a", "patient")
#user.register()
#success, msg = user.login()
#print(success)
#print(msg)

success, msg = user.logout()
print(success)
print(msg)
