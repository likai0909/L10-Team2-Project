class Laptop():
# Refactor (E): Extract duplicate attributes and methods.
# There are several common attributes and methods in
# Camera.py and Laptop.py. Extract these common attributes
# and methods into a super class, named item.py
    def __init__(self, assetTag, description, os):
        self._assetTag = assetTag
        self._description = description
        self._dueDate = ""
        self._isAvailable = True
        self._os = os
    def getAssetTag(self):
        return self._assetTag
    def getDescription(self):
        return self._description
    def getDueDate(self):
        return self._dueDate
    def getIsAvailable(self):
        if self._isAvailable:
            return "Yes"
        else:
            return "No"
    def getOS(self):
        return self._os

    def setDueDate(self, dueDate):
        self._dueDate = dueDate
        
    def setIsAvailable(self, isAvailable):
        self._isAvailable = isAvailable
        
    def loanAsset(self, assetTag, dueDate):
        success = False
        if len(assetTag) > 0 and len(dueDate) > 0:
            foundAsset = self.findAsset(assetTag)
            if foundAsset != None:
                if foundAsset.getIsAvailable() == "Yes":
                    foundAsset.setIsAvailable(False)
                    foundAsset.setDueDate(dueDate)
                    success = True
        return success
            
    def loanCamera(self, assetTag, dueDate):
        return self.loanAsset(assetTag, dueDate)
        
    def loanLaptop(self, assetTag, dueDate):
        return self.loanAsset(assetTag, dueDate)
    
    def returnCamera(self, assetTag):
        return self.returnAsset(assetTag)
        
    def returnLaptop(self, assetTag):
        return self.returnAsset(assetTag)
    
    def returnAsset(self, assetTag):
        success = False
        if len(assetTag) > 0:
            foundAsset = self.findAsset(assetTag)
            if foundAsset != None:
                if foundAsset.getIsAvailable() == "No":
                    foundAsset.setIsAvailable(True)
                    foundAsset.setDueDate("")
                    success = True
        return success
        


