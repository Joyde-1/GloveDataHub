from PyQt6 import QtWidgets, QtGui, QtCore
from window_manager import WindowManager
from custom_button import CustomButton

class WelcomeScreen:
    """
    Class to manage the welcome screen of the application.

    Attributes
    ----------
    is_first_time : bool 
        Flag to indicate if it's the first time the welcome screen is being set.
    main_window : WindowManager 
        The main window manager instance.
    welcome_panel : QtWidgets.QWidget 
        The main widget for the welcome screen.
    welcome_layout : QtWidgets.QVBoxLayout 
        The layout for the welcome screen.
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
        if WelcomeScreen.is_first_time:
            self._create_welcome_widget()
            WelcomeScreen.is_first_time = not WelcomeScreen.is_first_time
            
        self._set_buttons_layout()

    def _create_welcome_widget(self):
        """
        Create the welcome screen widget and its components.
        """
        # Create a panel to contain all widgets
        self.welcome_panel = QtWidgets.QWidget()
        self.welcome_panel.setStyleSheet("background-color: #E9E6DB;")
        self.welcome_layout = QtWidgets.QVBoxLayout(self.welcome_panel)
        
        # Welcome title
        welcome_label = QtWidgets.QLabel("Welcome to GloveDataHub!")
        welcome_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Weight.Bold))
        #welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 50px 0px 40px 20px;")
        
        self.welcome_layout.addWidget(welcome_label)
        
        # Application description
        description_text = (
            "This application will allow you to capture raw data from your haptic gloves.\n"
            "The steps to be performed in the following screens will be:"
        )
        description_label = QtWidgets.QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QtGui.QFont("Arial", 16))
        description_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 20px 40px 20px;")
        description_layout = QtWidgets.QVBoxLayout()
        # description_layout.addWidget(description_label, alignment=QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        description_layout.addWidget(description_label)
        # description_layout.addStretch()
        self.welcome_layout.addLayout(description_layout)

        # Step 1 to be performed
        step1_text = "1 • Calibration of haptic gloves"
        step1_label = QtWidgets.QLabel(step1_text)
        step1_label.setFont(QtGui.QFont("Arial", 16))
        step1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 20px 40px 20px;")

        # Step 2 to be performed
        step2_text = "2 • Entering user data"
        step2_label = QtWidgets.QLabel(step2_text)
        step2_label.setFont(QtGui.QFont("Arial", 16))
        step2_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 20px 40px 20px;")
        
        # Step 3 to be performed
        step3_text = "3 • Data acquisition"
        step3_label = QtWidgets.QLabel(step3_text)
        step3_label.setFont(QtGui.QFont("Arial", 16))
        step3_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 20px 0px 20px;")
        
        steps_layout = QtWidgets.QVBoxLayout()
        steps_layout.addWidget(step1_label)
        #steps_layout.addStretch()
        steps_layout.addWidget(step2_label)
        #steps_layout.addStretch()
        steps_layout.addWidget(step3_label)
        steps_layout.addStretch()
        self.welcome_layout.addLayout(steps_layout)
        
        self.welcome_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Add the welcome panel to the main window content layout
        self.main_window.add_content_widget(self.welcome_panel)
        
        # self.main_window.content_layout.addWidget(self.welcome_panel)
        
    def _set_buttons_layout(self):
        """
        Set up the layout for buttons on the welcome screen.
        """
       # Button to proceed
        next_button = CustomButton("Next", 120, 40, 16)
        next_button.clicked.connect(self._show_next_screen)
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(next_button)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(button_layout)
        
        self.main_window.add_button(button_widget)

    def _show_next_screen(self):
        """
        Show the next screen after clicking the 'Next' button.
        """
        from calibration_screen import CalibrationScreen
        
        self.main_window.clear_buttons_layout()
        
        self.calibration_screen = CalibrationScreen(self.main_window)
        
        self.calibration_screen.set_calibration_screen()
        
        self.main_window.show_content_widget("Next")
        
        # Cancella tutto il contenuto attuale
        # self.main_window.clear_content_layout()
        #self.main_window.init_calibration_screen()
        # self.main_window.setCentralWidget(None)
        # self.calilbration_screen = CalibrationScreen(self.main_window)
