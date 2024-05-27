from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
import sys
from window_manager import WindowManager
from welcome_screen import WelcomeScreen

if __name__ == "__main__":
    """
    Main script to initialize and run the application.
    """
    app = QtWidgets.QApplication(sys.argv)
    
    # Parameters for the main window
    main_window_params = {
        'ghd_logo_path': "GUI/images/logo_GloveDataHub.png",
        'kore_logo_path': "GUI/images/kore_Logo.png",
        'window_title': "GloveDataHub", 
        'window_width': 1040, 
        'window_height': 670, 
        'background': '#E9E6DB',
        'frontground': '#031725',
        'header_title': "GloveDataHub",
        'header_font': QFont("Montserrat", 24, QFont.Weight.Bold)
    }
    
    # Create the main window
    main_window = WindowManager(**main_window_params)
    
    # Start the main window's event loop
    main_window.show()

    # Create and set up the welcome screen
    welcome_screen = WelcomeScreen(main_window)
    
    welcome_screen.set_welcome_screen()
    
    sys.exit(app.exec())