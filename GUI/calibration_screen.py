#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont

from window_manager import WindowManager
from custom_button import CustomButton


class CalibrationScreen():
    """
    Class representing the calibration screen.

    Attributes
    ----------
    is_first_time : bool (class attribute)
        Indicates whether it's the first time the screen is being displayed.
    is_data_acquired : bool (class attribute)
        Indicates whether the data has been acquired.
    main_window : WindowManager (istance attribute)
        The main window manager instance.
    calibration_panel : QWidget (istance attribute)
        The main widget for the calibration screen.
    calibration_screen : CalibrationScreen (istance attribute)
        Set the calibration screen when 'Back' button is clicked.
    data_entry_screen : DataEntryScreen (istance attribute)
        Set the data entry screen when 'Next' button is clicked.
    """
    
    is_first_time = True
    is_data_acquired = False
    
    def __init__(self, main_window: WindowManager):
        """
        Initializes the CalibrationScreen.

        Parameters
        ----------
        main_window : WindowManager 
            The main window manager instance.
        """
        
        self.main_window = main_window
        
    def set_calibration_screen(self):
        """
        Sets up the calibration screen.
        """
        
        # Check if is the first time the calibration screen is being set
        if CalibrationScreen.is_first_time:
            self._create_calibration_widget()
            CalibrationScreen.is_first_time = not CalibrationScreen.is_first_time
        
        # Check if SenseCom layout is already created
        if not WindowManager.is_sensecom_layout:
            self.main_window.create_sensecom_widget()
        
        # Set the buttons layout            
        self._set_buttons_layout()

    def _create_calibration_widget(self):
        """
        Creates the widgets for the calibration screen.
        """
        
        # Create a panel to contain all the widgets
        self.calibration_panel = QWidget()
        self.calibration_panel.setStyleSheet("background-color: #CFDCE6; border-radius: 15px; padding: 10px")
        calibration_layout = QVBoxLayout(self.calibration_panel)
        
        # Calibration screen title
        calibration_title = QLabel("1 • Calibration of Haptic Gloves")
        calibration_title.setWordWrap(True)
        calibration_title.setFont(QFont("Montserrat", 16, QFont.Weight.Bold))
        calibration_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        calibration_title.setStyleSheet("color: #FFFFFF; background-color: #026192; border-radius: 15px; margin: 10px 10px 10px 10px;")
        
        calibration_layout.addWidget(calibration_title)
        
        # Description of the calibration screen
        description_text = (
            "To calibrate your haptic gloves, you need to <br>"
            'run the <b><span style="color: #025885;">SenseCom</span></b> application, which <br>'
            "handles the connection. <br><br>"
            "It is important that this application remains <br>"
            "open throughout the session. <br><br>"
            "In case you mistakenly close it, please reopen <br>"
            "it and re-calibrate. <br><br>"
            'Press the <b><span style="color: #025885;">Start Sensecom</span></b> button to start <br>'
            "the application and proceed with the calibration."
        )
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QFont("Source Sans Pro", 14))
        description_label.setStyleSheet("color: #031729; background-color: #CFDCE6; padding: 0px;")

        description_layout = QVBoxLayout()
        
        description_layout.addWidget(description_label)
        description_layout.setContentsMargins(0, 0, 0, 0)
        
        description_widget = QWidget()
        
        description_widget.setLayout(description_layout)
        description_widget.setStyleSheet("margin: 0px 10px 10px 10px; padding 0px;")
        description_widget.setContentsMargins(0, 0, 0, 0)
        
        calibration_layout.addWidget(description_widget)
        
        calibration_layout.addStretch()
        
        self.main_window.add_content_widget(self.calibration_panel)
        
    def _set_buttons_layout(self):
        """
        Sets up the layout for buttons.
        """
        
        # Button to go back
        back_button = CustomButton("Back", 0, 120, 40, 16)
        back_button.clicked.connect(self._show_previous_screen)
        
        # Button to proceed
        next_button = CustomButton("Next", 0, 120, 40, 16)
        next_button.clicked.connect(self._show_next_screen)
        
        buttons_layout = QHBoxLayout()
        
        buttons_layout.addWidget(back_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(next_button)
        
        # If data has already acquired, hide 'Back' button
        if CalibrationScreen.is_data_acquired == True:
            back_button.hide()
            buttons_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
            
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        
        button_widget = QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)

    def _show_previous_screen(self):
        """
        Shows the previous screen.
        """
        
        # Delayed import to avoid circular import between start_calibration_screen class and welcome_screen class
        from welcome_screen import WelcomeScreen
        
        # Close and remove SenseCom from the GUI
        self.main_window.close_sensecom_widget()
        
        # Show the previous screen
        self.main_window.show_content_widget("Back")
        
        # Remove all the buttons from main window buttons layout
        self.main_window.clear_buttons_layout()
        
        self.welcome_screen = WelcomeScreen(self.main_window)
        
        # Set the final screen
        self.welcome_screen.set_welcome_screen()
        

    def _show_next_screen(self):
        """
        Shows the next screen.
        """
        
        from data_entry_screen import DataEntryScreen
        
        # Remove all the buttons from main window buttons layout
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        # Set the data entry screen
        self.data_entry_screen.set_data_entry_screen()
        
        # Show the next screen
        self.main_window.show_content_widget("Next") 