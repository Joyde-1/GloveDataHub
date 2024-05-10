import tkinter as tk
from window_manager import WindowManager
from start_calibration_screen import StartCalibrationScreen

class WelcomeScreen:
    def __init__(self, window):
        self.main_window = window
        self._create_welcome_screen()

    def _create_welcome_screen(self):       
        # Crea un pannello per contenere tutti i widget
        self.welcome_panel = tk.PanedWindow(self.main_window, orient=tk.VERTICAL, bg='#E9E6DB')
        self.welcome_panel.pack(fill=tk.BOTH, expand=True)

        # Titolo di benvenuto
        welcome_label = tk.Label(
            self.welcome_panel,
            text="Welcome to GloveDataHub!",
            font=("Arial", 24, "bold"),
            justify="center",
            bg='#E9E6DB',
            fg='black',
            pady=10
        )
        welcome_label.pack()

        # Descrizione dell'applicazione
        description_text = (
            "This application will allow you to capture raw data from your haptic gloves.\n"
            "The steps to be performed in the following screens will be:"
        )
        description_label = tk.Label(
            self.welcome_panel,
            text=description_text,
            wraplength=700,
            font=("Arial", 20),
            bg='#E9E6DB',
            fg='black',
            pady=10,
            justify="left"
        )
        description_label.pack(anchor='w', padx=(30, 0), pady=(10, 0))

        # Step 1 da compiere
        step1_text = (
            "1 • Calibration of haptic gloves"
        )
        step1_label = tk.Label(
            self.welcome_panel,
            text=step1_text,
            font=("Arial", 20),
            bg='#E9E6DB',
            fg='black',
            pady=5,
            justify="left"
        )
        step1_label.pack(anchor='w', padx=(30, 0), pady=(5, 0))

        # Step 2 da compiere
        step2_text = (
            "2 • Entering user data"
        )
        step2_label = tk.Label(
            self.welcome_panel,
            text=step2_text,
            font=("Arial", 20),
            bg='#E9E6DB',
            fg='black',
            pady=5,
            justify="left"
        )
        step2_label.pack(anchor='w', padx=(30, 0), pady=(5, 0))
        
        # Step 3 da compiere
        step3_text = (
            "3 • Data acquisition"
        )
        step3_label = tk.Label(
            self.welcome_panel,
            text=step3_text,
            font=("Arial", 20),
            bg='#E9E6DB',
            fg='black',
            pady=5,
            justify="left"
        )
        step3_label.pack(anchor='w', padx=(30, 0), pady=(5, 20))

        # Crea un widget Frame per contenere il contenuto principale
        main_frame = tk.Frame(self.welcome_panel, bg='#E9E6DB')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Bottone per procedere
        next_button = tk.Button(main_frame, text="Next", command=lambda: self._show_start_calibration_screen(), font=("Arial", 18), bg='#E9E6DB', fg='black', padx=40, pady=20, highlightbackground='#E9E6DB')
        next_button.pack(side=tk.BOTTOM, anchor='e', padx=(0, 20), pady=(0, 20))

    def _show_start_calibration_screen(self):
        # Cancella tutto il contenuto attuale
        self.welcome_panel.destroy()
        self.start_calilbration_screen = StartCalibrationScreen(self.main_window)