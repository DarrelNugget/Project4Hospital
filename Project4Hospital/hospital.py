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
        return f'{self.doctorID}_{self.name}_{self.specialization}_{self.workingTime}_{self.qualification}_{self.roomNumber}'



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
