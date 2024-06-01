#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont

from window_manager import WindowManager
from custom_button import CustomButton


class WelcomeScreen:
    """
    Class to manage the welcome screen of the application.

    Attributes
    ----------
    is_first_time : bool (class attribute)
        Flag to indicate if it's the first time the welcome screen is being set.
    main_window : WindowManager (istance attribute)
        The main window manager instance.
    welcome_panel : QWidget (istance attribute)
        The main widget for the welcome screen.
    calibration_screen : CalibrationScreen (istance attribute)
        Set the calibration screen when 'Next' button is clicked.
    """
    
    is_first_time = True
    
    def __init__(self, main_window: WindowManager):
        """
        Constructor, initialize the WelcomeScreen.

        Parameters
        ----------
        main_window : WindowManager 
            The main window manager instance.
        """
        
        self.main_window = main_window
        
    def set_welcome_screen(self):
        """
        Set up and display the welcome screen.
        """
        
        # Check if is the first the welcome screen is being set
        if WelcomeScreen.is_first_time:
            self._create_welcome_widget()
            WelcomeScreen.is_first_time = not WelcomeScreen.is_first_time
        
        # Set the buttons layout
        self._set_buttons_layout()

    def _create_welcome_widget(self):
        """
        Create the welcome screen widget and its components.
        """
        
        # Create a panel to contain all widgets
        self.welcome_panel = QWidget()
        self.welcome_panel.setStyleSheet("background-color: #CFDCE6;")
        welcome_layout = QVBoxLayout(self.welcome_panel)
        
        # Welcome title
        welcome_label = QLabel("Welcome to GloveDataHub!")
        welcome_label.setFont(QFont("Montserrat", 20, QFont.Weight.Bold))
        welcome_label.setStyleSheet("color: #023E58; background-color: #CFDCE6; padding: 20px 0px 40px 20px;")
        
        welcome_layout.addWidget(welcome_label)
        
        # Application description
        description_text = (
            "This application will allow you to capture raw data from your haptic gloves.\n"
            "The steps to be performed in the following screens will be:"
        )
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QFont("Source Sans Pro", 16))
        description_label.setStyleSheet("color: #031729; background-color: #CFDCE6; padding: 0px 20px 40px 20px;")
        
        description_layout = QVBoxLayout()
        description_layout.addWidget(description_label)
        
        welcome_layout.addLayout(description_layout)

        # Step 1 to be performed
        step1_text = "1 • Calibration of haptic gloves"
        step1_label = QLabel(step1_text)
        step1_label.setFont(QFont("Source Sans Pro", 16, QFont.Weight.Bold))
        step1_label.setStyleSheet("color: #025885; background-color: #CFDCE6; padding: 0px 20px 40px 20px;")

        # Step 2 to be performed
        step2_text = "2 • Entering user data"
        step2_label = QLabel(step2_text)
        step2_label.setFont(QFont("Source Sans Pro", 16, QFont.Weight.Bold))
        step2_label.setStyleSheet("color: #025885; background-color: #CFDCE6; padding: 0px 20px 40px 20px;")
        
        # Step 3 to be performed
        step3_text = "3 • Data acquisition"
        step3_label = QLabel(step3_text)
        step3_label.setFont(QFont("Source Sans Pro", 16, QFont.Weight.Bold))
        step3_label.setStyleSheet("color: #025885; background-color: #CFDCE6; padding: 0px 20px 0px 20px;")
        
        steps_layout = QVBoxLayout()
        
        steps_layout.addWidget(step1_label)
        steps_layout.addWidget(step2_label)
        steps_layout.addWidget(step3_label)
        
        steps_layout.addStretch()
        
        welcome_layout.addLayout(steps_layout)
        
        welcome_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Add the welcome panel to the main window content layout
        self.main_window.add_content_widget(self.welcome_panel)
        
    def _set_buttons_layout(self):
        """
        Set up the layout for buttons on the welcome screen.
        """
        
        # Button to proceed
        next_button = CustomButton("Next", 0, 120, 40, 16)
        next_button.clicked.connect(self._show_next_screen)
        
        button_layout = QHBoxLayout()
        
        button_layout.addWidget(next_button)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        
        # Add the button to the main window buttons layout
        self.main_window.add_button(button_widget)

    def _show_next_screen(self):
        """
        Show the next screen after clicking the 'Next' button.
        """
        
        from calibration_screen import CalibrationScreen
        
        # Remove all the buttons from main window buttons layout
        self.main_window.clear_buttons_layout()
        
        self.calibration_screen = CalibrationScreen(self.main_window)
        
        # Set the calibration screen
        self.calibration_screen.set_calibration_screen()
        
        # Show the next screen
        self.main_window.show_content_widget("Next")