import tkinter as tk
from PIL import Image, ImageTk

class WindowManager:

    def __init__(self):
        self.ghd_logo_path = 'GUI/images/logo_GloveDataHub_new.png'
        self.kore_logo_path = 'GUI/images/kore_Logo.png'

    def create_window(self, title, width, height, background):
        # Crea la finestra principale
        self.window = tk.Tk()

        self.set_window_title(title)

        self.set_window_geometry(width, height)

        self.set_window_background(background)

    def set_window_title(self, title):
        self.window.title(title)

    def set_window_geometry(self, width, height):
        # Ottieni le dimensioni dello schermo automaticamente
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calcola le coordinate per centrare la finestra
        x_cordinate = int((screen_width / 2) - (width / 2))
        y_cordinate = int((screen_height / 2) - (height / 2))

        # Imposta la geometria della finestra con posizione centrata
        self.window.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

    def set_window_background(self, background):
        self.window.configure(bg=background)
    
    def set_window_header(self, title, font, background, frontground):
        # Carica e ridimensiona l'immagine del logo
        gdh_original_image = Image.open(self.ghd_logo_path)  # Assicurati di sostituire 'path/to/your/logo.png' con il percorso corretto
        self.gdh_image = ImageTk.PhotoImage(gdh_original_image)

        # Carica e ridimensiona l'immagine del logo Kore
        kore_original_image = Image.open(self.kore_logo_path)  # Assicurati di sostituire 'path/to/your/logo.png' con il percorso corretto
        self.kore_image = ImageTk.PhotoImage(kore_original_image)

        # Crea un frame per il titolo e il logo
        self.title_frame = tk.Frame(self.window, bg=background)
        self.title_frame.pack(fill='both', pady=(20, 20))

        # Inserisci il logo GDH nel frame
        self.logo_label = tk.Label(self.title_frame, image=self.gdh_image, bg=background)
        self.logo_label.pack(side=tk.LEFT, padx=(20, 0))

        # Inserisci il logo kore nel frame
        self.kore_label = tk.Label(self.title_frame, image=self.kore_image, bg=background)
        self.kore_label.pack(side=tk.RIGHT, padx=(0, 20))

        # Titolo dell'applicazione accanto al logo
        self.title_label = tk.Label(self.title_frame, text=title, font=font, bg=background, fg=frontground)
        self.title_label.pack(side=tk.LEFT, padx=0, expand=True, fill='both')

    def set_window_screen(self):
        pass

    def get_window(self):
        return self.window