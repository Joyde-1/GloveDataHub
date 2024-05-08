import time

from user_data import UserData
from duration_time import DurationTime
from manage_exe import ManageExe

class ManageMain:
    def __init__(self):
        self.user_data = UserData()
        self.duration_time = DurationTime()
        self.exe_manager = ManageExe()

    def display_welcome_screen(self):
        print("Welcome to the NOVA Gloves Data Acquisition System \n")
        input("Press Enter to continue...")
        print("\n")

    def start_calibration_screen(self):
        print("Calibration starting... \n")
        # TODO: Add run_sensecom
        input("Press Enter to continue...")
        print("\n")
        print("Calibration completed \n")

    def data_entry_screen(self):
        print("Please enter user data to proceed:\n")
        while(True):
            try:
                name = input("Enter Name: ")
                print("\n")
                self.user_data.set_name(name)
                break
            except ValueError:
                print("Enter a valid Name! \n")

        while(True):    
            try:
                surname = input("Enter Surname: ")
                print("\n")
                self.user_data.set_surname(surname)
                break
            except ValueError:
                print("Enter a valid Surname! \n")

        while(True):
            try:
                time_min = int(input("Enter Duration Time (in minutes): "))
                print("\n")
                self.duration_time.set_time_min(time_min)
                break
            except ValueError:
                print("Enter a valid Time! \n")

        path_directory = input("Enter Directory Path to Save Data: ")
        print("\n")
        self.user_data.set_path_directory(path_directory)

        path_csv = self.user_data.create_path_csv()
        print(f"Data saved in {path_csv} \n")

        input("Press Enter to continue...")
        print("\n")

    def data_acquisition_screen(self):
        start_time = time.time()

        print("Data acquisition in progress...\n")

        current_time = time.time() - start_time
        while(self.duration_time.check_time(current_time)):
            current_time = time.time() - start_time

            if current_time % 5 == 0:
                print(f"Current Time: {current_time} \n")

        print("Data acquisition completed \n")
        input("Press Enter to continue...")
        print("\n")

    def repeat_or_close_screen(self):
        while True:
            choice = input("\nPress R to repeat measurement or Q to quit the program: ").upper()
            if choice == 'R':
                return choice
            elif choice == 'Q':
                print("Exiting the program \n")
                return choice
            else:
                print("Invalid input, please choose 'R' to repeat or 'Q' to quit")