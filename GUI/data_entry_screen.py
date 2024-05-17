from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QFileDialog, QInputDialog
from custom_button import CustomButton
import sys
import os

class DataEntryScreen:
    def __init__(self, main_window):
        self.main_window = main_window
        self._create_data_entry_screen()
    
    def _create_data_entry_screen(self):  
        # Crea un pannello per contenere tutti i widget
        self.data_entry_panel = QtWidgets.QWidget()
        self.data_entry_panel.setStyleSheet("background-color: #E9E6DB;")
        self.data_entry_layout = QtWidgets.QVBoxLayout(self.data_entry_panel)
        
        # Descrizione sopra i campi
        description1_text = "Ensure name and surname are entered, specify measurement duration, and complete calibration before starting."
        description1_label = QtWidgets.QLabel(description1_text)
        description1_label.setWordWrap(True)
        description1_label.setFont(QtGui.QFont("Arial", 16))
        description1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 20px 20px 10px 20px;")
        self.data_entry_layout.addWidget(description1_label)

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
        self.data_entry_layout.addLayout(name_layout)

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
        self.data_entry_layout.addLayout(surname_layout)

        # Widget per la durata
        duration_label = QtWidgets.QLabel("Duration:")
        duration_label.setFont(QtGui.QFont("Arial", 16))
        duration_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 20px;")
        self.duration_entry = QtWidgets.QLineEdit()
        self.duration_entry.setFont(QtGui.QFont("Arial", 14))
        self.duration_entry.setStyleSheet("color: black;")
        self.duration_entry.setFixedWidth(200)
        self.duration_entry.setContentsMargins(20, 5, 10, 5)
        duration_layout = QtWidgets.QVBoxLayout()
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(self.duration_entry)
        self.data_entry_layout.addLayout(duration_layout)

        # Aggiungi il panel al layout del contenuto principale
        self.main_window.add_dynamic_content(self.data_entry_panel)
        
        # Bottone per tornare indietro
        back_button = CustomButton("Back", 140, 40)
        back_button.clicked.connect(self._show_calibration_screen)
        
        # Bottone per procedere
        next_button = CustomButton("Next", 140, 40)
        next_button.clicked.connect(self._show_data_acquisition_screen)

        start_measurement_button = CustomButton("Start Measurement", 280, 40)
        start_measurement_button.clicked.connect(self._start_measurement)
        
        self.main_window.add_button(back_button)
        self.main_window.add_button(next_button)
        self.main_window.add_button(start_measurement_button)

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
    
    def _start_measurement(self):
        # Aggiungi il percorso della directory 'API' al PYTHONPATH
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
        from exe_manager import ExeManager

        # Chiedi all'utente di selezionare una cartella
        folder_path = QFileDialog.getExistingDirectory(self.main_window, 'Select the destination folder')

        if folder_path:
            # Creare la finestra di dialogo per inserire la durata
            input_dialog = QInputDialog(self.main_window)
            input_dialog.setWindowTitle("Measurement duration")
            input_dialog.setLabelText("Enter the duration (in minutes):")
            input_dialog.setIntRange(1, 1000)
            input_dialog.setIntValue(1)

            # Applica lo stile alla finestra di dialogo
            self._set_input_dialog_style(input_dialog)

            # Mostra la finestra di dialogo e ottieni il valore inserito dall'utente
            ok_pressed = input_dialog.exec()

            if ok_pressed:
                duration = input_dialog.intValue()
                # Mostra la durata nel campo duration_entry
                self.duration_entry.setText(str(duration))

                # Se l'utente ha confermato la durata, esegui lo script con i parametri forniti
                self.duration = duration

                # Ottieni nome e cognome inseriti dall'utente
                name = self.name_entry.text().strip()
                surname = self.surname_entry.text().strip()

                # Genera il nome del file CSV
                csv_filename = f"{name}_{surname}.csv"
                csv_path = os.path.join(folder_path, csv_filename)
                
                # Esegui lo script con il percorso CSV e la durata
                self.script = ExeManager().run_script(csv_path, duration)

    
    def _set_input_dialog_style(self, input_dialog):
        if input_dialog:
            input_dialog.setStyleSheet("""
                QInputDialog {
                    color: black;
                }
                QLabel {
                    color: black;
                }
                
                QSpinBox {
                    color: black; /* Colore dei numeri */
                }
                QPushButton {
                    color: black;
                    background-color: #E9E6DB;
                    border: 1px solid #000000;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #CCCCCC;
                }
            """)

