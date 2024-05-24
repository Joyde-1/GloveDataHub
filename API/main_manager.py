import time

from user_data import UserData
from duration_time import DurationTime
from exe_manager import ExeManager

class MainManager:
    """
    Class responsible for managing the main operations of the NOVA Gloves Data Acquisition System.

    Attributes
    ----------
    user_data : UserData 
        An instance of UserData for managing user data.
    duration_time (DurationTime): DurationTime
        An instance of DurationTime for managing duration time.
    exe_manager : ExeManager 
        An instance of ExeManager for executing system commands.
    """
    def __init__(self):
        """
        Constructor, initialize MainManager with instances of UserData, DurationTime, and ExeManager.
        """
        self.user_data = UserData()
        self.duration_time = DurationTime()
        self.exe_manager = ExeManager()

    def display_welcome_screen(self):
        """
        Display the welcome screen of the system.
        """
        print("Welcome to the NOVA Gloves Data Acquisition System \n")
        input("Press Enter to continue...")
        print("\n")

    def start_calibration_screen(self):
        """
        Display the calibration screen and start calibration.
        """
        print("Calibration starting... \n")
        self.exe_manager.start_sensecom()
        input("Press Enter to continue...")
        print("\n")
        print("Calibration completed \n")

    def data_entry_screen(self):
        """
        Display the data entry screen and prompt user to enter necessary data.
        """
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
        """
        Display the data acquisition screen and perform data acquisition.
        """
        path_csv = self.user_data.create_path_csv()
        start_time = time.time()

        print("Data acquisition in progress...\n")
        self.exe_manager.start_script(path_csv, self.duration_time.get_time_sec())

        current_time = time.time() - start_time
        
        """ while(self.duration_time.is_time_over(current_time)):
            current_time = time.time() - start_time

            if current_time % 5 == 0:
                print(f"Current Time: {current_time} \n")
 """
        print("Data acquisition completed \n")
        input("Press Enter to continue...")
        print("\n")

    def repeat_or_close_screen(self):
        """
        Display the repeat or close screen and prompt user for choice.

        Returns
        -------
        str 
            'R' if user chooses to repeat, 'Q' if user chooses to quit.
        """
        while True:
            choice = input("Press R to repeat measurement or Q to quit the program: ").upper()
            print("\n")
            if choice == 'R':
                return choice
            elif choice == 'Q':
                print("Exiting the program \n")
                return choice
            else:
                print("Invalid input, please choose 'R' to repeat or 'Q' to quit \n")