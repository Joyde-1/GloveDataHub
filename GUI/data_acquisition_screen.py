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

        # Descrizione sopra il campo
        description1_text = (
            "Enter the measurement duration in the \n"
            "corresponding field. \n\n"
            "If you prefer the data acquisition to have \n"
            "an unlimited duration, leave the duration \n"
            "field empty."
        )
        description1_label = QtWidgets.QLabel(description1_text)
        description1_label.setWordWrap(True)
        description1_label.setFont(QtGui.QFont("Arial", 16))
        description1_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 20px 10px;")
        
        self.data_acquisition_layout.addWidget(description1_label)

        # Widget per la durata
        duration_label = QtWidgets.QLabel("Duration (in minutes):")
        duration_label.setFont(QtGui.QFont("Arial", 16))
        duration_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 20px 10px 10px 10px;")
        
        DataAcquisitionScreen.duration_entry = QtWidgets.QLineEdit()
        DataAcquisitionScreen.duration_entry.setFont(QtGui.QFont("Arial", 14))
        DataAcquisitionScreen.duration_entry.setStyleSheet("color: black;")
        DataAcquisitionScreen.duration_entry.setFixedWidth(90)
        DataAcquisitionScreen.duration_entry.setContentsMargins(15, 5, 10, 5)
        
        duration_layout = QtWidgets.QVBoxLayout()
        
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(DataAcquisitionScreen.duration_entry)
        
        #duration_layout.addStretch()

        self.data_acquisition_layout.addLayout(duration_layout)
        
        time_label = QtWidgets.QLabel("Time:")
        time_label.setFont(QtGui.QFont("Arial", 16))
        time_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 10px 10px 10px")
        
        self.time_display = QtWidgets.QLabel("00:00:00")
        self.time_display.setFont(QtGui.QFont("Arial", 16))
        self.time_display.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 10px 5px;")
        
        self.time_to_reach_label = QtWidgets.QLabel("/  -")
        self.time_to_reach_label.setFont(QtGui.QFont("Arial", 16))
        self.time_to_reach_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 10px 0px;")
        
        # Display del cronometro
        time_layout = QtWidgets.QHBoxLayout()
        
        time_layout.addWidget(time_label)
        time_layout.addWidget(self.time_display)
        time_layout.addWidget(self.time_to_reach_label)
        
        time_layout.addStretch()
        
        self.data_acquisition_layout.addLayout(time_layout)
        
        # Descrizione sotto il campo
        description2_text = (
            "Press the 'Start Measurement' button to \n"
            "start capturing data from your haptic gloves."
        )
        description2_label = QtWidgets.QLabel(description2_text)
        description2_label.setWordWrap(True)
        description2_label.setFont(QtGui.QFont("Arial", 16))
        description2_label.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 20px 10px;")
        
        self.data_acquisition_layout.addWidget(description2_label)
        
        # Aggiungi il panel al layout del contenuto principale
        self.main_window.add_content_widget(self.data_acquisition_panel)
        
    def _start_timer(self):        
        self.time_display.setText("00:00:00")  # Resetta il display del tempo
        
        # Inizializza il timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._update_timer)
        
        # Tempo trascorso in secondi
        self.elapsed_time = 0
        
        # Inizia il timer con un intervallo di 1 secondo (1000 millisecondi)
        self.timer.start(1000)
        
    def _update_timer(self):
        self.elapsed_time += 1
        hours, remainder = divmod(self.elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.time_display.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        #if self.elapsed_time >= self.target_time:
        if self.duration_time.is_time_over(self.elapsed_time):
            self._stop_measurement()
            
    def _conclude_data_acquisition(self):
        self.timer.stop()
        self._show_success_message()
        self.elapsed_time = 0  # Resetta il tempo trascorso
        
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
            
            self._start_timer()
            
            self.back_button.hide()
            self.measurement_button.setText("Stop")
            self.measurement_button.clicked.disconnect(self._start_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)
        else:
            self._show_error_message()
        
    def _stop_measurement(self):
        if self.exe_manager.is_script_running() and not self.duration_time.is_time_over(self.elapsed_time):
            
            self.exe_manager.close_script()
            
        self._conclude_data_acquisition()
            
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
            
            self._start_timer()
            
            self.measurement_button.setText("Stop")
            self.measurement_button.clicked.disconnect(self._restart_measurement)
            self.measurement_button.clicked.connect(self._stop_measurement)
            self.next_button.hide()
            self.buttons_layout.setAlignment(self.measurement_button, QtCore.Qt.AlignmentFlag.AlignCenter)

    def _save_duration_field(self):
        self.field_error = ""
        
        duration = DataAcquisitionScreen.duration_entry.text()  # Ottieni la durata inserita dall'utente
            
        if duration == "":
            self.duration_time.set_time_min()
            self.time_to_reach_label.setText("/  ∞")
        else:
            try:
                duration = int(duration)
                self.duration_time.set_time_min(duration)
                
                hours, minutes = divmod(duration, 60)
                self.time_to_reach_label.setText(f"/  {hours:02d}:{minutes:02d}:00")
            except ValueError as e:
                self.field_error += "• " + str(e)
    
    def _is_error_message(self):
        if self.field_error != "":
            self.field_error = "Please fix the following errors:\n" + self.field_error
            return True
        else:
            return False

    def _show_error_message(self):
        error_msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, "Error", self.field_error.strip())
        self._set_output_dialog_style(error_msg_box)
        error_msg_box.exec()
        
    def _show_success_message(self):
        timer_msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, "Success", ("I dati dei guanti aptici sono stati \n"
                                                                                                  "acquisiti con successo!"))
        self._set_output_dialog_style(timer_msg_box)
        timer_msg_box.exec() 

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
