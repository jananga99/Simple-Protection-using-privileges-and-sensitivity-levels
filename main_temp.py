

from User import User


user = User("a", "a", "patient")
#user.register()
success, result = user.login()
#print(success)
#print(msg)

success, result = user.addPersonalDetails("Moved to los angaleses")
print(success)
print(result)

success, result = user.addSicknessDetails("Man down , I repeat man down")
print(success)
print(result)

success, result = user.addDrugPrescription("KASIPPU")
print(success)
print(result)

success, result = user.addLabTestPrescription("Well crazy mf")
print(success)
print(result)



#success, msg = user.logout()
#print(success)
#print(msg)
