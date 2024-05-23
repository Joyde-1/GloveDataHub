from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout
from custom_button import CustomButton

class FinalScreen:
    is_first_time = True

    def set_final_screen(self):
        if FinalScreen.is_first_time:
            self._create_final_screen_widget()
            FinalScreen.is_first_time = not FinalScreen.is_first_time
            
        self._set_buttons_layout()
        
    def _create_post_measurement_buttons(self):
        close_button = CustomButton("Close", 140, 40, 14)
        close_button.clicked.connect(self._close_application)
        
        new_measurement_button = CustomButton("New Measurement", 280, 40, 14)
        new_measurement_button.clicked.connect(self._start_new_measurement)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(close_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(new_measurement_button)
        buttons_layout.addStretch()
        
        button_widget = QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
    def _start_new_measurement(self):
        from data_entry_screen import DataEntryScreen
        
        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        self.data_entry_screen.set_data_entry_screen()
        
    def _close_application(self):
        QtCore.QCoreApplication.quit()