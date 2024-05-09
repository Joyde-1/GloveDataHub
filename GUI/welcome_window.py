import tkinter as tk
from PIL import Image, ImageTk
from window_manager import WindowManager

class WelcomeWindow:
    def create_welcome_window():
        # Crea la finestra principale
        window_manager = WindowManager()

        window_params = {
            'title': "GloveDataHub", 
            'width': 800, 
            'height': 600, 
            'background': '#E9E6DB'
        }

        welcome_window = window_manager.create_window(**window_params)

        window_header_params = {
            'window': welcome_window,
            'title': "GloveDataHub",
            'font': ("Arial", 24), 
            'background': '#E9E6DB', 
            'frontground': 'black'
        }

        welcome_window = window_manager.set_window_header(**window_header_params)

        # Paragrafo di descrizione
        description = ("Welcome to GloveDataHub, your interface for managing and "
                    "visualizing data from your sensor-equipped gloves. This tool "
                    "allows you to access and analyze the data in real-time.")
        description_label = tk.Label(welcome_window, text=description, wraplength=500, font=("Arial", 16), justify="center", bg='#E9E6DB', fg='black')
        description_label.pack(pady=(50, 40))

        # Crea un widget Frame per contenere il contenuto principale
        main_frame = tk.Frame(welcome_window, bg='#E9E6DB')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Area di testo nella parte superiore
        #text_area = tk.Text(main_frame, height=15, width=75, bg='white', fg='black', font=("Arial", 12))
        #text_area.pack(padx=20, pady=(0, 20))

        # Bottone per procedere
        next_button = tk.Button(main_frame, text="Next", command=lambda: print("Next was clicked"), font=("Arial", 18), bg='#E9E6DB', fg='black', padx=40, pady=20, highlightbackground='#E9E6DB')
        next_button.pack(side=tk.BOTTOM, anchor='e', padx=(0, 20), pady=(0, 20))

        # Avvia il main loop della finestra
        welcome_window.mainloop()
