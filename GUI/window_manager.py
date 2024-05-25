from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget, QMessageBox
from PyQt6.QtGui import QFont
import sys
import os
import ctypes
from ctypes import wintypes
import psutil
import pygetwindow as gw
import time
from custom_button import CustomButton

# Add the directory 'API' path to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))

from exe_manager import ExeManager

# Constants for Windows messages
WM_SYSCOMMAND = 0x0112
WM_NCLBUTTONDOWN = 0x00A1
SC_MOVE = 0xF010

# Define the message filter callback function
def window_proc(hwnd, msg, wparam, lparam):
    """
    Callback function to handle window messages.

    Parameters
    ----------
    hwnd : int
        The handle to the window.
    msg : int
        The message identifier.
    wparam : int
        Additional message information.
    lparam : int
        Additional message information.

    Returns
    -------
    int
        The result of the message processing and the action taken.
    """
    if msg == WM_SYSCOMMAND and (wparam == SC_MOVE or wparam == SC_MOVE + 1):
        return 0  # Ignore the move command
    if msg == WM_NCLBUTTONDOWN:
        return 0  # Ignore the non-client click (movement)
    return ctypes.windll.user32.DefWindowProcW(hwnd, msg, wparam, lparam)

# Convert the callback function to a function pointer
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int)
window_proc_pointer = WNDPROC(window_proc)

