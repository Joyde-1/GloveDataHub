import tkinter as tk
from PIL import Image, ImageTk

class WindowManager:

    def __init__(self):
        self.ghd_logo_path = 'GUI/images/logo_GloveDataHub_new.png'
        self.kore_logo_path = 'GUI/images/kore_Logo.png'

    def create_window(self, title, width, height, background):
        # Crea la finestra principale
        window = tk.Tk()

        self.set_window_title(window, title)

        self.set_window_geometry(window, width, height)

        self.set_window_background(window, background)

        return window

    def set_window_title(self, window, title):
        return window.title(title)

    def set_window_geometry(self, window, width, height):
        # Ottieni le dimensioni dello schermo automaticamente
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calcola le coordinate per centrare la finestra
        x_cordinate = int((screen_width / 2) - (width / 2))
        y_cordinate = int((screen_height / 2) - (height / 2))

        # Imposta la geometria della finestra con posizione centrata
        return window.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

    def set_window_background(self, window, background):
        return window.configure(bg=background)
    
    def set_window_header(self, window, title, font, background, frontground):
        # Carica e ridimensiona l'immagine del logo
        gdh_image = Image.open(self.ghd_logo_path)  # Assicurati di sostituire 'path/to/your/logo.png' con il percorso corretto
        gdh_image = ImageTk.PhotoImage(gdh_image)

        # Carica e ridimensiona l'immagine del logo Kore
        kore_image = Image.open(self.kore_logo_path)  # Assicurati di sostituire 'path/to/your/logo.png' con il percorso corretto
        kore_image = ImageTk.PhotoImage(kore_image)

        # Crea un frame per il titolo e il logo
        title_frame = tk.Frame(window, bg=background)
        title_frame.pack(fill='both', pady=(20, 20))

        # Inserisci il logo GDH nel frame
        logo_label = tk.Label(title_frame, image=gdh_image, bg=background)
        logo_label.pack(side=tk.LEFT, padx=(20, 0))

        # Inserisci il logo kore nel frame
        kore_label = tk.Label(title_frame, image=kore_image, bg=background)
        kore_label.pack(side=tk.RIGHT, padx=(0, 20))

        # Titolo dell'applicazione accanto al logo
        title_label = tk.Label(title_frame, text=title, font=font, bg=background, fg=frontground)
        title_label.pack(side=tk.LEFT, padx=0, expand=True, fill='both')

        return window