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
    

    def edit_doctor_info(self):
        id = input("Enter doctor ID to edit: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == id:
                name = input("Enter the new name: ")
                specialization = input("Enter the new specialization: ")
                working_time = input("Enter the new working time: ")
                qualification = input("Enter the new qualification: ")
                room_number = input("Enter the new room number: ")

                doctor.set_name(name)
                doctor.set_specialization(specialization)
                doctor.set_working_time(working_time)
                doctor.set_qualification(qualification)
                doctor.set_room_number(room_number)

                self.write_list_of_doctors_to_file()

                print("Doctor info edited successfully.")
                return
        print("Cannot find the doctor...")
        
    def display_doctors_list(self):
        for doctor in self.doctors[1:]:
            newdoctor = str(doctor)
            print(newdoctor.replace("_", "   "))

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as f:
            for doctor in self.doctors:
                f.write(self.format_dr_info(doctor) + "\n")
                
    def add_dr_to_file(self):
        doctor = self.enter_dr_info()
        self.doctors.append(doctor)
        with open("doctors.txt", "a") as f:
            f.write(self.format_dr_info(doctor) + "\n")
        print("New doctor added successfully!")

manager = doctorManager()

manager.read_doctors_file()
manager.display_doctors_list()