class WindowManager(QWidget):
    """
    Class to manage the main window of the application.

    Attributes
    ----------
    is_sensecom_layout : bool 
        Flag to indicate whether the SenseCom layout is currently displayed.
    ghd_logo_path : str
        The path to the GHD logo image.
    kore_logo_path : str 
        The path to the Kore logo image.
    window_title : str 
        The title of the window.
    window_width : int
        The width of the window.
    window_height : int    
        The height of the window.
    background : str
        The background color of the window.
    frontground : str 
        The frontground color of the window.
    header_title : str 
        The title displayed in the window header.
    header_font : QtGui.QFont 
        The font used for the header title.
    exe_manager : ExeManager 
        An instance of the ExeManager class.
    """
    
    is_sensecom_layout = False

    def __init__(self, ghd_logo_path, kore_logo_path, window_title, window_width, window_height, background, frontground, header_title, header_font):
        """
        Constructor, initialize the WindowManager.

        Parameters
        ----------
        ghd_logo_path : str 
            The path to the GHD logo image.
        kore_logo_path : str  
            The path to the Kore logo image.
        window_title : str 
            The title of the window.
        window_width : int 
            The width of the window.
        window_height : int 
            The height of the window.
        background : str 
            The background color of the window.
        frontground : str 
            The frontground color of the window.
        header_title : str 
            The title displayed in the window header.
        header_font : QtGui.QFont 
            The font used for the header title.
        """
        super().__init__()
        
        self.ghd_logo_path = ghd_logo_path
        self.kore_logo_path = kore_logo_path
        self.window_title = window_title
        self.window_width = window_width
        self.window_height = window_height
        self.background = background
        self.frontground = frontground
        self.header_title = header_title
        self.header_font = header_font

        self.exe_manager = ExeManager()
        
        self._init_window()
    
    def _init_window(self):
        """
        Initialize the main window.
        """
        self._create_window()
        self._set_window_header()
        self._center_window()  # Center the window on the screen
        
        self.setLayout(self.main_layout)

    def _create_window(self):
        """
        Create the main window.
        """
        self.setWindowTitle(self.window_title)
        self.setFixedSize(self.window_width, self.window_height)
        self.setStyleSheet(f"background-color: {self.background};")

        self.main_layout = QVBoxLayout()

    def _set_window_header(self):
        """
        Set up the window header.
        """
        header_layout = QHBoxLayout()

        # Load logo images
        gdh_image = QtGui.QPixmap(self.ghd_logo_path)
        kore_image = QtGui.QPixmap(self.kore_logo_path)
        
        # Resize images to 100x100 pixel
        gdh_image = gdh_image.scaled(100, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        kore_image = kore_image.scaled(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)

        # Create labels for the images
        self.gdh_logo = QLabel()
        self.gdh_logo.setPixmap(gdh_image)

        self.kore_logo = QLabel()
        self.kore_logo.setPixmap(kore_image)

        # Create the application title
        self.title_label = QLabel(self.header_title)
        self.title_label.setFont(self.header_font)
        self.title_label.setStyleSheet(f"color: {self.frontground};")

        # Add logos and title to the header layout
        header_layout.addWidget(self.gdh_logo)
        header_layout.addStretch()
        header_layout.addWidget(self.title_label)        
        header_layout.addStretch()
        header_layout.addWidget(self.kore_logo)
        
        header_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Set margin and padding to position the elements correctly
        header_layout.setContentsMargins(5, 5, 5, 5)
        
        # header_widget.setLayout(header_layout)
        #header_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) #  | QtCore.Qt.AlignmentFlag.AlignTop

        # Imposta il margine e padding per posizionare correttamente gli elementi
        # header_layout.setContentsMargins(5, 5, 5, 5)
        
        # Aggiungi l'header layout alla parte superiore del layout principale
        self.main_layout.addLayout(header_layout)

        # Aggiungi un layout per il contenuto dinamico
        # self.content_layout = QVBoxLayout()
        # self.main_layout.addLayout(self.content_layout)
        
        self._create_content_layout()
        
        self._create_buttons_layout()
    
    def _center_window(self):
        """
        Center the window on the screen.
        """
        # Get screen dimensions
        screen_geometry = QtGui.QGuiApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calculate window width and height
        window_width = self.width()
        window_height = self.height()

        # Define desired distance from edges
        margin_horizontal = 50  # Modifica questa variabile per regolare la distanza dai bordi
        margin_vertical = 50  # Modifica questa variabile per regolare la distanza dai bordi

        # Calculate x and y positions to center the window horizontally and vertically
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Calculate vertical distance from edges
        distance_top = y
        distance_bottom = screen_height - y - window_height

        # Calculate additional vertical offset to compensate for the difference between top and bottom distance
        additional_offset = (distance_bottom - distance_top) // 2  # Aumenta il divisore per sollevare ulteriormente la finestra

        # Adjust vertical offset
        y -= additional_offset + 50  # Modifica il valore di 50 per regolare ulteriormente il sollevamento

        # Ensure window stays within the screen
        x = max(margin_horizontal, min(x, screen_width - window_width - margin_horizontal))
        y = max(margin_vertical, min(y, screen_height - window_height - margin_vertical))

        # Set window position
        self.move(x, y)
        
    def _create_content_layout(self):
        """
        Create the layout for dynamic content.
        """
        self.content_layout = QGridLayout()
        self.stacked_content = QStackedWidget()
        
        self.content_layout.addWidget(self.stacked_content)
        
        self.main_layout.addLayout(self.content_layout)
        
    def add_content_widget(self, widget):
        """
        Add a widget to the content layout.

        Parameters
        ----------
        widget 
            The widget to add.
        """     
        self.stacked_content.addWidget(widget)
        
    def show_content_widget(self, direction):
        """
        Show the next or previous content widget.

        Parameters
        ----------
        direction : str 
            The direction to navigate ('Next' or 'Back').
        """
        current_index = self.stacked_content.currentIndex()
        
        if direction == "Next":
            next_index = current_index + 1
        elif direction == "Back":
            next_index = current_index - 1
        elif direction == "New":
            next_index = current_index - 3
            
        if next_index == 0 or next_index == 1 or next_index == 4:
            self._modify_content_widget_position(next_index)
            
        self.stacked_content.setCurrentIndex(next_index)
        
    def _modify_content_widget_position(self, next_index):
        """
        Modify the position of the content widget.

        Parameters
        ----------
        next_index : int 
            The index of the next content widget.
        """
        # Rimuovi the widget from the current layout
        self.content_layout.removeWidget(self.stacked_content)

        if next_index == 0 or next_index == 4:
            self.content_layout.addWidget(self.stacked_content)
        else:
            self.content_layout.addWidget(self.stacked_content, 0, 0, 3, 2, QtCore.Qt.AlignmentFlag.AlignLeft)
        
    def _create_buttons_layout(self):
        """
        Create the layout for buttons.
        """
        #self.button_widget = QWidget()
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addStretch()
        self.buttons_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        #self.button_widget.setLayout(self.buttons_layout)
        #self.main_layout.addWidget(self.buttons_widget)
        self.main_layout.addLayout(self.buttons_layout)
        
        # WindowManager.is_buttons_layout = not WindowManager.is_buttons_layout
        
    def add_button(self, button):
        """
        Add a button to the button layout.

        Parameters
        ----------
        button 
            The button to add.
        """
        self.buttons_layout.addWidget(button)
        #self.buttons_layout.addStretch()
        
    def create_sensecom_widget(self):
        """
        Create the SenseCom widget.
        """
        self.sensecom_widget = QWidget()
        
        # Add a layout for sensecom
        self.sensecom_layout = QVBoxLayout()
        
        # Sensecom title
        self.sensecom_title = QLabel("SenseCom Application")
        self.sensecom_title.setWordWrap(True)
        self.sensecom_title.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Weight.Bold))
        self.sensecom_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sensecom_title.setStyleSheet("color: black; background-color: #E9E6DB; padding: 0px 0px 5px 0px;")
        
        # Container for SenseCom
        self.sensecom_container = QWidget()
        self.sensecom_container.setFixedSize(528, 289)
        
        # Button to start SenseCom
        self.sensecom_button = CustomButton("Start SenseCom", 200, 30, 14)
        self.sensecom_button.clicked.connect(self._embed_sensecom)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.sensecom_button)
        
        self.sensecom_layout.addWidget(self.sensecom_title)
        self.sensecom_layout.addWidget(self.sensecom_container)
        # self.sensecom_layout.addStretch()
        self.sensecom_layout.addLayout(button_layout)
        self.sensecom_layout.addStretch()
        self.sensecom_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        
        self.sensecom_widget.setLayout(self.sensecom_layout)
        
        # Initialize the timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._check_sensecom)
        self.timer.start(1000)

        # self.main_layout.addLayout(self.sensecom_layout)
        self.content_layout.addWidget(self.sensecom_widget, 0, 1, 3, 2, QtCore.Qt.AlignmentFlag.AlignRight)
        # Aggiungi un layout per il contenuto dinamico
        # self.content_panel = QtWidgets.QStackedWidget()
        # self.content_layout.addWidget(self.content_panel)
        
        WindowManager.is_sensecom_layout = not WindowManager.is_sensecom_layout

    def _check_sensecom(self):
        """
        Check if SenseCom is not running to show 'Start Sensecom' button
        """
        
        if not self.exe_manager.is_sensecom_running():
            try:
                self.sensecom_button.show()
            except:
                pass

    def _embed_sensecom(self):
        """
        Embed SenseCom into the GUI.
        """
        if self.exe_manager.is_sensecom_running():
            pass
        else:
            # Control if the proces SenseCom is running
            for process in psutil.process_iter():
                if process.name() == "SenseCom.exe":
                    process.terminate()
                    break
            
            time.sleep(1)

            self.exe_manager.start_sensecom()
            QtCore.QTimer.singleShot(2500, self._embed_sensecom_window)
            
            self.sensecom_button.hide()

    def _embed_sensecom_window(self):
        """
        Embed SenseCom window into the GUI.
        """
        try:
            sensecom_hwnd = gw.getWindowsWithTitle("SenseCom")[0]

            sensecom_hwnd.restore()  # Restore the window if it's minimized or maximized
            sensecom_hwnd.moveTo(0, 0)  # Move the window to a specific position
            #sensecom_hwnd.resize(300, 200)  # Resize the window to fit inside the GUI container

            container_hwnd = int(self.sensecom_container.winId())
            ctypes.windll.user32.SetParent(sensecom_hwnd._hWnd, container_hwnd)
            
            # Get the current style of the SenseCom window
            style = ctypes.windll.user32.GetWindowLongW(sensecom_hwnd._hWnd, -16)
            
            # Remove the system buttons from the window
            style &= ~0x00C00000  # Remove WS_CAPTION (title bar) and WS_BORDER (border)
            ctypes.windll.user32.SetWindowLongW(sensecom_hwnd._hWnd, -16, style)

            # Set the anchor to pin the SenseCom window to the main GUI window
            ex_style = ctypes.windll.user32.GetWindowLongW(sensecom_hwnd._hWnd, -20)
            ex_style |= 0x00000008  # Set WS_EX_CONTROLPARENT
            ctypes.windll.user32.SetWindowLongW(sensecom_hwnd._hWnd, -20, ex_style)

        except IndexError:
            #pass
            QMessageBox.critical(self, "Error", "SenseCom window not found.") 
        
    def close_sensecom_widget(self):
        """
        Close the SenseCom widget.
        """
        self.clear_sensecom_layout()
        # self.content_layout.removeWidget(self.sensecom_widget)
        WindowManager.is_sensecom_layout = not WindowManager.is_sensecom_layout

    def closeEvent(self, event):
        """
        Handle the close event of the window.
        """
        if self.exe_manager.is_sensecom_running():
            self.exe_manager.close_sensecom()
        event.accept()
        
    def clear_sensecom_layout(self):
        """
        Clear the SenseCom layout.
        """
        while self.sensecom_layout.count():
            item = self.sensecom_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.layout() is not None:
                # If the item is a layout, is cleaned recursively
                self._clear_layout(item.layout())
                
    def clear_buttons_layout(self):
        """
        Clear the buttons layout.
        """
        # It only cleans the button_layout
        while self.buttons_layout.count() > 0:
            item = self.buttons_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Remove and delete the widget
            elif item.layout() is not None:
                self._clear_layout(item.layout())  # Recursively cleans nested layouts

    def _clear_layout(self, layout):
        """
        Clear a layout recursively.

        Parameters
        ----------
        layout : QLayout 
            The layout to clear.
        """
        # Recursively cleans a generic layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.layout() is not None:
                self._clear_layout(item.layout())