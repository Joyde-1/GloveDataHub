from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QFileDialog, QInputDialog
from custom_button import CustomButton
from window_manager import WindowManager
import sys
import os

# Aggiungi il percorso della directory 'Data-Acquisition' al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))

from user_data import UserData
from duration_time import DurationTime
from exe_manager import ExeManager

class DataAcquisitionScreen:
    is_first_time = True
    
    duration_entry = None
    
    def __init__(self, main_window: WindowManager, user_data: UserData):
        self.main_window = main_window
        self.user_data = user_data
        self.duration_time = DurationTime()
        self.exe_manager = ExeManager()
        self.stop_measurement_button = None  # Variabile per il pulsante di stop
        
    def set_data_acquisition_screen(self):
        if DataAcquisitionScreen.is_first_time:
            self._create_data_acquisition_widget()
            DataAcquisitionScreen.is_first_time = not DataAcquisitionScreen.is_first_time
            
        self._set_buttons_layout()
    
    def _create_data_acquisition_widget(self):  
        # Crea un pannello per contenere tutti i widget
        self.data_acquisition_panel = QtWidgets.QWidget()
        self.data_acquisition_panel.setStyleSheet("background-color: #E9E6DB;")
        self.data_acquisition_layout = QtWidgets.QVBoxLayout(self.data_acquisition_panel)
        # self.data_acquisition_layout.setContentsMargins(20, 40, 20, 20)

        # Spaziatore per sollevare il contenuto
        # self.data_acquisition_layout.addStretch(2)
        
        # Descrizione sopra i campi
        description_text = "Data acquisition."
        description_label = QtWidgets.QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QtGui.QFont("Arial", 16))
        description_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 20px 10px 20px;")
        description_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.data_acquisition_layout.addWidget(description_label)
        
        # Layout per il tempo
        time_layout = QtWidgets.QHBoxLayout()

        # Widget per la durata
        duration_label = QtWidgets.QLabel("Duration:")
        duration_label.setFont(QtGui.QFont("Arial", 16))
        duration_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 10px 10px 10px 20px;")
        
        DataAcquisitionScreen.duration_entry = QtWidgets.QLineEdit()
        DataAcquisitionScreen.duration_entry.setFont(QtGui.QFont("Arial", 14))
        DataAcquisitionScreen.duration_entry.setStyleSheet("color: black;")
        DataAcquisitionScreen.duration_entry.setFixedWidth(200)
        DataAcquisitionScreen.duration_entry.setContentsMargins(20, 5, 10, 5)
        
        duration_layout = QtWidgets.QVBoxLayout()
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(DataAcquisitionScreen.duration_entry)
        
        time_layout.addLayout(duration_layout)
        time_layout.addStretch(1)  # Sposta verso sinistra

        self.data_acquisition_layout.addLayout(time_layout)

        # Spaziatore per mantenere il contenuto centrale
        self.data_acquisition_layout.addStretch(5)
        
        # Aggiungi il panel al layout del contenuto principale
        self.main_window.add_content_widget(self.data_acquisition_panel)
        
    def _set_buttons_layout(self):
        # Bottone per tornare indietro
        self.back_button = CustomButton("Back", 120, 40, 16)
        self.back_button.clicked.connect(self._show_previous_screen)
        
        # Bottone per la misurazione
        self.measurement_button = CustomButton("Start Measurement", 240, 40, 16)
        self.measurement_button.clicked.connect(self._start_measurement)
        
        # Bottone per procedere
        self.next_button = CustomButton("Next", 120, 40, 16)
        self.next_button.clicked.connect(self._show_next_screen)
        
        self.buttons_layout = QtWidgets.QHBoxLayout()
        
        self.buttons_layout.addWidget(self.back_button, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.measurement_button, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.next_button, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        
        # Impostare lo stato iniziale dei pulsanti
        self.next_button.hide()
        
        self.buttons_layout.setAlignment(self.back_button, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.button_widget = QtWidgets.QWidget()
        self.button_widget.setLayout(self.buttons_layout)
        
        self.main_window.add_button(self.button_widget)

    def _show_previous_screen(self):
        from data_entry_screen import DataEntryScreen
        
        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        self.data_entry_screen.set_data_entry_screen()

    def _show_next_screen(self):
        from final_screen import FinalScreen
        
        self.main_window.clear_buttons_layout()
        
        self.final_screen = FinalScreen(self.main_window)
        
        self.final_screen.set_final_screen()
        
        self.main_window.show_content_widget("Next")

    def _start_measurement(self):       
        self._save_duration_field()
        
        if not self._is_error_message():
            self.path_to_csv = self.user_data.create_path_csv()
            
            self.total_time = self.duration_time.get_time_sec()
            
            self.exe_manager.start_script(self.path_to_csv, self.total_time)
            
            # TODO: aggiungere inizio cronometro
            
            self.back_button.hide()
            self.measurement_button.setText("Stop")
            self.measurement_button.clicked.disconnect(self._start_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)
        else:
            self._show_error_message()
        
    def _stop_measurement(self):
        # TODO: aggiungere controllo sul tempo
        if self.exe_manager.is_script_running():
            
            self.exe_manager.close_script()
            
            self.measurement_button.setText("Restart")
            self.measurement_button.clicked.disconnect(self._stop_measurement)
            self.measurement_button.clicked.connect(self._restart_measurement)
            self.next_button.show()
            self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignLeft)
            self.buttons_layout.setAlignment(self.next_button, QtCore.Qt.AlignmentFlag.AlignRight)
        
    def _restart_measurement(self):
        self._save_duration_field()
        
        if not self._is_error_message():
            self.total_time = self.duration_time.get_time_sec()
            
            self.exe_manager.start_script(self.path_to_csv, self.total_time)
            
            # TODO: aggiungere inizio cronometro
            
            self.measurement_button.setText("Stop")
            self.measurement_button.clicked.disconnect(self._restart_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            self.next_button.hide()
            self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)

    def _save_duration_field(self):
        self.field_error = ""
        
        try:
            duration = DataAcquisitionScreen.duration_entry.text()  # Ottieni la durata inserita dall'utente
        except AttributeError as e:
            duration = ""
            
        if duration == "":
            duration = None
        else:
            duration = int(duration)
            
        try:
            self.duration_time.set_time_min(duration)
        except ValueError as e:
            self.field_error += "• " + str(e)
    
    def _is_error_message(self):
        if self.field_error != "":
            self.field_error = "Please fix the following errors:\n" + self.field_error
            return True
        else:
            return False

    def _show_error_message(self):
        error_msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, "Error", self.fields_errors.strip())
        self._set_output_dialog_style(error_msg_box)
        error_msg_box.exec()

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
