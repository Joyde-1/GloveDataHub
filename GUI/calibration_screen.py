from PyQt6 import QtWidgets, QtGui, QtCore
from custom_button import CustomButton

class CalibrationScreen():
    def __init__(self, main_window):
        self.main_window = main_window
        self._create_calibration_screen()
        self.main_window.create_sensecom_layout()

    def _create_calibration_screen(self):
        # Crea un pannello per contenere tutti i widget
        self.calibration_panel = QtWidgets.QWidget()
        self.calibration_panel.setStyleSheet("background-color: #E9E6DB;")
        self.calibration_layout = QtWidgets.QVBoxLayout(self.calibration_panel)
        
        # Descrizione dell'applicazione
        description_text = (
            "Activate the SenseCom application by clicking the button at the bottom center to calibrate your haptic gloves.\n"
        )
        description_label = QtWidgets.QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QtGui.QFont("Arial", 16))
        description_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 0px 20px 0px;")
        description_layout = QtWidgets.QVBoxLayout()
        description_layout.addWidget(description_label)
        self.calibration_layout.addLayout(description_layout)
        
        self.calibration_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.main_window.create_dynamic_content_layout()
        
        # Aggiungi il calibration panel al layout del contenuto principale
        self.main_window.add_dynamic_content(self.calibration_panel)
        
        # Bottone per tornare indietro
        back_button = CustomButton("Back", 140, 40)
        back_button.clicked.connect(self._show_welcome_screen)
        
        # Bottone per procedere
        next_button = CustomButton("Next", 140, 40)
        next_button.clicked.connect(self._show_data_entry_screen)
        
        self.main_window.create_button_layout()
        
        self.main_window.add_button(back_button)
        self.main_window.add_button(next_button)        

    def _show_welcome_screen(self):
        # Import ritardato per evitare import circolare tra classe start_calibration_screen e classe welcome_screen
        from welcome_screen import WelcomeScreen
        
        self.main_window.clear_content_layout()
        
        self.welcome_screen = WelcomeScreen(self.main_window)

    def _show_data_entry_screen(self):
        from data_entry_screen import DataEntryScreen
        
        self.main_window.clear_dynamic_content()
        
        self.main_window.clear_button_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
