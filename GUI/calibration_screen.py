from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox
from window_manager import WindowManager
from custom_button import CustomButton

class CalibrationScreen():
    is_first_time = True
    
    def __init__(self, main_window: WindowManager):
        self.main_window = main_window
        
    def set_calibration_screen(self):
        if CalibrationScreen.is_first_time:
            self._create_calibration_widget()
            CalibrationScreen.is_first_time = not CalibrationScreen.is_first_time
            
        if not WindowManager.is_sensecom_layout:
            self.main_window.create_sensecom_widget()
            
        self._set_buttons_layout()

    def _create_calibration_widget(self):
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
        
        self.calibration_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.main_window.add_content_widget(self.calibration_panel)
        
        """ if not WindowManager.is_dynamic_content_layout:
            self.main_window.create_dynamic_content_layout()
        
        # Aggiungi il calibration panel al layout del contenuto principale
        self.main_window.add_dynamic_content(self.calibration_panel) """
        
    def _set_buttons_layout(self):
        # Bottone per tornare indietro
        back_button = CustomButton("Back", 140, 40)
        back_button.clicked.connect(self._show_previous_screen)
        
        # Bottone per procedere
        next_button = CustomButton("Next", 140, 40)
        next_button.clicked.connect(self._show_next_screen)
        
        buttons_layout = QtWidgets.QHBoxLayout()
        # button_layout.addStretch()
        buttons_layout.addWidget(back_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(next_button)
        # buttons_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
        """ if not WindowManager.is_button_layout:
            self.main_window.create_button_layout() """
        
        #self.main_window.add_button(back_button)
        #self.main_window.add_button(next_button)

    def _show_previous_screen(self):
        # Import ritardato per evitare import circolare tra classe start_calibration_screen e classe welcome_screen
        from welcome_screen import WelcomeScreen
    
        # self.main_window.clear_content_layout()
        
        self.main_window.close_sensecom_widget()
        
        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.welcome_screen = WelcomeScreen(self.main_window)
        
        self.welcome_screen.set_welcome_screen()
        

    def _show_next_screen(self):
        from data_entry_screen import DataEntryScreen
        
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        self.data_entry_screen.set_data_entry_screen()
        
        self.main_window.show_content_widget("Next") 