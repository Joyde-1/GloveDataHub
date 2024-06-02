#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
import sys
import os

from window_manager import WindowManager
from welcome_screen import WelcomeScreen


def resource_path(relative_path):
    """
    Gets the absolute path of the resources, works for the executable and for the normal script.
    """
    
    try:
        # Path when it is in a PyInstaller executable
        base_path = sys._MEIPASS
    except Exception:
        # Path when in a normal Python script
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    """
    Main script to initialize and run the application.
    """
    
    app = QApplication(sys.argv)
    
    # Parameters for the main window
    main_window_params = {
        'ghd_logo_path': resource_path("GUI/images/GDH.png"),
        'kore_logo_path': resource_path("GUI/images/Kore.png"),
        'window_title': "GloveDataHub", 
        'window_width': 1040, 
        'window_height': 670,
        'background': '#617B89',
        'frontground': '#026192',
        'header_title': "GloveDataHub",
        'header_font': QFont("Raleway", 24, QFont.Weight.Bold)
    }
    
    # Create the main window
    main_window = WindowManager(**main_window_params)
    
    # Start the main window's event loop
    main_window.show()

    # Create and set up the welcome screen
    welcome_screen = WelcomeScreen(main_window)
    
    welcome_screen.set_welcome_screen()
    
    sys.exit(app.exec())