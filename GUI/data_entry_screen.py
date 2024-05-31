"""
Authors
-------
Giovanni Fanara
Alfredo Gioacchino MariaPio Vecchio

Date
----
2024-05-30
"""



from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox,QFileDialog,QLineEdit
from PyQt6.QtGui import QFont
from pathlib import Path
import os
import sys

# Add the main directory path to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from API.user_data import UserData
from custom_button import CustomButton
from window_manager import WindowManager


class DataEntryScreen:
    """
    Represents the data entry screen of the application.

    Attributes
    ----------
    is_first_time : bool (class attribute)
        Indicates if it's the first time the screen is being displayed.
    first_name_entry : QLineEdit (class attribute)
        Entry field for the first name.
    last_name_entry : QLineEdit (class attribute)
        Entry field for the last name.
    code_entry : QLineEdit (class attribute)
        Entry field for the 4-digit code.
    path_directory_entry : QLineEdit (class attribute)
        Entry field for the path directory.
    user_data : UserData (istance attribute)
        Instance of UserData for managing user data.
    data_entry_panel : QWidget (istance attribute) 
        Panel used to contain the all widget.
    data_entry_layout :  QVBoxLayout (istance attribute)
        Layout used for the widgets.  
    first_name_entry : QLineEdit (istance attribute)
        Field used to insert the first name.
    last_name_entry : QLineEdit (istance attribute)
        Field used to insert the last name.
    code_entry : QLineEdit (istance attribute)
        Field used to insert the code.
    path_directory_entry : QLineEdit (istance attribute)
        Field used to set the directoty path.
    fields_errors : str (istance attribute)
        Fields used for the errors.
    info_message : str (istance attribute)
       Contains the message that is shown to the user.
    calibration_screen : CalibrationScreen (istance attribute)
        Instance used to create the CalibrationScreen.
    data_acquisition_screen : DataAcqusitionScreen (istance attribute)
         Instance used to create the DataAcqusitionScreen.
    """

    is_first_time = True
    
    first_name_entry = None
    last_name_entry = None
    code_entry = None
    path_directory_entry = None
    
    def __init__(self, main_window: WindowManager):
        """
        Initializes the Data Entry Screen.

        Parameters
        ----------
        main_window : WindowManager
            The main window manager instance.
        """

        self.main_window = main_window
        self.user_data = UserData()

    def set_data_entry_screen(self):
        """
        Sets up the data entry screen.
        """

        # Check if is the first time the data entry screen is being set
        if DataEntryScreen.is_first_time:
            self._create_data_entry_widget()
            DataEntryScreen.is_first_time = not DataEntryScreen.is_first_time
        
        # Set the buttons layout     
        self._set_buttons_layout()
        
        
    def _create_data_entry_widget(self):
        """
        Creates the widget for data entry.
        """

        # Create a panel to contain all the widgets
        self.data_entry_panel = QWidget()
        self.data_entry_panel.setStyleSheet("background-color: #FFFCF0; border-radius: 15px; padding: 10px")
        self.data_entry_layout = QVBoxLayout(self.data_entry_panel)
        
        # Title of the data entry section
        data_entry_title = QLabel("2 • Entering User Data")
        data_entry_title.setWordWrap(True)
        data_entry_title.setFont(QFont("Montserrat", 16, QFont.Weight.Bold))
        data_entry_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        data_entry_title.setStyleSheet("color: #023E58; background-color: #D9E7EC; border-radius: 15px; margin: 10px 10px 10px 10px;")
        
        self.data_entry_layout.addWidget(data_entry_title)
        
        # Description above the fields
        description_text = (
            "You do not have to fill all fields. If all are left <br>"
            "blank, the system will generate a random <br>"
            "4-digit code."
        )
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setFont(QFont("Source Sans Pro", 14))
        description_label.setStyleSheet("color: #031729; background-color: #FFFCF0; padding: 0px 10px 0px 10px;")
        
        self.data_entry_layout.addWidget(description_label)
        
        # Layout for first and last name
        name_layout = QHBoxLayout()

        # Widget for the name
        first_name_label = QLabel("<b>First Name</b>:")
        first_name_label.setFont(QFont("Source Sans Pro", 16))
        first_name_label.setStyleSheet("color: #025885; background-color: #FFFCF0; margin: 0px 10px 0px 0px; padding: 0px 0px 5px 0px;")
        first_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # Name field
        DataEntryScreen.first_name_entry = QLineEdit()
        DataEntryScreen.first_name_entry.setFont(QFont("Georgia", 14))
        DataEntryScreen.first_name_entry.setFixedSize(195, 35)
        DataEntryScreen.first_name_entry.setStyleSheet("color: #031729; background-color: #F5FBFF; border-radius: 8px; border: 2px solid #CCE4F6; margin: 0px 10px 0px 0px; padding: 5px 5px 5px 5px;")  

        # First Name layout
        first_name_layout = QVBoxLayout() 
        
        first_name_layout.addWidget(first_name_label)
        first_name_layout.addWidget(DataEntryScreen.first_name_entry)
        first_name_layout.addStretch(3)
        
        first_name_widget = QWidget()
        first_name_widget.setLayout(first_name_layout)
        first_name_widget.setContentsMargins(0, 0, 0, 0)
        first_name_widget.setStyleSheet("margin: 0px; padding: 5px 10px 5px 0px;")
        
        name_layout.addWidget(first_name_widget)
        name_layout.addStretch()

        # Widget for the surname
        last_name_label = QLabel("<b>Last Name</b>:")
        last_name_label.setFont(QFont("Source Sans Pro", 16))
        last_name_label.setStyleSheet("color: #025885; background-color: #FFFCF0; margin: 0px 0px 0px 0px; padding: 0px 0px 5px 0px;")
        
        # Last name field
        DataEntryScreen.last_name_entry = QLineEdit()
        DataEntryScreen.last_name_entry.setFont(QFont("Georgia", 14))
        DataEntryScreen.last_name_entry.setFixedSize(195, 35)
        DataEntryScreen.last_name_entry.setStyleSheet("color: #031729; background-color: #F5FBFF; border-radius: 8px; border: 2px solid #CCE4F6; margin: 0px 10px 0px 0px; padding: 5px 5px 5px 5px;")
        
        # Last name layout
        last_name_layout = QVBoxLayout()
        
        last_name_layout.addWidget(last_name_label)
        last_name_layout.addWidget(DataEntryScreen.last_name_entry)
        last_name_layout.addStretch(3)
        
        last_name_widget = QWidget()
        last_name_widget.setLayout(last_name_layout)
        last_name_widget.setContentsMargins(0, 0, 0, 0)
        last_name_widget.setStyleSheet("margin: 0px; padding: 5px 0px 5px 0px;")
           
        name_layout.addWidget(last_name_widget)
        name_layout.addStretch()
        
        name_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.data_entry_layout.addLayout(name_layout)
        
        # Widget for the optional code
        code_label = QLabel("<b>4-digit Code</b>:")
        code_label.setFont(QFont("Source Sans Pro", 16))
        code_label.setStyleSheet("color: #025885; background-color: #FFFCF0; margin: 0px 10px 0px 0px; padding: 0px 0px 5px 0px;")
        
        # Code field
        DataEntryScreen.code_entry = QLineEdit()
        DataEntryScreen.code_entry.setFont(QFont("Georgia", 14))
        DataEntryScreen.code_entry.setStyleSheet("color: #031729; background-color: #F5FBFF; border-radius: 8px; border: 2px solid #CCE4F6; margin: 0px 10px 0px 0px; padding: 5px 5px 5px 5px;")
        DataEntryScreen.code_entry.setFixedSize(90, 35)
        
        # Code layout
        code_layout = QVBoxLayout()
        
        code_layout.addWidget(code_label)
        code_layout.addWidget(DataEntryScreen.code_entry)
        code_layout.addStretch(3)

        code_widget = QWidget()
        code_widget.setLayout(code_layout)
        code_widget.setContentsMargins(0, 0, 0, 0)
        code_widget.setStyleSheet("margin: 0px; padding: 5px 0px 5px 0px;")
        
        self.data_entry_layout.addWidget(code_widget)

        # Widget for the path
        path_directory_label = QLabel("<b>Path</b> (is required):")
        path_directory_label.setFont(QFont("Source Sans Pro", 16))
        path_directory_label.setStyleSheet("color: #025885; background-color: #FFFCF0; margin: 0px 10px 0px 0px; padding: 0px 0px 5px 0px;")

        # Path field
        DataEntryScreen.path_directory_entry = QLineEdit()
        DataEntryScreen.path_directory_entry.setText(str(Path.home() / "Documents"))
        DataEntryScreen.path_directory_entry.setFont(QFont("Georgia", 12))
        DataEntryScreen.path_directory_entry.setStyleSheet("color: #031729; background-color: #F5FBFF; border-radius: 8px; border: 2px solid #CCE4F6; margin: 0px 10px 0px 0px; padding: 2px 2px 2px 2px;")
        DataEntryScreen.path_directory_entry.setFixedSize(260, 30)
        
        # browse button to set a specific path
        browse_button = CustomButton("Browse", 1, 120, 30, 14)
        browse_button.clicked.connect(self._browse_path)

        # Path Layout
        # Use QVBoxLayout for label and QHBoxLayout for entry and button
        path_directory_layout = QVBoxLayout()
        
        path_directory_entry_layout = QHBoxLayout()
        path_directory_entry_layout.addWidget(DataEntryScreen.path_directory_entry)
        path_directory_entry_layout.addStretch()
        path_directory_entry_layout.addWidget(browse_button)

        path_directory_layout.addWidget(path_directory_label)
        path_directory_layout.addLayout(path_directory_entry_layout)
        
        path_directory_widget = QWidget()
        path_directory_widget.setLayout(path_directory_layout)
        path_directory_widget.setContentsMargins(0, 0, 0, 0)
        path_directory_widget.setStyleSheet("margin: 0px; padding: 5px 0px 5px 0px;")
        
        self.data_entry_layout.addWidget(path_directory_widget)

        # Add the panel to the main content layout
        self.main_window.add_content_widget(self.data_entry_panel)
        
    def _set_buttons_layout(self):
        """
        Sets up the layout for buttons.
        """
        
        # Button to go back
        back_button = CustomButton("Back", 0, 120, 40, 16)
        back_button.clicked.connect(self._show_previous_screen)
        
        # Button to proceed
        next_button = CustomButton("Next", 0, 120, 40, 16)
        next_button.clicked.connect(self._show_next_screen)
        
        buttons_layout = QHBoxLayout()
        
        buttons_layout.addWidget(back_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(next_button)
        
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        
        button_widget = QWidget()
        button_widget.setLayout(buttons_layout)
        
        self.main_window.add_button(button_widget)
        
    def _browse_path(self):
        """
        Opens a file dialog to browse for a directory path.
        """
        
        # Get the path of the Documents folder
        documents_path = str(Path.home() / "Documents")
        
        # Open the QFileDialog starting from the Documents folder
        path_directory = QFileDialog.getExistingDirectory(self.main_window, 'Select the destination folder', documents_path)

        if path_directory:
            DataEntryScreen.path_directory_entry.setText(path_directory)

    def _show_previous_screen(self):
        """
        Shows the previous screen.
        """
        
        from calibration_screen import CalibrationScreen

        # Show the next screen
        self.main_window.show_content_widget("Back")
        
        # Remove all the buttons from main window buttons layout
        self.main_window.clear_buttons_layout()
        
        self.calibration_screen = CalibrationScreen(self.main_window)
        
        # Set the calibration screen
        self.calibration_screen.set_calibration_screen()

    def _show_next_screen(self):
        """
        Shows the next screen.
        """
        
        from data_acquisition_screen import DataAcquisitionScreen
        
        self._save_fields_values()
        
        if not self._is_error_message():
            # If the code was generated randomically, show an info message
            if self.info_message != "":
                self._show_information_message()
            
            # Remove all the buttons from main window buttons layout
            self.main_window.clear_buttons_layout()
            
            self.data_acquisition_screen = DataAcquisitionScreen(self.main_window, self.user_data)
            
            # Set the data acquisition screen
            self.data_acquisition_screen.set_data_acquisition_screen()
            
            # Show the next screen
            self.main_window.show_content_widget("Next")
        else:
            # Show error message
            self._show_error_message()

    def _save_fields_values(self):
        """
        Saves the values of the fields.
        """
        
        self.fields_errors = ""
        self.info_message = ""

        # Get the first name entered by the user
        first_name = DataEntryScreen.first_name_entry.text().strip()
        
        # Get the last name entered by the user
        last_name = DataEntryScreen.last_name_entry.text().strip()
        
        # Get the code entered by the user
        code = DataEntryScreen.code_entry.text()
        
        # Get the path of the directory indicated by the user
        path_directory = DataEntryScreen.path_directory_entry.text()

        # Set user first name
        try:
            self.user_data.set_first_name(first_name)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
        
        # Set user last name
        try:
            self.user_data.set_last_name(last_name)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
        
        # If all the fields are empty, the system generates a random 4-digit code
        if first_name == "" and last_name == "" and code == "" and self.fields_errors == "":
            code = self.user_data.generate_random_code()
            DataEntryScreen.code_entry.setText(code)
            self.info_message = (
                'The <b><span style="color: #025885;">code</span></b> has been generated automatically \n'
                'because the <b><span style="color: #025885;">first</span></b> and <b><span style="color: #025885;">last name</span></b> are missing.'
            )

        try:
            self.user_data.set_code(code)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
        
        # Set directory to save .CSV file
        try:
            self.user_data.set_path_directory(path_directory)
        except ValueError as e:
            self.fields_errors += "• " + str(e)
        
    def _is_error_message(self):
        """
        Checks if there is an error message.
        """
        
        if self.fields_errors != "":
            self.fields_errors = "Please fix the following errors:<br>" + self.fields_errors
            return True
        else:
            return False  

    def _show_error_message(self):
        """
        Shows an error message.
        """
        
        error_msg_box = QMessageBox(QMessageBox.Icon.Critical, "Error", self.fields_errors.strip())
        
        # Set the msg box style
        self._set_output_dialog_style(error_msg_box)
        error_msg_box.exec()

    def _show_information_message(self):
        """
        Shows an information message.
        """
        
        info_msg_box = QMessageBox(QMessageBox.Icon.Information, "Information", self.info_message)
        
        # Set the msg box style
        self._set_output_dialog_style(info_msg_box)
        info_msg_box.exec()      

    def _set_output_dialog_style(self, dialog):
        """
        Sets the style of the output dialog.
        """
        
        if dialog:
            dialog.setStyleSheet("""
                QMessageBox {
                    color: #023E58;
                    background-color: #E9E6DB;
                }
                QLabel {
                    color: #023E58;
                    font: ("Merriweather", 14);
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