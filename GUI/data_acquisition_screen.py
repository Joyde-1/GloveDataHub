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

class DataAcquisitionScreen:
    is_first_time = True
    
    def __init__(self, main_window: WindowManager, user_data: UserData):
        self.main_window = main_window
        self.user_data = user_data
        self.duration_time = DurationTime()
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
        self.data_acquisition_layout.setContentsMargins(20, 40, 20, 20)

        # Spaziatore per sollevare il contenuto
        self.data_acquisition_layout.addStretch(2)
        
        # Descrizione sopra i campi
        description1_text = "Data acquisition."
        description1_label = QtWidgets.QLabel(description1_text)
        description1_label.setWordWrap(True)
        description1_label.setFont(QtGui.QFont("Arial", 16))
        description1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 20px 20px 10px 20px;")
        description1_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.data_acquisition_layout.addWidget(description1_label)
        
        # Layout per il tempo
        time_layout = QtWidgets.QHBoxLayout()

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
        time_layout.addLayout(duration_layout)
        time_layout.addStretch(1)  # Sposta verso sinistra

        self.data_acquisition_layout.addLayout(time_layout)

        # Spaziatore per mantenere il contenuto centrale
        self.data_acquisition_layout.addStretch(5)
        
        # Aggiungi il panel al layout del contenuto principale
        self.main_window.add_content_widget(self.data_acquisition_panel)
        
    def _set_buttons_layout(self):
        # Bottone per tornare indietro
        back_button = CustomButton("Back", 140, 40)
        back_button.clicked.connect(self._show_previous_screen)
        
        # Bottone per iniziare la misurazione
        start_measurement_button = CustomButton("Start Measurement", 280, 40)
        start_measurement_button.clicked.connect(self._start_measurement)
        
        # Bottone per procedere
        next_button = CustomButton("Next", 140, 40)
        next_button.clicked.connect(self._show_next_screen)
        
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(start_measurement_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(next_button)
        
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
        """ self.main_window.add_button(back_button)
        self.main_window.add_button(next_button) """    

    def _show_previous_screen(self):
        from data_entry_screen import DataEntryScreen
        
        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        self.data_entry_screen.set_data_entry_screen()

    def _show_next_screen(self):
        """ from data_acquisition_screen import DataAcquisitionScreen
        
        self.main_window.clear_buttons_layout()
        
        self.data_acquisition_screen = DataAcquisitionScreen(self.main_window)
        
        self.data_acquisition_screen.set_data_acquisition_screen()
        
        self.main_window.show_content_widget("Next") """
        
        self._check_entry_fields()

    def _start_measurement(self):
        # Aggiungi il percorso della directory 'API' al PYTHONPATH
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
        from exe_manager import ExeManager
        
        self.path_csv = self.user_data.create_path_csv()

        # Aggiorna lo stato e crea il pulsante di stop
        DataAcquisitionScreen.measurement_started = True
        self._create_stop_button()

    def _create_stop_button(self):
        self.stop_measurement_button = CustomButton("Stop Measurement", 280, 40)
        self.stop_measurement_button.clicked.connect(self._stop_measurement)

        self.main_window.clear_buttons_layout()  # Rimuove i pulsanti attuali
        self.main_window.add_button(self.stop_measurement_button)  # Aggiunge il pulsante di stop

    def _stop_measurement(self):
        # Aggiungi il percorso della directory 'API' al PYTHONPATH
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
        from exe_manager import ExeManager

        if DataAcquisitionScreen.measurement_started:
            # Logica per fermare la misurazione, ad esempio fermare il processo del script
            self.script = ExeManager().close_script()
            DataAcquisitionScreen.measurement_started = False

            # Rimuove il pulsante di stop
            self.main_window.clear_buttons_layout() 
            
            # Aggiungi i pulsanti "Close" e "New Measurement"
            self._create_post_measurement_buttons()     

    def _create_post_measurement_buttons(self):
        close_button = CustomButton("Close", 140, 40)
        close_button.clicked.connect(self._close_application)
        
        new_measurement_button = CustomButton("New Measurement", 280, 40)
        new_measurement_button.clicked.connect(self._start_new_measurement)
        
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(close_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(new_measurement_button)
        buttons_layout.addStretch()
        
        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
    def _close_application(self):
        QtCore.QCoreApplication.quit()
        
    def _start_new_measurement(self):
        from data_entry_screen import DataEntryScreen
        
        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        self.data_entry_screen.set_data_entry_screen()

    def _save_duration_field(self):
        self.field_error = ""
        
        try:
            duration = self.duration_entry.text()  # Ottieni la durata inserita dall'utente
        except AttributeError as e:
            duration = ""
            
        if duration == "":
            duration = "-1"
            
        try:
            self.duration_time.set_time_min(int(duration))
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
