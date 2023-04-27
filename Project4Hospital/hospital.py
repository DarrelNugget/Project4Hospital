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
        
        class management_methods:

    # Define a function to display the main menu
    def display_main_menu():
        print('''Main Menu
        1. Doctors
        2. Patients
        3. Exit''')

    # Define a function to display the Doctors submenu
    def display_doctors_menu():
        print('''Doctors Menu
        1. Display doctors list
        2. Search for a doctor by ID
        3. Search for a doctor by name
        4. Add a new doctor
        5. Edit existing doctor information
        6. Return to main menu
        ''')

    # Define a function to display the Patients submenu
    def display_patients_menu():
        print('''Patients Menu
        1. Display patients list
        2. Search for a patient by ID
        3. Add a new patient
        4. Edit existing patient information
        5. Return to main menu
        ''')


    while True:
        display_main_menu()
        main_menu_choice = input('Enter your choice (1-3): ')

        if main_menu_choice == '1':
            while True:
                display_doctors_menu()
                choice = input('Enter your choice (1-6): ')

                if choice == '1':
                    #display_doctors()
                elif choice == '2':
                    #search_doctor_by_id()
                elif choice == '3':
                    #search_doctor_by_name()
                elif choice == '4':
                    #add_doctor()
                elif choice == '5':
                    #edit_doctor()
                elif choice == '6':
                    break
                else:
                    print('Invalid choice. Please try again.')

        elif main_menu_choice == '2':
            while True:
                display_patients_menu()
                choice = input('Enter your choice (1-5): ')

                if choice == '1':
                    #display_patients()
                elif choice == '2':
                    #search_patient_by_id()
                elif choice == '3':
                    #add_patient()
                elif choice == '4':
                    #edit_patient()
                elif choice == '5':
                    break
                else:
                    print('Invalid choice. Please try again.')

        elif main_menu_choice == '3':
            print('Exiting program...')
            break

        else:
            print('Invalid choice. Please try again.')
