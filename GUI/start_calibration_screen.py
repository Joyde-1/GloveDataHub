import tkinter as tk
from window_manager import WindowManager

class StartCalibrationScreen:
    def __init__(self, window):
        self.main_window = window
        self._create_start_calibration_screen()
    
    def _create_start_calibration_screen(self):    
        # Crea un pannello per contenere tutti i widget
        welcome_panel = tk.PanedWindow(self.main_window, orient=tk.VERTICAL, bg='#E9E6DB')
        welcome_panel.pack(fill=tk.BOTH, expand=True)

        # Paragrafo di descrizione
        description = ("")
        description_label = tk.Label(welcome_panel, text=description, wraplength=600, font=("Arial", 16), justify="left", bg='#E9E6DB', fg='black')
        description_label.pack(pady=(50, 40))

        # Crea un widget Frame per contenere il contenuto principale
        main_frame = tk.Frame(welcome_panel, bg='#E9E6DB')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Area di testo nella parte superiore
        #text_area = tk.Text(main_frame, height=15, width=75, bg='white', fg='black', font=("Arial", 12))
        #text_area.pack(padx=20, pady=(0, 20))

        # Bottone per procedere
        next_button = tk.Button(main_frame, text="Next", command=lambda: print("Pompami"), font=("Arial", 18), bg='#E9E6DB', fg='black', padx=40, pady=20, highlightbackground='#E9E6DB')
        next_button.pack(side=tk.BOTTOM, anchor='e', padx=(0, 20), pady=(0, 20))