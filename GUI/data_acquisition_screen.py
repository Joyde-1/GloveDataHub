#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont
import os
import sys

# Add the main directory path to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from API.user_data import UserData
from API.duration_time import DurationTime
from API.exe_manager import ExeManager
from custom_button import CustomButton
from message_manager import MessageManager
from window_manager import WindowManager


class DataAcquisitionScreen:
    """
    DataAcquisitionScreen class manages the data acquisition process.

    Attributes
    ----------
    is_first_time : bool (class attribute)
        Flag indicating if it's the first time setting up the screen.
    description1_text : str (class attribute):
        Dynamic description in the top of the panel.
    description1_label : QLabel (class attribute)
        Dynamic label in the top of the panel.
    description2_text : str (class attribute)
        Dynamic description in the bottom of the panel.
    description2_label : QLabel (class attribute)
        Dynamic label in the bottom of the panel.
    duration_entry : QLineEdit (class attribute)
        Field for entering the measurement duration.
    duration_widget : QWidget (class attribute)
        Widget for entering the measurement duration.
    timer_display : QLabel (class attribute)
        Widget for displaying the elapsed time.
    main_window : WindowManager (istance attribute)
            Instance of WindowManager for managing the main window.
    user_data : UserData (istance attribute)
        Instance of UserData for managing user data.
    duration_time : DurationTime (istance attribute)
        Istance of DurationTime for manage duration time.
    exe_manager : ExeManager (istance attribute)
        An instance of the ExeManager class.
    data_acquisition_panel : QWidget (istance attribute)
        Panel containing all widgets for data acquisition.
    data_acquisition_layout : QVBoxLayout (istance attribute)
        Dynamic data acquisition layout
    back_button : CustomButton 
        Button for navigating to the previous screen.
    measurement_button : CustomButton
        Button for starting/stopping/restarting the measurement.
    next_button : CustomButton
        Button for navigating to the next screen.
    buttons_layout : QHBoxLayout
        The dybamic buttons layout.
    timer : QTimer 
        Timer for tracking the measurement duration.
    elapsed_time : int 
        Time elapsed since the start of measurement.
    path_to_csv : str
        Path to the CSV file for saving measurement data.
    time_to_reach : str
        Usefull to show the remaining time.
    fields_errors : str 
        Errors messages related to the duration field or SenseCom widget.
    script_return_code : int 
        The return code of the script to acquire data.
    data_entry_screen : DataEntryScreen (istance attribute)
        Set the data entry screen when 'Back' button is clicked.
    final_screen : FinalScreen (istance attribute)
        Set the final screen when 'Next' button is clicked.
    """
    
    is_first_time = True
    
    description1_text = None
    description1_label = None
    description2_text = None
    description2_label = None
    duration_entry = None
    duration_widget = None
    timer_display = None
    
    
    def __init__(self, main_window: WindowManager, user_data: UserData):
        """
        Constructor, initializes the data acquisition screen.

        Parameters
        ----------
        main_window : WindowManager 
            Instance of WindowManager for managing the main window.
        user_data : UserData 
            Instance of UserData for managing user data.
        """
        
        self.main_window = main_window
        self.user_data = user_data
        
        self.duration_time = DurationTime()
        self.exe_manager = ExeManager()
        
        self.script_return_code = None
        
    def set_data_acquisition_screen(self):
        """
        Sets up the data acquisition screen.
        """
        
        # Check if is the first the data acquisition screen is being set
        if DataAcquisitionScreen.is_first_time:
            self._create_data_acquisition_widget()
            DataAcquisitionScreen.is_first_time = not DataAcquisitionScreen.is_first_time
        else:
            # Reset the timer
            self._reset_time_layout()
        
        # Set the buttons layout
        self._set_buttons_layout()
    
    def _create_data_acquisition_widget(self):  
        """
        Creates the widgets for data acquisition.
        """
        
        # Create a panel to contain all widgets
        self.data_acquisition_panel = QWidget()
        self.data_acquisition_panel.setStyleSheet("background-color: #CFDCE6; border-radius: 15px; padding: 10px")
        self.data_acquisition_layout = QVBoxLayout(self.data_acquisition_panel)

        # Data acquistion title
        data_acquisition_title = QLabel("3 • Data Acquisition")
        data_acquisition_title.setWordWrap(True)
        data_acquisition_title.setFont(QFont("Montserrat", 16, QFont.Weight.Bold))
        data_acquisition_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        data_acquisition_title.setStyleSheet("color: #FFFFFF; background-color: #026192; border-radius: 15px; margin: 10px 10px 10px 10px;")
        
        self.data_acquisition_layout.addWidget(data_acquisition_title)

        # Description above the field
        DataAcquisitionScreen.description1_text = (
            "Enter the measurement duration in the <br>"
            "corresponding field. <br><br>"
            "If you prefer the data acquisition to have an <br>"
            "unlimited duration, leave the duration field <br>"
            "empty."
        )
        DataAcquisitionScreen.description1_label = QLabel(DataAcquisitionScreen.description1_text)
        DataAcquisitionScreen.description1_label.setWordWrap(True)
        DataAcquisitionScreen.description1_label.setFont(QFont("Source Sans Pro", 14))
        DataAcquisitionScreen.description1_label.setStyleSheet("color: #031729; background-color: #CFDCE6; padding: 0px 10px 0px 10px; margin: 0px 0px 15px 0px")
        
        self.data_acquisition_layout.addWidget(DataAcquisitionScreen.description1_label)

        # Widget for duration
        duration_label = QLabel("<b>Duration</b> (in minutes):")
        duration_label.setFont(QFont("Source Sans Pro", 16))
        duration_label.setStyleSheet("color: #025885; background-color: #CFDCE6; margin: 0px 10px 0px 0px; padding: 0px 0px 5px 0px;")
        
        # Field for duration
        DataAcquisitionScreen.duration_entry = QLineEdit()
        DataAcquisitionScreen.duration_entry.setFont(QFont("Georgia", 14))
        DataAcquisitionScreen.duration_entry.setFixedSize(90, 35)
        DataAcquisitionScreen.duration_entry.setStyleSheet("color: #031729; background-color: #FFFFFF; border-radius: 8px; border: 2px solid #BAC6CF; margin: 0px 10px 0px 0px; padding: 5px 5px 5px 5px;")
        
        # Layout for duration
        duration_layout = QVBoxLayout()
        
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(DataAcquisitionScreen.duration_entry)
        
        duration_layout.addStretch(3)
        
        DataAcquisitionScreen.duration_widget = QWidget()
        
        DataAcquisitionScreen.duration_widget.setLayout(duration_layout)
        DataAcquisitionScreen.duration_widget.setContentsMargins(0, 0, 0, 0)
        DataAcquisitionScreen.duration_widget.setStyleSheet("margin: 0px; padding: 5px 0px 5px 0px;")
        
        self.data_acquisition_layout.addWidget(DataAcquisitionScreen.duration_widget)
        
        # Timer display
        DataAcquisitionScreen.timer_display = QLabel("<b>Time</b>:&nbsp;&nbsp;&nbsp;&nbsp;00:00:00 / -")
        DataAcquisitionScreen.timer_display.setFont(QFont("DSEG", 16))
        DataAcquisitionScreen.timer_display.setFixedWidth(305)
        DataAcquisitionScreen.timer_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        DataAcquisitionScreen.timer_display.setStyleSheet("color: #023E58; background-color: #B1BCC4; border-radius: 10px; margin: 10px; padding: 5px;")
        
        self.data_acquisition_layout.addWidget(DataAcquisitionScreen.timer_display, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Hide timer display
        DataAcquisitionScreen.timer_display.hide()
        
        # Description below the field
        DataAcquisitionScreen.description2_text = (
            'Press the <b><span style="color: #025885;">Start Measurement</span></b> button to <br>'
            "start capturing data from your haptic gloves."
        )
        DataAcquisitionScreen.description2_label = QLabel(DataAcquisitionScreen.description2_text)
        DataAcquisitionScreen.description2_label.setWordWrap(True)
        DataAcquisitionScreen.description2_label.setFont(QFont("Source Sans Pro", 14))
        DataAcquisitionScreen.description2_label.setStyleSheet("color: #031729; background-color: #CFDCE6; margin: 15px 0px 0px 0px; padding: 0px 10px 0px 10px;")
        
        self.data_acquisition_layout.addWidget(DataAcquisitionScreen.description2_label)
        
        self.data_acquisition_layout.addStretch()
        
        # Add the panel to the layout of the main content
        self.main_window.add_content_widget(self.data_acquisition_panel)
        
    def _start_timer(self):
        """
        Starts the timer for measurement duration.
        """
        
        # Reset the time display
        DataAcquisitionScreen.timer_display.setText("<b>Time</b>:&nbsp;&nbsp;&nbsp;&nbsp;00:00:00 / " + self.time_to_reach)
        
        # Initialize the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_timer)
        
        # Time elapsed in seconds
        self.elapsed_time = 0
        
        # Start the timer with an interval of 1 second (1000 milliseconds)
        self.timer.start(1000)
        
    def _update_timer(self):
        """
        Updates the timer display.
        """
        
        # Increment of 1 second of elapsed time
        self.elapsed_time += 1
        
        hours, remainder = divmod(self.elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Update timer display
        DataAcquisitionScreen.timer_display.setText(f"<b>Time</b>:&nbsp;&nbsp;&nbsp;&nbsp;{hours:02d}:{minutes:02d}:{seconds:02d} / " + self.time_to_reach)

        # Stop the measurement if the duration is over or SenseCom or script is not running
        if self.duration_time.is_time_over(self.elapsed_time) or not self.exe_manager.is_sensecom_running() or not self.exe_manager.is_script_running():
            self._stop_measurement()
            
    def _reset_time_layout(self):
        """
        Resets timer display
        """
        
        DataAcquisitionScreen.timer_display.setText("<b>Time</b>:&nbsp;&nbsp;&nbsp;&nbsp;00:00:00 / -")
        
    def _conclude_data_acquisition(self):
        """
        Concludes the data acquisition process.
        """
        
        # Stop the timer
        self.timer.stop()
        
        # Check if the script was closed by the 'Stop' button
        if self.script_return_code != 8:
            # Get the return code from the script
            self.script_return_code = self.exe_manager.get_script_return_code()

        # Show success message
        self._show_script_end_message()
        
        # Reset the script return code
        self.script_return_code = None
        
        # Reset the elapsed time
        self.elapsed_time = 0
        
    def _set_buttons_layout(self):
        """
        Sets up the layout for buttons.
        """
        
        # Button for going back
        self.back_button = CustomButton("Back", 0, 120, 40, 16)
        self.back_button.setContentsMargins(20, 0, 300, 20)
        self.back_button.clicked.connect(self._show_previous_screen)
        
        # Button for starting/stopping the measurement
        self.measurement_button = CustomButton("Start Measurement", 1, 240, 40, 16)
        self.measurement_button.setContentsMargins(300, 0, 4000, 20)
        self.measurement_button.clicked.connect(self._start_measurement)
        
        # Button for proceeding
        self.next_button = CustomButton("Next", 0, 120, 40, 16)
        self.next_button.setContentsMargins(300, 0, 20, 20)
        self.next_button.clicked.connect(self._show_next_screen)        
        
        self.buttons_layout = QHBoxLayout()
        
        self.buttons_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.addStretch(20)
        self.buttons_layout.addWidget(self.measurement_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.buttons_layout.addStretch(30)
        self.buttons_layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        
        # Set the initial state of buttons
        self.next_button.hide()
        
        self.button_widget = QWidget()
        
        self.button_widget.setLayout(self.buttons_layout)
        
        self.main_window.add_button(self.button_widget)

    def _show_previous_screen(self):
        """
        Shows the previous screen.
        """
        
        from data_entry_screen import DataEntryScreen
        
        # Show the previous screen
        self.main_window.show_content_widget("Back")
        
        # Remove all the buttons from main window buttons layout
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        # Set the data entry screen        
        self.data_entry_screen.set_data_entry_screen()

    def _show_next_screen(self):
        """
        Shows the next screen.
        """
        
        from final_screen import FinalScreen
        
        # Close and remove SenseCom from the GUI
        self.main_window.close_sensecom_widget()
        
        # Remove all the buttons from main window buttons layout
        self.main_window.clear_buttons_layout()
        
        self.final_screen = FinalScreen(self.main_window)
        
        # Set the final screen
        self.final_screen.set_final_screen()
        
        # Show the next screen
        self.main_window.show_content_widget("Next")

    def _start_measurement(self): 
        """
        Starts the measurement process.
        """      
        
        # Save the duration field
        self._save_duration_field()
        
        # Check if SenseCom is active
        self._check_sensecom_running_before_start()
        
        # Check if there is a error message to show
        if not self._is_error_message():
            
            # Get file .CSV path to save data
            self.path_to_csv = self.user_data.create_path_csv()
            
            # get duration time in seconds
            total_time = self.duration_time.get_time_sec()
            
            # Start the script to get data from haptic gloves
            self.exe_manager.start_script(self.path_to_csv, total_time)
            
            # Start the timer
            self._start_timer()
            
            # New description for this screen
            DataAcquisitionScreen.description1_text = (
                "The script to capture the data is running. \n\n"
                "SenseCom manages the connection with your \n"
                "haptic gloves, so if you close it, the \n"
                "measurement will be stopped instantly."
            )
            
            DataAcquisitionScreen.description1_label.setText(DataAcquisitionScreen.description1_text)
            
            # Hide duration widget
            DataAcquisitionScreen.duration_widget.hide()
            
            DataAcquisitionScreen.timer_display.setStyleSheet("color: #023E58; background-color: #B1BCC4; border-radius: 10px; margin: 15px 10px 10px 10px; padding: 5px;")
            
            # Show timer display
            DataAcquisitionScreen.timer_display.show()
            
            # New description for this screen
            DataAcquisitionScreen.description2_text = (
                "Then if you want to stop data acquisition <br>"
                'immediately, you can press the <b><span style="color: #025885;">Stop</span></b> button <br>'
                "or close SenseCom."
            )
            
            DataAcquisitionScreen.description2_label.setText(DataAcquisitionScreen.description2_text)
            
            # Set buttons layout and handlers with only 'Stop' button
            self.back_button.hide()
            self.measurement_button.setText("Stop")
            self.measurement_button.setFixedSize(120, 40)
            self.measurement_button.clicked.disconnect(self._start_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            
            self.buttons_layout.setAlignment(self.back_button, Qt.AlignmentFlag.AlignLeft)
            self.buttons_layout.setStretch(1, 1)
            self.buttons_layout.setAlignment(self.measurement_button, Qt.AlignmentFlag.AlignCenter)
            self.buttons_layout.setStretch(3, 1)
            self.buttons_layout.setAlignment(self.next_button, Qt.AlignmentFlag.AlignRight)
        else:
            self._show_error_message()
        
    def _stop_measurement(self):
        """
        Stop the measurement process.
        """  
        
        # Check if the script is running while the duration_time isn't over
        if self.exe_manager.is_script_running() and not self.duration_time.is_time_over(self.elapsed_time):
            
            # Terminate the script to get data from haptic gloves
            self.exe_manager.close_script()
            
            self.script_return_code = 8
            
        self._conclude_data_acquisition()
        
        DataAcquisitionScreen.description1_text = (
            "The data has been successfully acquired. <br>"
            "If you are not satisfied with the <br>"
            "measurement, you can repeat it by entering <br>"
            "the duration in the corresponding field again."
        )
        
        DataAcquisitionScreen.description1_label.setText(DataAcquisitionScreen.description1_text)
        DataAcquisitionScreen.description1_label.setStyleSheet("color: #031729; background-color: #CFDCE6; padding: 0px 10px 0px 10px; margin: 0px 0px 0px 0px")
        
        DataAcquisitionScreen.duration_widget.show()
        
        DataAcquisitionScreen.timer_display.setStyleSheet("color: #023E58; background-color: #B1BCC4; border-radius: 10px; margin: 10px 10px 10px 10px; padding: 5px;")
        
        DataAcquisitionScreen.description2_text = (
            "If you want to repeat the measurement, press <br>"
            'the <b><span style="color: #025885;">Restart</span></b> button. Otherwise if you want to <br>'
            'go ahead, press the <b><span style="color: #025885;">Next</span></b> button.'
        )
        
        DataAcquisitionScreen.description2_label.setText(DataAcquisitionScreen.description2_text)
        DataAcquisitionScreen.description2_label.setStyleSheet("color: #031729; background-color: #CFDCE6; margin: 0px 0px 0px 0px; padding: 0px 10px 0px 10px;")
        
        self.next_button.show()
        
        self.measurement_button.setText("Restart")
        self.measurement_button.setFixedSize(140, 40)
        self.measurement_button.clicked.disconnect(self._stop_measurement)
        self.measurement_button.clicked.connect(self._restart_measurement)
        
        self.buttons_layout.setAlignment(self.back_button, Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.setStretch(1, 48)
        self.buttons_layout.setAlignment(self.measurement_button, Qt.AlignmentFlag.AlignCenter)
        self.buttons_layout.setStretch(3, 34)
        self.buttons_layout.setAlignment(self.next_button, Qt.AlignmentFlag.AlignRight)
            
    def _restart_measurement(self):
        """
        Restart the measurement process.
        """  
        
        self._save_duration_field()
        self._check_sensecom_running_before_start()
        
        if not self._is_error_message():            
            total_time = self.duration_time.get_time_sec()
            
            self.exe_manager.start_script(self.path_to_csv, total_time)
            
            self._start_timer()
            
            DataAcquisitionScreen.description1_text = (
                "The script to capture the data is running. \n\n"
                "SenseCom manages the connection with your \n"
                "haptic gloves, so if you close it, the \n"
                "measurement will be stopped instantly."
            )
            
            DataAcquisitionScreen.description1_label.setText(DataAcquisitionScreen.description1_text)
            DataAcquisitionScreen.description1_label.setStyleSheet("color: #031729; background-color: #CFDCE6; padding: 0px 10px 0px 10px; margin: 0px 0px 15px 0px")
            
            DataAcquisitionScreen.duration_widget.hide()
            
            DataAcquisitionScreen.timer_display.setStyleSheet("color: #023E58; background-color: #B1BCC4; border-radius: 10px; margin: 10px 10px 15px 10px; padding: 5px;")
            
            DataAcquisitionScreen.timer_display.show()
                        
            DataAcquisitionScreen.description2_text = (
                "Then if you want to stop data acquisition <br>"
                'immediately, you can press the <b><span style="color: #025885;">Stop</span></b> button <br>'
                "or close SenseCom."
            )
            
            DataAcquisitionScreen.description2_label.setText(DataAcquisitionScreen.description2_text)
            DataAcquisitionScreen.description2_label.setStyleSheet("color: #031729; background-color: #CFDCE6; margin: 15px 0px 0px 0px; padding: 0px 10px 0px 10px;")
            
            self.measurement_button.setText("Stop")
            self.measurement_button.setFixedSize(120, 40)
            self.measurement_button.clicked.disconnect(self._restart_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            self.next_button.hide()
            
            self.buttons_layout.setAlignment(self.back_button, Qt.AlignmentFlag.AlignLeft)
            self.buttons_layout.setStretch(1, 1)
            self.buttons_layout.setAlignment(self.measurement_button, Qt.AlignmentFlag.AlignCenter)
            self.buttons_layout.setStretch(3, 1)
            self.buttons_layout.setAlignment(self.next_button, Qt.AlignmentFlag.AlignRight)
        else:
            self._show_error_message()

    def _save_duration_field(self):
        """
        Saves the duration entered by the user.
        """
        
        self.fields_errors = ""
        
        # Get the duration entered by the user
        duration = DataAcquisitionScreen.duration_entry.text()
        
        if duration == "":
            # If the duration is unlimited:
            self.duration_time.set_time_min()
            self.time_to_reach = "∞"
            
            DataAcquisitionScreen.timer_display.setFixedWidth(240)
        else:
            # If the duration is a finite number
            try:
                self.duration_time.set_time_min(duration)
                
                duration = int(duration)
                
                hours, minutes = divmod(duration, 60)
                self.time_to_reach = f"{hours:02d}:{minutes:02d}:00"
                
                DataAcquisitionScreen.timer_display.setFixedWidth(305)
            except ValueError as e:
                self.fields_errors += "• " + str(e)
                
    def _check_sensecom_running_before_start(self):
        """
        Checks if sensecom is running before script starts
        """
        
        if not self.exe_manager.is_sensecom_running():
            self.fields_errors += "• " + ('SenseCom is not running. Please press the <b><span style="color: #025885;">Start Sensecom</span></b> <br>'
                                          "button to start SenseCom before proceeding with data acquisition. <br>")
    
    def _is_error_message(self):
        """
        Checks if there are errors messages.
        """
        
        if self.fields_errors != "":
            self.fields_errors = "Please fix the following errors:<br>" + self.fields_errors
            return True
        else:
            return False

    def _show_error_message(self):
        """
        Shows an error message.
        """
        
        message_manager = MessageManager("Error", self.fields_errors.strip())
            
        # Show an error message with an output dialog
        message_manager.show_message_box()
        
    def _show_script_end_message(self):
        """
        Shows the end of script message.
        """
        
        # Set the message box by the return code of the script
        if self.script_return_code == 0 or self.script_return_code == 7 or self.script_return_code == 8:
            msg_box_title = "Success"
            msg_box_msg = ("Haptic gloves data have been acquired successfully!")
        elif self.script_return_code == 1:
            msg_box_title = "Error"
            msg_box_msg = ("The script for capturing data from haptic gloves has broken down. <br>"
                           'Please press the <b><span style="color: #025885;">Restart</span></b> button to perform a new measurement.')
        elif self.script_return_code == 2:
            msg_box_title = "Error"
            msg_box_msg = ("The Script was run to acquire data from haptic gloves passing an <br>"
                           "inadequate number of arguments. <br>"
                           'Please press the <b><span style="color: #025885;">Restart</span></b> button to perform a new measurement.')
        elif self.script_return_code == 3:
            msg_box_title = "Error"
            msg_box_msg = ("The script to acquire data from haptic gloves encountered an <br>"
                           "error opening the file .CSV. <br>"
                           'Please press the <b><span style="color: #025885;">Restart</span></b> button to perform a new measurement.')
        elif self.script_return_code == 4:
            msg_box_title = "Error"
            msg_box_msg = ("The script to acquire data from haptic gloves suddenly <br>"
                           "stopped because it did not detect one or more gloves. <br>"
                           'Please press the <b><span style="color: #025885;">Restart</span></b> button to perform a new measurement.')
        elif self.script_return_code == 5:
            msg_box_title = "Error"
            msg_box_msg = ("The script to acquire data from haptic gloves suddenly <br>"
                           "stopped because the connection with SenseCom was interrupted. <br>"
                           'Please press the <b><span style="color: #025885;">Restart</span></b> button to perform a new measurement.')
        elif self.script_return_code == 6:
            msg_box_title = "Error"
            msg_box_msg = ("The script to acquire data from haptic gloves failed to <br>"
                           "start SenseCom by forcing it to run. <br>"
                           'Please press the <b><span style="color: #025885;">Restart</span></b> button to perform a new measurement.')
        
        message_manager = MessageManager(msg_box_title, msg_box_msg)
            
        # Show an error message with an output dialog
        message_manager.show_message_box()