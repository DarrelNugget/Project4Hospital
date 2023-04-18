#Project 4 Hospital Classes

class Doctor:
    def __init__(self, doctorID, name, specialization, workingTime, qualification, roomNumber):
        self.doctorID = doctorID
        self.name = name
        self.specialization = specialization
        self.workingTime = workingTime
        self.qualification = qualification
        self.roomNumber = roomNumber

    def setDoctorID(self, newID):
        self.doctorID = newID
    
    def getDoctorID(self):
        return self.doctorID
    
    def setName(self, newName):
        self.name = newName
    
    def getName(self):
        return self.name
    
    def setSpecialization(self, newSpecialization):
        self.specialization = newSpecialization
    
    def getSpecialization(self):
        return self.specialization
    
    def setWorkingTime(self, newWorkingTime):
        self.workingTime = newWorkingTime

    def getWorkingTime(self):
        return self.workingTime
    
    def setQualification(self, newqualifcation):
        self.qualification = newqualifcation
    
    def getQualification(self):
        return self.qualification
    
    def setRoomNumber(self, newRoomNumber):
        self.roomNumber = newRoomNumber

    def getRoomNumber(self):
        return self.roomNumber
    
    def __str__(self):
        return f"{self.doctorID}_{self.name}_{self.specialization}_{self.workingTime}_{self.qualification}_{self.roomNumber}"



class management_methods:

    choice = input('''
please choose from the following options:
1-Doctors submenu
2-patients submenu
3-Exit the program''')

    while choice != 3:
    
        if (choice == 1): #doctor submenu
            print#placeholders


        elif(choice == 2):#patient submenu
            print#placeholders


        elif(choice == 3):#exits the program
            break

        else:#invalid inout message
            print('thats not a valid input please try again')

    