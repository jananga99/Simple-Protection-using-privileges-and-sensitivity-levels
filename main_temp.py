

from Controller import Controller


controller = Controller("a", "a", "patient")
#user.register()
success, result = controller.login()
#print(success)
#print(msg)

success, result = controller.editPersonalDetails("a", {"id":"0", "desc":"New Man I Am", "sensitivity":"5"})
print(success)
print(result)
success, result = controller.editSicknessDetails("a", {"id":"10", "desc":"New Sickness I Am", "sensitivity":"5"})
print(success)
print(result)
success, result = controller.editDrugPrescription("a", {"id":"0", "desc":"New Drug I Am", "sensitivity":"5"})
print(success)
print(result)
success, result = controller.editLabTestPrescription("a", {"id":"0", "desc":"New Lab test I Am", "sensitivity":"5"})
print(success)
print(result)



"""
success, result = controller.viewPersonalDetails("a")
print(success)
print(result)
success, result = controller.viewSicknessDetails("a")
print(success)
print(result)
success, result = controller.viewDrugPrescription("aa")
print(success)
print(result)
success, result = controller.viewLabTestPrescription("a")
print(success)
print(result)
"""

"""
success, result = controller.addPersonalDetails("Moved to los angaleses")
print(success)
print(result)

success, result = controller.addSicknessDetails("Man down , I repeat man down")
print(success)
print(result)

success, result = controller.addDrugPrescription("KASIPPU")
print(success)
print(result)

success, result = controller.addLabTestPrescription("Well crazy mf")
print(success)
print(result)
"""


#success, msg = user.logout()
#print(success)
#print(msg)
