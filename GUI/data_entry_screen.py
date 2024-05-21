from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QFileDialog, QInputDialog
from custom_button import CustomButton
from window_manager import WindowManager
import sys
import os

# Aggiungi il percorso della directory 'Data-Acquisition' al PYTHONPATH
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
from user_data import UserData

class DataEntryScreen:
    is_first_time = True
    
    def __init__(self, main_window: WindowManager):
        self.main_window = main_window
        self.user_data = UserData()
        self.name_entry = None
        self.surname_entry = None
        self.code_entry = None
        self.path_entry = None
        self.saved_name = ""
        self.saved_surname = ""
        self.saved_code = ""
        self.saved_path = ""

        
    def set_data_entry_screen(self):
        #if DataEntryScreen.is_first_time:
        #    self._create_data_entry_widget()
        #    DataEntryScreen.is_first_time = not DataEntryScreen.is_first_time
        if DataEntryScreen.is_first_time:
            self._create_data_entry_widget()
            DataEntryScreen.is_first_time = False
            
        self._set_buttons_layout()
        
        
    def _create_data_entry_widget(self):  
        # Crea un pannello per contenere tutti i widget
        self.data_entry_panel = QtWidgets.QWidget()
        self.data_entry_panel.setStyleSheet("background-color: #E9E6DB;")
        self.data_entry_layout = QtWidgets.QVBoxLayout(self.data_entry_panel)
        
        # Descrizione sopra i campi
        description1_text = "Ensure name and surname and possibly also the code are correctly entered."
        description1_label = QtWidgets.QLabel(description1_text)
        description1_label.setWordWrap(True)
        description1_label.setFont(QtGui.QFont("Arial", 16))
        description1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 20px 20px 10px 20px;")
        self.data_entry_layout.addWidget(description1_label)
        
        # Layout per nome e cognome
        name_surname_layout = QtWidgets.QHBoxLayout()

        # Widget per il nome
        name_label = QtWidgets.QLabel("Name:")
        name_label.setFont(QtGui.QFont("Arial", 16))
        name_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 20px;")
        self.name_entry = QtWidgets.QLineEdit()
        self.name_entry.setFont(QtGui.QFont("Arial", 14))
        self.name_entry.setFixedWidth(200)
        self.name_entry.setStyleSheet("color: black;")  
        self.name_entry.setContentsMargins(20, 5, 10, 5)
        name_layout = QtWidgets.QVBoxLayout() 
        name_layout.addWidget(name_label)  
        name_layout.addWidget(self.name_entry) 
        name_surname_layout.addLayout(name_layout)

        # Widget per il cognome
        surname_label = QtWidgets.QLabel("Surname:")
        surname_label.setFont(QtGui.QFont("Arial", 16))
        surname_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 20px;")
        self.surname_entry = QtWidgets.QLineEdit()
        self.surname_entry.setFont(QtGui.QFont("Arial", 14))
        self.surname_entry.setStyleSheet("color: black;")
        self.surname_entry.setFixedWidth(200)
        self.surname_entry.setContentsMargins(20, 5, 10, 5)
        surname_layout = QtWidgets.QVBoxLayout()
        surname_layout.addWidget(surname_label)
        surname_layout.addWidget(self.surname_entry)
        name_surname_layout.addLayout(surname_layout)
        
        self.data_entry_layout.addLayout(name_surname_layout)
        
        # Widget per il codice opzionale
        code_label = QtWidgets.QLabel("Code (optional):")
        code_label.setFont(QtGui.QFont("Arial", 16))
        code_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 20px;")
        self.code_entry = QtWidgets.QLineEdit()
        self.code_entry.setFont(QtGui.QFont("Arial", 14))
        self.code_entry.setStyleSheet("color: black;")
        self.code_entry.setFixedWidth(200)
        self.code_entry.setContentsMargins(20, 5, 10, 5)
        code_layout = QtWidgets.QVBoxLayout()
        code_layout.addWidget(code_label)
        code_layout.addWidget(self.code_entry)
        self.data_entry_layout.addLayout(code_layout)

        # Widget per la path
        path_label = QtWidgets.QLabel("Path:")
        path_label.setFont(QtGui.QFont("Arial", 16))
        path_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 20px;")

        self.path_entry = QtWidgets.QLineEdit()
        self.path_entry.setFont(QtGui.QFont("Arial", 12))
        self.path_entry.setStyleSheet("color: black;")
        self.path_entry.setFixedWidth(300)
        self.path_entry.setContentsMargins(20, 5, 10, 5)
        
        browse_button = CustomButton("Browse", 155, 40)
        browse_button.clicked.connect(self._browse_path)

        # Use QVBoxLayout for label and QHBoxLayout for entry and button
        path_layout = QtWidgets.QVBoxLayout()
        
        path_entry_layout = QtWidgets.QHBoxLayout()
        path_entry_layout.addWidget(self.path_entry)
        path_entry_layout.addStretch()
        path_entry_layout.addWidget(browse_button)

        path_layout.addWidget(path_label)
        path_layout.addLayout(path_entry_layout)
        
        self.data_entry_layout.addLayout(path_layout) 

        # Aggiungi il panel al layout del contenuto principale
        self.main_window.add_content_widget(self.data_entry_panel)
        
    def _set_buttons_layout(self):
        # Bottone per tornare indietro
        back_button = CustomButton("Back", 140, 40)
        back_button.clicked.connect(self._show_previous_screen)
        
        # Bottone per procedere
        next_button = CustomButton("Next", 140, 40)
        next_button.clicked.connect(self._show_next_screen)
        
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(next_button)
        buttons_layout.addStretch()
        
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
    def _browse_path(self):
        folder_path = QFileDialog.getExistingDirectory(self.main_window, 'Select the destination folder')
        if folder_path:
            path = self.path_entry.setText(folder_path)
            self.user_data.set_path_directory(path)


    def _show_previous_screen(self):
        from calibration_screen import CalibrationScreen
        
        # Memorizza i valori dei campi
        self._save_field_values()

        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.calibration_screen = CalibrationScreen(self.main_window)
        
        self.calibration_screen.set_calibration_screen()

    def _show_next_screen(self):
        from data_acquisition_screen import DataAcquisitionScreen
        
        if self._check_entry_fields():

            # Memorizza i valori dei campi
            self._save_field_values()

            self.main_window.clear_buttons_layout()
            self.data_acquisition_screen = DataAcquisitionScreen(self.main_window, self.saved_name, self.saved_surname, self.saved_path)
            self.data_acquisition_screen.set_data_acquisition_screen()
            self.main_window.show_content_widget("Next")

    def _check_entry_fields(self):
        if not self.name_entry or not self.surname_entry or not self.code_entry or not self.path_entry:
            self._show_error_message("Form fields are not initialized.")
            return False

        name = self.name_entry.text().strip()  # Ottieni il nome inserito dall'utente
        surname = self.surname_entry.text().strip()  # Ottieni il cognome inserito dall'utente
        code = self.code_entry.text().strip()  # Ottieni il codice inserito dall'utente
        path = self.path_entry.text().strip() # Ottieni la path della directory indicata dall'utente

        errors = []

        if not name:
            errors.append("- Name cannot be empty.")
        if not surname:
            errors.append("- Surname cannot be empty.")
        if len(code) != 4 or not code.isdigit():
            errors.append("- Code must be a 4-digit number.")
        if not path:
            errors.append("- you must specify the directory")       
        if name == "" and surname == "" and code == "" and path != "":
            code = self.user_data.generate_random_code()
            self.code_entry.setText(code)
            self._show_information_message("the code has been generated automatically because the name and surname are missing")
            return True    
        if name != "" and surname != "" and path != "":
            return True

        try:
            self.user_data.set_name(name)
        except ValueError as e:
            errors.append(str(e))
        try:
            self.user_data.set_surname(surname)
        except ValueError as e:
            errors.append(str(e))
        try:
            self.user_data.set_code(code)
        except ValueError as e:
            errors.append(str(e))

        if errors:
            self._show_error_message("\n".join(errors))
            return False

        return True
    
    def _save_field_values(self):
        self.saved_name = self.name_entry.text().strip()
        self.saved_surname = self.surname_entry.text().strip()
        self.saved_code = self.code_entry.text().strip()
        self.saved_path = self.path_entry.text().strip()

    def _restore_field_values(self):
        self.name_entry.setText(self.saved_name)
        self.surname_entry.setText(self.saved_surname)
        self.code_entry.setText(self.saved_code)
        self.path_entry.setText(self.saved_path)    

    def _show_error_message(self, message):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, "Error", message)
        self._set_output_dialog_style(msg_box)
        msg_box.exec()

    def _show_information_message(self, message):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, "Information", message)
        self._set_output_dialog_style(msg_box)
        msg_box.exec()      

    def _set_output_dialog_style(self, dialog):
        if dialog:
            dialog.setStyleSheet("""
                QMessageBox {
                    color: black;
                    background-color: #E9E6DB;
                }
                QLabel {
                    color: black;
                }
                QPushButton {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #E9E6DB, stop:1 #CDE2CD);
                    color: black;
                    border: 2px solid #A3C293;
                    border-radius: 10px;
                    padding: 8px 10px;
                    min-width: 40px;
                }
                QPushButton:hover {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #CDE2CD, stop:1 #E9E6DB);
                    border-color: #89A06B;
                }
            """)