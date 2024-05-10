import tkinter as tk
from window_manager import WindowManager
import subprocess


class DataHandlerScreen:
    def __init__(self, window):
        self.main_window = window
        self._create_data_handler_screen()
    
    def _create_data_handler_screen(self):    
        # Crea un pannello per contenere tutti i widget
        self.data_handler_panel = tk.PanedWindow(self.main_window, orient=tk.VERTICAL, bg='#E9E6DB')
        self.data_handler_panel.pack(fill=tk.BOTH, expand=True)


        # Descrizione dell'applicazione
        description_text = (
            "Ensure name and surname are entered, specify measurement duration, and complete calibration before starting.\n"
        )
        description_label = tk.Label(
            self.data_handler_panel,
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
        main_frame = tk.Frame(self.data_handler_panel, bg='#E9E6DB')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Crea un widget Frame per contenere i bottoni
        button_frame = tk.Frame(self.data_handler_panel, bg='#E9E6DB')
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 20))
        
        # Bottone per tornare indietro
        back_button = tk.Button(button_frame, text="Back", command= self._show_start_calibration_screen, font=("Arial", 18), bg='#E9E6DB', fg='black', padx=10, pady=5, highlightbackground='#E9E6DB')
        back_button.pack(side=tk.LEFT, padx=(20, 10), anchor='w')
        
        # Bottone per iniziare la misurazione
        next_button = tk.Button(button_frame, text="Start the Measurement ", command=lambda: print("Start the Measurement"), font=("Arial", 18), bg='#E9E6DB', fg='black', padx=10, pady=5, highlightbackground='#E9E6DB')
        next_button.pack(side=tk.RIGHT, padx=(10, 20), anchor='e') 

    
    def _show_start_calibration_screen(self):
        # Import ritardato per evitare import circolare tra classe start_acalibration_screen e classe welcome_screen
        from start_calibration_screen import StartCalibrationScreen
        # Cancella tutto il contenuto attuale
        self.data_handler_panel.destroy()
        self.start_calibration_screen = StartCalibrationScreen(self.main_window)