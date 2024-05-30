from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from custom_button import CustomButton
from window_manager import WindowManager
from pathlib import Path

class FinalScreen:
    """
    Represents the final screen of the application, displayed after the measurement process.

    Attributes
    ----------
    is_first_time : bool 
        A flag to indicate if it's the first time setting up the final screen.
    """
    is_first_time = True
    
    def __init__(self, main_window: WindowManager):
        """
        Constructor, initializes the FinalScreen.

        Parameters
        ----------
        main_window : WindowManager 
            Instance of WindowManager for managing the main window.
        """
        self.main_window = main_window

    def set_final_screen(self):
        """
        Sets up the final screen of the application.
        """
        if FinalScreen.is_first_time:
            self._create_final_screen_widget() # Create the widget for the final screen
            FinalScreen.is_first_time = not FinalScreen.is_first_time
            
        self._set_buttons_layout() # Create the layout button for the final screen
        
    def _create_final_screen_widget(self):
        """
        Create the final screen widget and its components.
        """
        # Create a panel to contain all widgets
        self.final_screen_panel = QWidget()
        self.final_screen_panel.setStyleSheet("background-color: #FFFCF0;")
        self.final_screen_layout = QVBoxLayout(self.final_screen_panel)
        
        # Welcome title
        final_screen_label = QLabel("Thanks for using GloveDataHub!")
        final_screen_label.setFont(QtGui.QFont("Montserrat", 20, QtGui.QFont.Weight.Bold))
        final_screen_label.setStyleSheet("color: #023E58; background-color: #FFFCF0; padding: 20px 0px 30px 20px;")
        final_screen_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.final_screen_layout.addWidget(final_screen_label)
        
        # Application description
        description_text = (
            'If you want to perform a new data acquisition process from your haptic gloves, click the <b><span style="color: #025885;">New Acquisition</span></b> button. <br>'
            'Otherwise click on the <b><span style="color: #025885;">Close</span></b> button to exit from GloveDataHub.'
        )
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QtGui.QFont("Source Sans Pro", 16))
        description_label.setStyleSheet("color: #031729; background-color: #FFFCF0; padding: 0px 20px 40px 20px;")
        
        self.final_screen_layout.addWidget(description_label)
        
        self.final_screen_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Add the welcome panel to the main window content layout
        self.main_window.add_content_widget(self.final_screen_panel)
        
    def _set_buttons_layout(self):
        """
        Sets up the layout for buttons.
        """
        new_measurement_button = CustomButton("New Acquisition", 1, 240, 40, 16)
        new_measurement_button.clicked.connect(self._start_new_data_acquisition)
        
        close_button = CustomButton("Close", 0, 120, 40, 16)
        close_button.clicked.connect(self._close_application)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(new_measurement_button)
        buttons_layout.addWidget(close_button)
        
        buttons_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        
        button_widget = QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
    def _start_new_data_acquisition(self):
        """
        Starts a new data acquisition by navigating back to the calibration screen.
        """
        from calibration_screen import CalibrationScreen
        
        self.main_window.show_content_widget("New")
        
        self.main_window.clear_buttons_layout()
        
        self._reset_entry_fields()
        
        self.calibration_screen = CalibrationScreen(self.main_window)
        
        self.calibration_screen.set_calibration_screen()
        
    def _reset_entry_fields(self):
        """
        Reset all entry fields in data acquisition's screens
        """
        from calibration_screen import CalibrationScreen
        from data_entry_screen import DataEntryScreen
        from data_acquisition_screen import DataAcquisitionScreen
        
        CalibrationScreen.is_data_acquired = not CalibrationScreen.is_data_acquired
        
        DataEntryScreen.first_name_entry.setText("")
        DataEntryScreen.last_name_entry.setText("")
        DataEntryScreen.code_entry.setText("")
        DataEntryScreen.path_directory_entry.setText(str(Path.home() / "Documents"))
        
        DataAcquisitionScreen.description1_text = (
            "Enter the measurement duration in the <br>"
            "corresponding field. <br><br>"
            "If you prefer the data acquisition to have an <br>"
            "unlimited duration, leave the duration field <br>"
            "empty."
        )
        DataAcquisitionScreen.description1_label.setText(DataAcquisitionScreen.description1_text)
        DataAcquisitionScreen.description1_label.setStyleSheet("color: #031729; background-color: #FFFCF0; padding: 0px 10px 0px 10px; margin: 0px 0px 15px 0px")
        
        DataAcquisitionScreen.duration_entry.setText("")
        
        DataAcquisitionScreen.timer_display.setStyleSheet("color: #023E58; background-color: #D9E7EC; padding: 0px 0px 10px 5px;")
        
        DataAcquisitionScreen.timer_display.hide()
        
        DataAcquisitionScreen.description2_text = (
            'Press the <b><span style="color: #025885;">Start Measurement</span></b> button to <br>'
            "start capturing data from your haptic gloves."
        )
        DataAcquisitionScreen.description2_label.setText(DataAcquisitionScreen.description2_text)
        DataAcquisitionScreen.description2_label.setStyleSheet("color: #031729; background-color: #FFFCF0; margin: 15px 0px 0px 0px; padding: 0px 10px 0px 10px;")
        
    def _close_application(self):
        """
        Closes the application.
        """
        QtCore.QCoreApplication.quit()