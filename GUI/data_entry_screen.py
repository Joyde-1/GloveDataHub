from PyQt6 import QtWidgets, QtGui, QtCore
from custom_button import CustomButton

class DataEntryScreen:
    def __init__(self, main_window):
        self.main_window = main_window
        self._create_data_entry_screen()
    
    def _create_data_entry_screen(self):  
        # Crea un pannello per contenere tutti i widget
        self.data_entry_panel = QtWidgets.QWidget()
        self.data_entry_panel.setStyleSheet("background-color: #E9E6DB;")
        self.data_entry_layout = QtWidgets.QVBoxLayout(self.data_entry_panel)
        
        # Descrizione dell'applicazione
        description1_text = (
            "Enter user data \n"
        )
        description1_label = QtWidgets.QLabel(description1_text)
        description1_label.setWordWrap(True)
        description1_label.setFont(QtGui.QFont("Arial", 16))
        description1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 0px 20px 0px;")
        description1_layout = QtWidgets.QVBoxLayout()
        description1_layout.addWidget(description1_label)
        self.data_entry_layout.addLayout(description1_layout)
        
        # Widget per il nome
        name_label = QtWidgets.QLabel("Name:")
        name_label.setFont(QtGui.QFont("Arial", 16))
        self.name_entry = QtWidgets.QLineEdit()
        self.name_entry.setFont(QtGui.QFont("Arial", 14))
        self.name_entry.setFixedWidth(200)  # Larghezza adeguata per l'input
        name_layout = QtWidgets.QVBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_entry)
        self.data_entry_layout.addLayout(name_layout)
        
        # Widget per il cognome
        surname_label = QtWidgets.QLabel("Surname:")
        surname_label.setFont(QtGui.QFont("Arial", 16))
        self.surname_entry = QtWidgets.QLineEdit()
        self.surname_entry.setFont(QtGui.QFont("Arial", 14))
        self.surname_entry.setFixedWidth(200)
        surname_layout = QtWidgets.QVBoxLayout()
        surname_layout.addWidget(surname_label)
        surname_layout.addWidget(self.surname_entry)
        self.data_entry_layout.addLayout(surname_layout)

        # Widget per la durata
        duration_label = QtWidgets.QLabel("Duration:")
        duration_label.setFont(QtGui.QFont("Arial", 16))
        self.duration_entry = QtWidgets.QLineEdit()
        self.duration_entry.setFont(QtGui.QFont("Arial", 14))
        self.duration_entry.setFixedWidth(100)
        duration_layout = QtWidgets.QVBoxLayout()
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(self.duration_entry)
        self.data_entry_layout.addLayout(duration_layout)
        
        # Descrizione dell'applicazione
        description2_text = (
            "Ensure name and surname are entered, specify measurement duration, and complete calibration before starting.\n"
        )
        description2_label = QtWidgets.QLabel(description2_text)
        description2_label.setFont(QtGui.QFont("Arial", 16))
        description2_label.setWordWrap(True)
        description2_layout = QtWidgets.QHBoxLayout()
        description2_layout.addWidget(description2_label)
        self.data_entry_layout.addLayout(description2_layout)
        
        self.data_entry_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        
        #self.main_window.create_dynamic_content_layout()
        
        # Aggiungi il calibration panel al layout del contenuto principale
        self.main_window.add_dynamic_content(self.data_entry_panel)
        
        # Bottone per tornare indietro
        back_button = CustomButton("Back", 140, 40)
        back_button.clicked.connect(self._show_calibration_screen)
        
        # Bottone per procedere
        next_button = CustomButton("Next", 140, 40)
        next_button.clicked.connect(self._show_data_acquisition_screen)
        
        #self.main_window.create_button_layout()
        
        self.main_window.add_button(back_button)
        self.main_window.add_button(next_button)

    
    def _show_calibration_screen(self):
        from calibration_screen import CalibrationScreen
        
        # Cancella tutto il contenuto attuale
        self.main_window.clear_dynamic_content()
        
        self.main_window.clear_button_layout()
        
        self.start_calibration_screen = CalibrationScreen(self.main_window)

    def _show_data_acquisition_screen(self):
        from data_entry_screen import DataEntryScreen
        
        self.main_window.clear_dynamic_content()
        
        self.main_window.clear_button_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)