import clr
from Autodesk.Revit.DB import Workset, Transaction

def set_vars():
    print("Aanmaken variabelen")
    worksets = []
    worksets.append("Elektro installaties")
    worksets.append("Klimaat Installaties")
    worksets.append("Ruimtereservering")
    worksets.append("Sanitaire installaties")
    worksets.append("Verlichting")
    worksets.append("Bouwkundig")
    worksets.append("nulpunt")
    return worksets

def create_worksets(worksets=None):
    print("Aanmaken worksets")
    t = Transaction(doc)
    t.Start("Create Workset")
    for each in worksets:
        try:
            Workset.Create(doc, each)
            print("- {0}".format(each))
        except:
            print("- {0} bestaat al".format(each))
            pass
    t.Commit()

print(" ")
clr.AddReference("RevitAPI")
doc = __revit__.ActiveUIDocument.Document
worksets = set_vars()
create_worksets(worksets)
print("klaar")
