import tkinter as tk
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def create_welcome_window():
# Crea la finestra principale
    window = tk.Tk()
    window.title("GloveDataHub")

    # Configura le dimensioni della finestra e il colore di sfondo
    window.geometry('800x600')
    window.configure(bg='white')

    # Carica e ridimensiona l'immagine del logo
    original_image = Image.open('/Users/giovanni/Desktop/Human-Centered AI/GloveDataHub/GUI/images/logo_GloveDataHub.png')  # Assicurati di sostituire 'path/to/your/logo.png' con il percorso corretto
    resized_image = original_image.resize((100, 100))
    logo_image = ImageTk.PhotoImage(resized_image)

    # Crea un frame per il titolo e il logo
    title_frame = tk.Frame(window, bg='white')
    title_frame.pack(pady=(20, 10))

    # Inserisci il logo nel frame
    logo_label = tk.Label(title_frame, image=logo_image, bg='white')
    logo_label.pack(side=tk.LEFT, padx=10)

    # Titolo dell'applicazione accanto al logo
    title_label = tk.Label(title_frame, text="GloveDataHub", font=("Arial", 24), bg='white', fg='black')
    title_label.pack(side=tk.LEFT, padx=10)

    # Paragrafo di descrizione
    description = ("Welcome to GloveDataHub, your interface for managing and "
                   "visualizing data from your sensor-equipped gloves. This tool "
                   "allows you to access and analyze the data in real-time.")
    description_label = tk.Label(window, text=description, wraplength=500, justify="left", bg='white', fg='black')
    description_label.pack(pady=(0, 20))

    # Crea un widget Frame per contenere il contenuto principale
    main_frame = tk.Frame(window, bg='white')
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Area di testo nella parte superiore
    #text_area = tk.Text(main_frame, height=15, width=75, bg='white', fg='black', font=("Arial", 12))
    #text_area.pack(padx=20, pady=(0, 20))

    # Bottone per procedere
    next_button = tk.Button(main_frame, text="Next", command=lambda: print("Next was clicked"))
    next_button.pack(side=tk.BOTTOM, anchor='e', padx=20, pady=20)

    # Avvia il main loop della finestra
    window.mainloop()

if __name__ == "__main__":
    create_welcome_window()
