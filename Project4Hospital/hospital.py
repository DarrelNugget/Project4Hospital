#Project 4 Hospital Classes

class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def set_doctor_id(self, newID):
        self.doctor_id = newID
    
    def get_doctor_id(self):
        return self.doctor_id
    
    def set_name(self, newName):
        self.name = newName
    
    def get_name(self):
        return self.name
    
    def set_specialization(self, newSpecialization):
        self.specialization = newSpecialization
    
    def get_specialization(self):
        return self.specialization
    
    def set_working_time(self, newWorkingTime):
        self.working_time = newWorkingTime

    def get_working_time(self):
        return self.working_time
    
    def set_qualification(self, newqualifcation):
        self.qualification = newqualifcation
    
    def get_qualification(self):
        return self.qualification
    
    def set_room_number(self, newRoomNumber):
        self.room_number = newRoomNumber

    def get_room_number(self):
        return self.room_number
    
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

class doctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return str(doctor)

    def enter_dr_info(self):
        doctor_id = input("Enter doctor ID: ")
        name = input("Enter doctor name: ")
        specialization = input("Enter doctor specialization: ")
        working_time = input("Enter doctor working time: ")
        qualification = input("Enter doctor qualification: ")
        room_number = input("Enter doctor room number: ")
        return Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
        
    def read_doctors_file(self):
        with open("doctors.txt", "r") as flie:
            lines = flie.readlines()
            for line in lines:
                parts = line.strip().split("_")
                doctor_id, name, specialization, working_time, qualification, room_number = parts
                doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
                self.doctors.append(doctor)
                
           
    def search_doctor_by_id(self):
        doctor_id = input("Enter doctor ID: ")
        found = False
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                print(doctor)
                found = True
                break
        if found == False:
            print("Can't find the doctor with that ID.")   


    def search_doctor_by_name(self):
        name = input("Enter doctor name: ")
        for doctor in self.doctors:
            if doctor.get_name() == name:
                print(doctor)
                found = True
                break
        if found == False:
            print("Can't find the doctor with that name.")
    
        if (choice == 1): #doctor submenu
            print#placeholders


        elif(choice == 2):#patient submenu
            print#placeholders


        elif(choice == 3):#exits the program
            break

        else:#invalid inout message
            print('thats not a valid input please try again')

