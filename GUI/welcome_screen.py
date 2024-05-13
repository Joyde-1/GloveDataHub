from PyQt6 import QtWidgets, QtGui, QtCore
from window_manager import WindowManager
#from calibration_screen import CalibrationScreen

class WelcomeScreen:
    def __init__(self, main_window):
        self.main_window = main_window
        self._create_welcome_screen()

    def _create_welcome_screen(self):
        # Crea un pannello per contenere tutti i widget
        self.welcome_panel = QtWidgets.QWidget(self.main_window)
        self.welcome_panel.setStyleSheet("background-color: #E9E6DB;")
        self.layout = QtWidgets.QVBoxLayout(self.welcome_panel)
        self.main_window.setCentralWidget(self.welcome_panel)

        # Titolo di benvenuto
        welcome_label = QtWidgets.QLabel("Welcome to GloveDataHub!")
        welcome_label.setFont(QtGui.QFont("Arial", 24, QtGui.QFont.Weight.Bold))
        welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px;")
        self.layout.addWidget(welcome_label)

        # Descrizione dell'applicazione
        description_text = (
            "This application will allow you to capture raw data from your haptic gloves.\n"
            "The steps to be performed in the following screens will be:"
        )
        description_label = QtWidgets.QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QtGui.QFont("Arial", 20))
        description_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px;")
        self.layout.addWidget(description_label, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        # Step 1 da compiere
        step1_text = "1 • Calibration of haptic gloves"
        step1_label = QtWidgets.QLabel(step1_text)
        step1_label.setFont(QtGui.QFont("Arial", 20))
        step1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 5px;")
        self.layout.addWidget(step1_label, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        # Step 2 da compiere
        step2_text = "2 • Entering user data"
        step2_label = QtWidgets.QLabel(step2_text)
        step2_label.setFont(QtGui.QFont("Arial", 20))
        step2_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 5px;")
        self.layout.addWidget(step2_label, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        # Step 3 da compiere
        step3_text = "3 • Data acquisition"
        step3_label = QtWidgets.QLabel(step3_text)
        step3_label.setFont(QtGui.QFont("Arial", 20))
        step3_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 5px;")
        self.layout.addWidget(step3_label, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        # Bottone per procedere
        next_button = QtWidgets.QPushButton("Next")
        next_button.setFont(QtGui.QFont("Arial", 18))
        next_button.setStyleSheet("background-color: #E9E6DB; color: black; padding: 20px 40px;")
        next_button.clicked.connect(self._show_calibration_screen)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(next_button)
        self.layout.addLayout(button_layout)

    def _show_calibration_screen(self):
        # Cancella tutto il contenuto attuale
        self.main_window.setCentralWidget(None)
        #self.start_calilbration_screen = CalibrationScreen(self.main_window, self.win)
