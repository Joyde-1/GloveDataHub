from window_manager import WindowManager
from welcome_screen import WelcomeScreen

if __name__ == "__main__":
    # Crea la finestra principale
    window_manager = WindowManager()

    """ main_window_params = {
        'title': "GloveDataHub", 
        'width': 800, 
        'height': 600, 
        'background': '#E9E6DB'
    } """

    main_window_params = {
        'title': "GloveDataHub", 
        'width': 1100, 
        'height': 800, 
        'background': '#E9E6DB'
    }

    window_manager.create_window(**main_window_params)

    main_window_header_params = {
        'title': "GloveDataHub",
        'font': ("Arial", 30, "bold"), 
        'background': '#E9E6DB', 
        'frontground': 'black'
    }

    window_manager.set_window_header(**main_window_header_params)

    main_window = window_manager.get_window()

    welcome_screen = WelcomeScreen(main_window, window_manager)

    # Avvia il main loop della finestra
    main_window.mainloop()