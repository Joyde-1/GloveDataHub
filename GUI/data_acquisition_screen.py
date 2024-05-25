from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QFileDialog, QInputDialog
from custom_button import CustomButton
from window_manager import WindowManager
import sys
import os

# Add the path of the 'Data-Acquisition' directory to the PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))

from user_data import UserData
from duration_time import DurationTime
from exe_manager import ExeManager

class DataAcquisitionScreen:
    """
    DataAcquisitionScreen class manages the data acquisition process.

    Attributes
    ----------
    is_first_time : bool 
        Flag indicating if it's the first time setting up the screen.
    duration_entry : QtWidgets.QLineEdit
    Widget for entering the measurement duration.
    data_acquisition_panel : QtWidgets.QWidget 
        Panel containing all widgets for data acquisition.
    timer : QtCore.QTimer 
        Timer for tracking the measurement duration.
    lapsed_time : int 
        Time elapsed since the start of measurement.
    path_to_csv : str
        Path to the CSV file for saving measurement data.
    total_time : int 
        Total duration of the measurement in seconds.
    field_error : str 
        Error message related to the duration field.
    time_display : QtWidgets.QLabel 
        Widget for displaying the elapsed time.
    time_to_reach_label : QtWidgets.QLabel 
        Widget for displaying the remaining time.
    back_button : CustomButton 
        Button for navigating to the previous screen.
    measurement_button : CustomButton
        Button for starting/stopping/restarting the measurement.
    next_button : CustomButton
        Button for navigating to the next screen.
    """
    is_first_time = True
    
    duration_entry = None
    time_display = None
    time_to_reach_label = None
    
    
    def __init__(self, main_window: WindowManager, user_data: UserData):
        """
        Constructor, initializes the DataAcquisitionScreen.

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
        self.stop_measurement_button = None 
        
    def set_data_acquisition_screen(self):
        """Sets up the data acquisition screen."""
        if DataAcquisitionScreen.is_first_time:
            self._create_data_acquisition_widget()
            DataAcquisitionScreen.is_first_time = not DataAcquisitionScreen.is_first_time
        else:
            self._reset_time_layout()
            
        self._set_buttons_layout()
    
    def _create_data_acquisition_widget(self):  
        """Creates the widgets for data acquisition."""
        # Create a panel to contain all widgets
        self.data_acquisition_panel = QtWidgets.QWidget()
        self.data_acquisition_panel.setStyleSheet("background-color: #E9E6DB;")
        self.data_acquisition_layout = QtWidgets.QVBoxLayout(self.data_acquisition_panel)

        # Description above the field
        description1_text = (
            "Enter the measurement duration in the \n"
            "corresponding field. \n\n"
            "If you prefer the data acquisition to have \n"
            "an unlimited duration, leave the duration \n"
            "field empty."
        )
        description1_label = QtWidgets.QLabel(description1_text)
        description1_label.setWordWrap(True)
        description1_label.setFont(QtGui.QFont("Arial", 16))
        description1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 20px 10px;")
        
        self.data_acquisition_layout.addWidget(description1_label)

        # Widget for duration
        duration_label = QtWidgets.QLabel("Duration (in minutes):")
        duration_label.setFont(QtGui.QFont("Arial", 16))
        duration_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 20px 10px 10px 10px;")
        
        # Field for duration
        DataAcquisitionScreen.duration_entry = QtWidgets.QLineEdit()
        DataAcquisitionScreen.duration_entry.setFont(QtGui.QFont("Arial", 14))
        DataAcquisitionScreen.duration_entry.setStyleSheet("color: black;")
        DataAcquisitionScreen.duration_entry.setFixedWidth(90)
        DataAcquisitionScreen.duration_entry.setContentsMargins(15, 5, 10, 5)
        
        # Layout for duration
        duration_layout = QtWidgets.QVBoxLayout()
        
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(DataAcquisitionScreen.duration_entry)
        
        #duration_layout.addStretch()

        self.data_acquisition_layout.addLayout(duration_layout)
        
        # Lable for time
        time_label = QtWidgets.QLabel("Time:")
        time_label.setFont(QtGui.QFont("Arial", 16))
        time_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 10px 10px 10px")
        
        DataAcquisitionScreen.time_display = QtWidgets.QLabel("00:00:00")
        DataAcquisitionScreen.time_display.setFont(QtGui.QFont("Arial", 16))
        DataAcquisitionScreen.time_display.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 10px 5px;")
        
        DataAcquisitionScreen.time_to_reach_label = QtWidgets.QLabel("/  -")
        DataAcquisitionScreen.time_to_reach_label.setFont(QtGui.QFont("Arial", 16))
        DataAcquisitionScreen.time_to_reach_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 10px 0px;")
        
        # Display the timer
        time_layout = QtWidgets.QHBoxLayout()
        
        time_layout.addWidget(time_label)
        time_layout.addWidget(DataAcquisitionScreen.time_display)
        time_layout.addWidget(DataAcquisitionScreen.time_to_reach_label)
        
        time_layout.addStretch()
        
        self.data_acquisition_layout.addLayout(time_layout)
        
        # Description below the field
        description2_text = (
            "Press the 'Start Measurement' button to \n"
            "start capturing data from your haptic gloves."
        )
        description2_label = QtWidgets.QLabel(description2_text)
        description2_label.setWordWrap(True)
        description2_label.setFont(QtGui.QFont("Arial", 16))
        description2_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 20px 10px;")
        
        self.data_acquisition_layout.addWidget(description2_label)
        
        # Add the panel to the layout of the main content
        self.main_window.add_content_widget(self.data_acquisition_panel)
        
    def _start_timer(self):
        """Starts the timer for measurement duration."""        
        DataAcquisitionScreen.time_display.setText("00:00:00")  # Reset the time display
        
        # Initialize the timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._update_timer)
        
        # Time elapsed in seconds
        self.elapsed_time = 0
        
        #Start the timer with an interval of 1 second (1000 milliseconds)
        self.timer.start(1000)
        
    def _update_timer(self):
        """Updates the timer display."""
        self.elapsed_time += 1
        hours, remainder = divmod(self.elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        DataAcquisitionScreen.time_display.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        # Stop the measurement if the duration is over
        if self.duration_time.is_time_over(self.elapsed_time) or not self.exe_manager.is_sensecom_running():
            self._stop_measurement()
            
    def _conclude_data_acquisition(self):
        """Concludes the data acquisition process."""
        self.timer.stop()
        self._show_success_message()
        self.elapsed_time = 0  # Reset the elapsed time
        
    def _set_buttons_layout(self):
        """Sets up the layout for buttons."""
        # Button for going back
        self.back_button = CustomButton("Back", 120, 40, 16)
        self.back_button.clicked.connect(self._show_previous_screen)
        
        # Button for starting/stopping the measurement
        self.measurement_button = CustomButton("Start Measurement", 240, 40, 16)
        self.measurement_button.clicked.connect(self._start_measurement)
        
        # Button for proceeding
        self.next_button = CustomButton("Next", 120, 40, 16)
        self.next_button.clicked.connect(self._show_next_screen)
        
        self.buttons_layout = QtWidgets.QHBoxLayout()
        
        self.buttons_layout.addWidget(self.back_button, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.measurement_button, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.next_button, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        
        # Set the initial state of buttons
        self.next_button.hide()
        
        self.buttons_layout.setAlignment(self.back_button, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.button_widget = QtWidgets.QWidget()
        self.button_widget.setLayout(self.buttons_layout)
        
        self.main_window.add_button(self.button_widget)

    def _show_previous_screen(self):
        """
        Shows the previous screen.
        """
        from data_entry_screen import DataEntryScreen
        
        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        self.data_entry_screen.set_data_entry_screen()

    def _show_next_screen(self):
        """
        Shows the next screen.
        """
        from final_screen import FinalScreen
        
        self.main_window.clear_buttons_layout()
        
        self.final_screen = FinalScreen(self.main_window)
        
        self.final_screen.set_final_screen()
        
        self.main_window.show_content_widget("Next")

    def _start_measurement(self): 
        """Starts the measurement process."""      
        self._save_duration_field()
        self._check_sensecom_running_before_start()
        
        if not self._is_error_message():
            self.path_to_csv = self.user_data.create_path_csv()
            
            self.total_time = self.duration_time.get_time_sec()
            
            self.exe_manager.start_script(self.path_to_csv, self.total_time)
            
            self._start_timer()
            
            self.back_button.hide()
            self.measurement_button.setText("Stop")
            self.measurement_button.clicked.disconnect(self._start_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)
        else:
            self._show_error_message()
        
    def _stop_measurement(self):
        """Stop the measurement process."""  
        if self.exe_manager.is_script_running() and not self.duration_time.is_time_over(self.elapsed_time):
            
            self.exe_manager.close_script()
            
        self._conclude_data_acquisition()
            
        self.measurement_button.setText("Restart")
        self.measurement_button.clicked.disconnect(self._stop_measurement)
        self.measurement_button.clicked.connect(self._restart_measurement)
        self.next_button.show()
        self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.setAlignment(self.next_button, QtCore.Qt.AlignmentFlag.AlignRight)
            
    def _restart_measurement(self):
        """Restart the measurement process."""  
        self._save_duration_field()
        self._check_sensecom_running_before_start()
        
        if not self._is_error_message():            
            self.total_time = self.duration_time.get_time_sec()
            
            self.exe_manager.start_script(self.path_to_csv, self.total_time)
            
            self._start_timer()
            
            self.measurement_button.setText("Stop")
            self.measurement_button.clicked.disconnect(self._restart_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            self.next_button.hide()
            self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)
        else:
            self._show_error_message()

    def _save_duration_field(self):
        """Saves the duration entered by the user."""
        self.fields_errors = ""
        
        duration = DataAcquisitionScreen.duration_entry.text()  # Ottieni la durata inserita dall'utente
            
        if duration == "":
            self.duration_time.set_time_min()
            DataAcquisitionScreen.time_to_reach_label.setText("/  ∞")
        else:
            try:
                self.duration_time.set_time_min(duration)
                
                duration = int(duration)
                
                hours, minutes = divmod(duration, 60)
                DataAcquisitionScreen.time_to_reach_label.setText(f"/  {hours:02d}:{minutes:02d}:00")
            except ValueError as e:
                self.fields_errors += "• " + str(e)
                
    def _check_sensecom_running_before_start(self):
        """
        Checks if sensecom is running before script starts
        """
        if not self.exe_manager.is_sensecom_running():
            self.fields_errors += "• " + ("SenseCom is not running. Please press the 'Start Sensecom' \n   "
                                          "button to start SenseCom before proceeding with data acquisition. \n")
    
    def _is_error_message(self):
        """Checks if there are errors messages."""
        if self.fields_errors != "":
            self.fields_errors = "Please fix the following errors:\n" + self.fields_errors
            return True
        else:
            return False

    def _show_error_message(self):
        """Shows an error message."""
        error_msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, "Error", self.fields_errors.strip())
        self._set_output_dialog_style(error_msg_box)
        error_msg_box.exec()
        
    def _show_success_message(self):
        """Shows a success message."""
        timer_msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, "Success", ("I dati dei guanti aptici sono stati \n"
                                                                                                  "acquisiti con successo!"))
        self._set_output_dialog_style(timer_msg_box)
        timer_msg_box.exec() 

    def _set_output_dialog_style(self, dialog):
        """
        Sets the style for the output dialog.

        Parameters
        ----------
        dialog : QMessageBox 
            The output dialog to set the style for.
        """
        if dialog:
            dialog.setStyleSheet("""
                QMessageBox {
                    color: black;
                    background-color: #E9E6DB;
                }
                QLabel {
                    color: black;
                    font: ("Arial", 14);
                }
                QPushButton {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #E9E6DB, stop:1 #C8C5B8);
                    color: black;
                    border: 2px solid #C8C5B8;
                    border-radius: 15px;
                    padding: 5px 7px;
                    min-width: 30px;
                }
                QPushButton:hover {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #C8C5B8, stop:1 #A9A69B);
                    border-color: #A9A69B;
                    color: black;
                    border: 2px solid #A9A69B;
                    border-radius: 15px;
                    padding: 5px 7px;
                }
                QPushButton:pressed {
                    background-color: #A9A69B;
                    border-color: #8B887E;
                    color: black;
                    border: 2px solid #8B887E;
                    border-radius: 15px;
                    padding: 5px 7px;
                }
            """)
