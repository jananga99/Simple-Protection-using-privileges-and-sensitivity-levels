

from Model import Model


controller = Model("a", "a", "patient")
#user.register()
success, result = controller.login()
#print(success)
#print(msg)

"""
success, result = controller.deletePersonalDetails("a", "1")
print(success)
print(result)
success, result = controller.deleteSicknessDetails("a", "1")
print(success)
print(result)
success, result = controller.deleteDrugPrescription("a", "1")
print(success)
print(result)
success, result = controller.deleteLabTestPrescription("a", "1")
print(success)
print(result)
"""
"""
success, result = controller.editPersonalDetails("a", {"id":"0", "desc":"New Man I Am", "sensitivity":"5b"})
print(success)
print(result)
success, result = controller.editSicknessDetails("a", {"id":"10", "desc":"New Sickness I Am", "sensitivity":"5v"})
print(success)
print(result)
success, result = controller.editDrugPrescription("a", {"id":"0", "desc":"New Drug I Am", "sensitivity":"5r"})
print(success)
print(result)
success, result = controller.editLabTestPrescription("a", {"id":"0", "desc":"New Lab test I Am", "sensitivity":"5c"})
print(success)
print(result)
"""


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
