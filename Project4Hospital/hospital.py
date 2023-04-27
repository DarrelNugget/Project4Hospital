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
        
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid
    
    def get_name(self):
        return self.name
    
    def get_disease(self):
        return self.disease
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def set_pid(self, new_pid):
        self.pid = new_pid

    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"
    
class PatientManager:
    def __init__(self):
        self.patients = []

    def format_patient_info_for_file(self, patient):
        return f"{patient.get_pid}\t{patient.get_name}\t{patient.get_disease}\t{patient.get_gender}\t{patient.get_age}"

    # Helper method to enter patient info
    def enter_patient_info(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient Gender: ")
        age = input("Enter Patient Age: ")
        return Patient(pid, name, disease, gender, age)

    # Helper method to read patients data from file
    def read_patientsfile(self):
        with open("Project\Project Work\Project4Hospital\Project4Hospital\patients.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split("_")
                pid, name, disease, gender, age = parts
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)

    # Search patient by ID
    def search_patient_by_id(self):
        pid = input("Enter Patient ID: ")
        found = False
        for patient in self.patients:
            if patient.get_pid() == pid:
                print("ID\tName\tDisease\tGender\tAge")
                new_patient = str(patient)
                print(new_patient.replace('_', '\t'))
                found = True
                break
        if not found:
            print("Can't find the patient with the entered ID.")

    # Display patient info
    def display_patient_info(self, patient):
        print("ID\tName\tDisease\tGender\tAge")
        print(patient)

    def edit_patient_info_by_id(self):
        id = input("Enter patient ID to edit: ")
        for patient in self.patients:
            if patient.get_pid() == id:
                name = input("Enter the new name: ")
                disease = input("Enter the new disease: ")
                gender = input("Enter the new gender: ")
                age = input("Enter the new age: ")

                patient.set_name(name)
                patient.set_disease(disease)
                patient.set_gender(gender)
                patient.set_age(age)

                self.write_list_of_patients_to_file()

                print(f"Patient whose ID is {id} has been edited.")
                return
        print("Cannot find the doctor...")

    def display_patients_list(self):
        print("ID\tName\tDisease\tGender\tAge")
        for patient in self.patients[1:]:
            new_patient = str(patient)
            print(new_patient.replace('_', '\t'))

    def write_list_of_patients_to_file(self):
        with open("Project\Project Work\Project4Hospital\Project4Hospital\patients.txt", 'w') as file:
            for patient in self.patients[0:]:
                file.write(self.format_patient_info_for_file(patient) + "\n")
                file.close()

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        file = open("Project\Project Work\Project4Hospital\Project4Hospital\patients.txt",'a')
        file.write('\n')
        new_patient_string = str(new_patient)
        file.write(new_patient_string)
        file.close()
        print(f"Patient whose ID is {new_patient_string[:2]} has been added")