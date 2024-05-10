import tkinter as tk
from window_manager import WindowManager
import subprocess


class StartCalibrationScreen:
    def __init__(self, window):
        self.main_window = window
        self._create_start_calibration_screen()
    
    def _create_start_calibration_screen(self):    
        # Crea un pannello per contenere tutti i widget
        self.calibration_panel = tk.PanedWindow(self.main_window, orient=tk.VERTICAL, bg='#E9E6DB')
        self.calibration_panel.pack(fill=tk.BOTH, expand=True)


        # Descrizione dell'applicazione
        description_text = (
            "Activate the SenseCom application by clicking the button at the bottom center to calibrate your haptic gloves.\n"
        )
        description_label = tk.Label(
            self.calibration_panel,
            text=description_text,
            wraplength=600,
            font=("Arial", 20),
            bg='#E9E6DB',
            fg='black',
            pady=10,
            justify="center"
        )
        
        description_label.pack(expand=True)

        # Crea un widget Frame per contenere il contenuto principale
        main_frame = tk.Frame(self.calibration_panel, bg='#E9E6DB')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Crea un widget Frame per contenere i bottoni
        button_frame = tk.Frame(self.calibration_panel, bg='#E9E6DB')
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 20))
        
        # Bottone per tornare indietro
        back_button = tk.Button(button_frame, text="Back", command= self._show_start_calibration_screen, font=("Arial", 18), bg='#E9E6DB', fg='black', padx=10, pady=5, highlightbackground='#E9E6DB')
        back_button.pack(side=tk.LEFT, padx=(20, 10), anchor='w')
        
        # Bottone per avviare SenseCom
        SenseCom_button = tk.Button(button_frame, text="Start SenseCom", command= self.launch_calibration_app, font=("Arial", 18), bg='#E9E6DB', fg='black', padx=10, pady=5, highlightbackground='#E9E6DB')
        SenseCom_button.pack(side=tk.LEFT, expand= True, anchor='center', padx=(10, 10))

        # Bottone per andare avanti
        next_button = tk.Button(button_frame, text="Next", command=lambda: print("Next"), font=("Arial", 18), bg='#E9E6DB', fg='black', padx=10, pady=5, highlightbackground='#E9E6DB')
        next_button.pack(side=tk.LEFT, padx=(10, 20), anchor='e')

    def launch_calibration_app(self):
        # Percorso dell'applicazione di calibrazione (Attenzione c'è questo percorso perchè mi trovo su parallels !)
        path_to_app = "C:\Program Files (x86)\SenseCom\SenseCom.exe"
        subprocess.Popen([path_to_app])

    def _show_start_calibration_screen(self):
        # Import ritardato per evitare import circolare tra classe start_acalibration_screen e classe welcome_screen
        from welcome_screen import WelcomeScreen
        # Cancella tutto il contenuto attuale
        self.calibration_panel.destroy()
        self.start_welcome_screen = WelcomeScreen(self.main_window)