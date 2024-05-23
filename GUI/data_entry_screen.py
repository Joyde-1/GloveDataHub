from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QFileDialog, QInputDialog
from custom_button import CustomButton
from window_manager import WindowManager
import sys
import os
from pathlib import Path

# Aggiungi il percorso della directory 'Data-Acquisition' al PYTHONPATH
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
from user_data import UserData

class DataEntryScreen:
    is_first_time = True
    
    name_entry = None
    surname_entry = None
    code_entry = None
    path_directory_entry = None
    
    def __init__(self, main_window: WindowManager):
        self.main_window = main_window
        self.user_data = UserData()

    def set_data_entry_screen(self):
        if DataEntryScreen.is_first_time:
            self._create_data_entry_widget()
            DataEntryScreen.is_first_time = not DataEntryScreen.is_first_time
            
        self._set_buttons_layout()
        
        
    def _create_data_entry_widget(self):  
        # Crea un pannello per contenere tutti i widget
        self.data_entry_panel = QtWidgets.QWidget()
        self.data_entry_panel.setStyleSheet("background-color: #E9E6DB;")
        self.data_entry_layout = QtWidgets.QVBoxLayout(self.data_entry_panel)
        
        # Descrizione sopra i campi
        description_text = (
            "Enter the user data in the corresponding \n"
            "fields. \n"
            "If you do not want to specify the user's \n"
            "first and last name, leave these two \n"
            "fields empty and the system will generate \n"
            "a 4-digit code to assign to the user. \n"
        )
        description_label = QtWidgets.QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QtGui.QFont("Arial", 16))
        description_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 0px 10px;")
        
        self.data_entry_layout.addWidget(description_label)
        
        # Layout per nome e cognome
        name_surname_layout = QtWidgets.QHBoxLayout()

        # Widget per il nome
        name_label = QtWidgets.QLabel("Name:")
        name_label.setFont(QtGui.QFont("Arial", 16))
        name_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 20px 10px 10px;")
        name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        DataEntryScreen.name_entry = QtWidgets.QLineEdit()
        DataEntryScreen.name_entry.setFont(QtGui.QFont("Arial", 14))
        DataEntryScreen.name_entry.setFixedWidth(200)
        DataEntryScreen.name_entry.setStyleSheet("color: black;")  
        DataEntryScreen.name_entry.setContentsMargins(10, 5, 20, 5)
        
        name_layout = QtWidgets.QVBoxLayout() 
        
        name_layout.addWidget(name_label)  
        name_layout.addWidget(DataEntryScreen.name_entry) 
        name_layout.addStretch()
        #name_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        name_surname_layout.addLayout(name_layout)

        # Widget per il cognome
        surname_label = QtWidgets.QLabel("Surname:")
        surname_label.setFont(QtGui.QFont("Arial", 16))
        surname_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 20px;")
        
        DataEntryScreen.surname_entry = QtWidgets.QLineEdit()
        DataEntryScreen.surname_entry.setFont(QtGui.QFont("Arial", 14))
        DataEntryScreen.surname_entry.setStyleSheet("color: black;")
        DataEntryScreen.surname_entry.setFixedWidth(200)
        DataEntryScreen.surname_entry.setContentsMargins(20, 5, 10, 5)
        
        surname_layout = QtWidgets.QVBoxLayout()
        surname_layout.addWidget(surname_label)
        surname_layout.addWidget(DataEntryScreen.surname_entry)
        surname_layout.addStretch()
        
        name_surname_layout.addLayout(surname_layout)
        
        name_surname_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.data_entry_layout.addLayout(name_surname_layout)
        
        # Widget per il codice opzionale
        code_label = QtWidgets.QLabel("Code (optional):")
        code_label.setFont(QtGui.QFont("Arial", 16))
        code_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 10px;")
        
        DataEntryScreen.code_entry = QtWidgets.QLineEdit()
        DataEntryScreen.code_entry.setFont(QtGui.QFont("Arial", 14))
        DataEntryScreen.code_entry.setStyleSheet("color: black;")
        DataEntryScreen.code_entry.setFixedWidth(100)
        DataEntryScreen.code_entry.setContentsMargins(10, 5, 10, 5)
        
        code_layout = QtWidgets.QVBoxLayout()
        
        code_layout.addWidget(code_label)
        code_layout.addWidget(DataEntryScreen.code_entry)
        
        self.data_entry_layout.addLayout(code_layout)

        # Widget per la path
        path_directory_label = QtWidgets.QLabel("Path:")
        path_directory_label.setFont(QtGui.QFont("Arial", 16))
        path_directory_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 10px;")

        DataEntryScreen.path_directory_entry = QtWidgets.QLineEdit()
        DataEntryScreen.path_directory_entry.setText(str(Path.home() / "Documents"))
        DataEntryScreen.path_directory_entry.setFont(QtGui.QFont("Arial", 12))
        DataEntryScreen.path_directory_entry.setStyleSheet("color: black;")
        DataEntryScreen.path_directory_entry.setFixedWidth(335)
        DataEntryScreen.path_directory_entry.setContentsMargins(10, 5, 40, 5)
        
        browse_button = CustomButton("Browse", 120, 30, 14)
        browse_button.clicked.connect(self._browse_path)

        # Use QVBoxLayout for label and QHBoxLayout for entry and button
        path_directory_layout = QtWidgets.QVBoxLayout()
        
        path_directory_entry_layout = QtWidgets.QHBoxLayout()
        path_directory_entry_layout.addWidget(DataEntryScreen.path_directory_entry)
        path_directory_entry_layout.addStretch()
        path_directory_entry_layout.addWidget(browse_button)

        path_directory_layout.addWidget(path_directory_label)
        path_directory_layout.addLayout(path_directory_entry_layout)
        
        self.data_entry_layout.addLayout(path_directory_layout)

        # Aggiungi il panel al layout del contenuto principale
        self.main_window.add_content_widget(self.data_entry_panel)
        
    def _set_buttons_layout(self):
        # Bottone per tornare indietro
        back_button = CustomButton("Back", 120, 40, 16)
        back_button.clicked.connect(self._show_previous_screen)
        
        # Bottone per procedere
        next_button = CustomButton("Next", 120, 40, 16)
        next_button.clicked.connect(self._show_next_screen)
        
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(next_button)
        
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
    def _browse_path(self):
        # Ottieni il percorso della cartella Documenti
        documents_path = str(Path.home() / "Documents")
        
        # Apri il QFileDialog partendo dalla cartella Documenti
        path_directory = QFileDialog.getExistingDirectory(self.main_window, 'Select the destination folder', documents_path)

        if path_directory:
            DataEntryScreen.path_directory_entry.setText(path_directory)

    def _show_previous_screen(self):
        from calibration_screen import CalibrationScreen
        
        # Memorizza i valori dei campi
        # self._save_field_values()

        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.calibration_screen = CalibrationScreen(self.main_window)
        
        self.calibration_screen.set_calibration_screen()

    def _show_next_screen(self):
        from data_acquisition_screen import DataAcquisitionScreen
        
        self._save_fields_values()
        
        if not self._is_error_message():
            if self.info_message != "":
                self._show_information_message()
                
            self.main_window.clear_buttons_layout()
            self.data_acquisition_screen = DataAcquisitionScreen(self.main_window, self.user_data)
            self.data_acquisition_screen.set_data_acquisition_screen()
            self.main_window.show_content_widget("Next")
        else:
            self._show_error_message()

    def _save_fields_values(self):
        self.fields_errors = ""
        self.info_message = ""

        name = DataEntryScreen.name_entry.text().strip()  # Ottieni il nome inserito dall'utente
        surname = DataEntryScreen.surname_entry.text().strip()  # Ottieni il cognome inserito dall'utente
        code = DataEntryScreen.code_entry.text() # Ottieni il codice inserito dall'utente
        path_directory = DataEntryScreen.path_directory_entry.text() # Ottieni la path della directory indicata dall'utente
            
        if name == "" and surname == "" and code == "" and self.fields_errors == "":
            code = self.user_data.generate_random_code()
            DataEntryScreen.code_entry.setText(code)
            self.info_message = (
                "The code has been generated automatically \n"
                "because the name and surname are missing"
            )

        try:
            self.user_data.set_name(name)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
        
        try:
            self.user_data.set_surname(surname)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
            
        try:
            self.user_data.set_code(code)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
        """ except ValueError as e:
            self.fields_errors += "• " + str(e) """
            
        try:
            self.user_data.set_path_directory(path_directory)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
        
    def _is_error_message(self):
        if self.fields_errors != "":
            self.fields_errors = "Please fix the following errors:\n" + self.fields_errors
            return True
        else:
            return False  

    def _show_error_message(self):
        error_msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, "Error", self.fields_errors.strip())
        self._set_output_dialog_style(error_msg_box)
        error_msg_box.exec()

    def _show_information_message(self):
        info_msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, "Information", self.info_message)
        self._set_output_dialog_style(info_msg_box)
        info_msg_box.exec()      

    def _set_output_dialog_style(self, dialog):
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