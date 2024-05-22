from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
import sys
from window_manager import WindowManager
from welcome_screen import WelcomeScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    main_window_params = {
        'ghd_logo_path': "GUI/images/logo_GloveDataHub.png",
        'kore_logo_path': "GUI/images/kore_Logo.png",
        'window_title': "GloveDataHub", 
        'window_width': 1025, 
        'window_height': 600, 
        'background': '#E9E6DB',
        'frontground': '#000000',
        'header_title': "GloveDataHub",
        'header_font': QFont("Arial", 24, QFont.Weight.Bold)
    }
    
    # Crea la finestra principale
    main_window = WindowManager(**main_window_params)
    
    # Avvia il main loop della finestra
    main_window.show()

    welcome_screen = WelcomeScreen(main_window)
    
    welcome_screen.set_welcome_screen()
    
    sys.exit(app.exec())