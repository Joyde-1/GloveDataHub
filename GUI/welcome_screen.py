from PyQt6 import QtWidgets, QtGui, QtCore
from window_manager import WindowManager
from custom_button import CustomButton

class WelcomeScreen:
    is_first_time = True
    
    def __init__(self, main_window: WindowManager):
        self.main_window = main_window
        
    def set_welcome_screen(self):
        if WelcomeScreen.is_first_time:
            self._create_welcome_widget()
            WelcomeScreen.is_first_time = not WelcomeScreen.is_first_time
            
        self._set_buttons_layout()

    def _create_welcome_widget(self):
        # Crea un pannello per contenere tutti i widget
        self.welcome_panel = QtWidgets.QWidget()
        self.welcome_panel.setStyleSheet("background-color: #E9E6DB;")
        self.welcome_layout = QtWidgets.QVBoxLayout(self.welcome_panel)
        
        # Titolo di benvenuto
        welcome_label = QtWidgets.QLabel("Welcome to GloveDataHub!")
        welcome_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Weight.Bold))
        # welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 20px 0px 30px 20px;")
        title_layout = QtWidgets.QVBoxLayout()
        title_layout.addWidget(welcome_label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        # title_layout.addStretch()
        self.welcome_layout.addLayout(title_layout)
        
        # Descrizione dell'applicazione
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

        # Step 1 da compiere
        step1_text = "1 • Calibration of haptic gloves"
        step1_label = QtWidgets.QLabel(step1_text)
        step1_label.setFont(QtGui.QFont("Arial", 16))
        step1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 20px 40px 20px;")

        # Step 2 da compiere
        step2_text = "2 • Entering user data"
        step2_label = QtWidgets.QLabel(step2_text)
        step2_label.setFont(QtGui.QFont("Arial", 16))
        step2_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 20px 40px 20px;")
        
        # Step 3 da compiere
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
        
        # Aggiungi il welcome panel al layout del contenuto principale
        self.main_window.add_content_widget(self.welcome_panel)
        
        # self.main_window.content_layout.addWidget(self.welcome_panel)
        
    def _set_buttons_layout(self):
        # Bottone per procedere
        next_button = CustomButton("Next", 140, 40)
        next_button.clicked.connect(self._show_next_screen)
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(next_button)
        button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(button_layout)
        
        self.main_window.add_button(button_widget)

    def _show_next_screen(self):
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
