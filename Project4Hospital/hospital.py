#Project 4 Hospital Classes

class Doctor:
    def __init__(self, doctorID, name, specialization, workingTime, qualification, roomNumber):
        self.doctorID = doctorID
        self.name = name
        self.specialization = specialization
        self.workingTime = workingTime
        self.qualification = qualification
        self.rooomNumber = roomNumber

    def setDoctorID(self, newID):
        self.doctorID = newID
    
    def getDoctorID(self):
        return self.doctorID
    
    def setName(self, newName):
        self.name = newName
    
    def getName(self):
        return self.name
    
        
        
