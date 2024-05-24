from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout
from custom_button import CustomButton

class FinalScreen:
    """
    Represents the final screen of the application, displayed after the measurement process.

    Attributes
    ----------
    is_first_time : bool 
        A flag to indicate if it's the first time setting up the final screen.
    """
    is_first_time = True

    def set_final_screen(self):
        """
        Sets up the final screen of the application.
        """
        if FinalScreen.is_first_time:
            self._create_final_screen_widget() # Create the widget for the final screen
            FinalScreen.is_first_time = not FinalScreen.is_first_time
            
        self._set_buttons_layout() # Create the layout button for the final screen
        
    def _create_post_measurement_buttons(self):
        """
        Creates buttons for post-measurement actions.
        """
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
        """
        Starts a new measurement by navigating back to the data entry screen.
        """
        from data_entry_screen import DataEntryScreen
        
        self.main_window.show_content_widget("Back")
        
        self.main_window.clear_buttons_layout()
        
        self.data_entry_screen = DataEntryScreen(self.main_window)
        
        self.data_entry_screen.set_data_entry_screen()
        
    def _close_application(self):
        """
        Closes the application.
        """
        QtCore.QCoreApplication.quit()